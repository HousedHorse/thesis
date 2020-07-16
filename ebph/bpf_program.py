"""
    ebpH (Extended BPF Process Homeostasis)  A host-based IDS written in eBPF.
    Copyright (C) 2019-2020  William Findlay

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    A wrapper around the BPF program. Exposes methods for interacting
    with it from userspace and for handling events.

    2020-Jul-13  William Findlay  Created this.
"""

import os
import time
import atexit
import ctypes as ct
from collections import defaultdict
from typing import List, Optional

from bcc import BPF

from ebph.libebph import Lib
from ebph.logger import get_logger
from ebph.structs import (
    EBPHProfileStruct,
    EBPH_SETTINGS,
    calculate_profile_magic,
)
from ebph import defs

logger = get_logger()


def ringbuf_callback(bpf, map_name, infer_type=True):
    def _inner(func):
        def _wrapper(ctx, data, size):
            if infer_type:
                data = bpf[map_name].event(data)
            func(ctx, data, size)

        bpf[map_name].open_ring_buffer(_wrapper)

    return _inner


class BPFProgram:
    def __init__(self, debug: bool = False, log_sequences: bool = False):
        self.bpf = None
        self.usdt_contexts = []
        self.seqstack_inner_bpf = None
        self.cflags = []
        self.debug = debug

        self.profile_key_to_exe = defaultdict(lambda: '[unknown]')
        self.syscall_number_to_name = defaultdict(lambda: '[unknown]')

        self._set_cflags()
        self._load_bpf()
        self._register_ring_buffers()
        self.load_profiles()

        atexit.register(self._cleanup)

        self.change_setting(EBPH_SETTINGS.LOG_SEQUENCES, log_sequences)

        self.change_setting(EBPH_SETTINGS.NORMAL_WAIT, defs.NORMAL_WAIT)
        self.change_setting(EBPH_SETTINGS.NORMAL_FACTOR, defs.NORMAL_FACTOR)
        self.change_setting(
            EBPH_SETTINGS.NORMAL_FACTOR_DEN, defs.NORMAL_FACTOR_DEN
        )
        self.change_setting(EBPH_SETTINGS.ANOMALY_LIMIT, defs.ANOMALY_LIMIT)

        self.start_monitoring()

    def on_tick(self) -> None:
        try:
            self.bpf.ring_buffer_consume()
        except Exception:
            pass

    def change_setting(self, setting: EBPH_SETTINGS, value: int) -> int:
        if value < 0:
            logger.error(
                'Value for {setting.name} must be a positive integer.'
            )
            return -1

        rc = Lib.set_setting(setting, value)
        err = os.strerror(ct.get_errno())

        if rc < 0:
            logger.error(f'Failed to set {setting.name} to {value}: {err}')
        if rc == 1:
            logger.info(f'{setting.name} is already set to {value}.')
        if rc == 0:
            logger.info(f'{setting.name} set to {value}.')
        return rc

    def get_setting(self, setting: EBPH_SETTINGS) -> Optional[int]:
        try:
            return self.bpf['_ebph_settings'][ct.c_uint64(setting)].value
        except (KeyError, IndexError):
            logger.error(f'Failed to get {setting.name}: Key does not exist')
        return None

    def start_monitoring(self, silent=False) -> int:
        if self.get_setting(EBPH_SETTINGS.MONITORING) and not silent:
            logger.info('System is already being monitored.')
            return 1
        rc = Lib.set_setting(EBPH_SETTINGS.MONITORING, True)
        err = os.strerror(ct.get_errno())
        if rc < 0 and not silent:
            logger.error(f'Failed to start monitoring: {err}')
        if rc == 0 and not silent:
            logger.info('Started monitoring the system.')
        return rc

    def stop_monitoring(self, silent=False) -> int:
        if not self.get_setting(EBPH_SETTINGS.MONITORING) and not silent:
            logger.info('System is not being monitored.')
            return 1
        rc = Lib.set_setting(EBPH_SETTINGS.MONITORING, False)
        err = os.strerror(ct.get_errno())
        if rc < 0 and not silent:
            logger.error(f'Failed to stop monitoring: {err}')
        if rc == 0 and not silent:
            logger.info('Stopped monitoring the system.')
        return rc

    def save_profiles(self) -> int:
        saved = 0
        error = 0

        logger.info('Saving profiles...')

        for k in self.bpf['profiles'].keys():
            key = k.value
            exe = self.profile_key_to_exe[key]
            fname = f'{key}'
            try:
                profile = EBPHProfileStruct.from_bpf(
                    self.bpf, exe.encode('ascii'), key
                )
                with open(os.path.join(defs.EBPH_DATA_DIR, fname), 'wb') as f:
                    f.write(profile)
                logger.debug(f'Successfully saved profile {fname} ({exe}).')
            except Exception as e:
                logger.error(
                    f'Unable to save profile {fname} ({exe}).', exc_info=e
                )
                error += 1
            saved += 1
        logger.info(f'Saved {saved} profiles successfully!')
        return saved, error

    def load_profiles(self) -> None:
        loaded = 0
        error = 0

        logger.info('Loading profiles...')
        # If we are monitoring, stop
        monitoring = self.get_setting(EBPH_SETTINGS.MONITORING)

        if monitoring:
            self.stop_monitoring()

        for fname in os.listdir(defs.EBPH_DATA_DIR):
            try:
                profile = EBPHProfileStruct()
                with open(os.path.join(defs.EBPH_DATA_DIR, fname), 'rb') as f:
                    f.readinto(profile)
                # Wrong version
                if profile.magic != calculate_profile_magic():
                    logger.debug(f'Wrong magic number for profile {fname}, skipping.')
                    continue
                profile.load_into_bpf(self.bpf)
                self.profile_key_to_exe[profile.profile_key] = profile.exe.decode('ascii')
                exe = self.profile_key_to_exe[profile.profile_key]
                logger.debug(f'Successfully loaded profile {fname} ({exe}).')
            except Exception as e:
                logger.error(f'Unable to load profile {fname}.', exc_info=e)
                error += 1
            loaded += 1

        # If we were monitoring, resume
        if monitoring:
            self.start_monitoring()
        logger.info(f'Loaded {loaded} profiles successfully!')
        return loaded, error

    def get_profile(self, key: int) -> ct.Structure:
        return self.bpf['profiles'][ct.c_uint64(key)]

    def get_process(self, pid: int) -> ct.Structure:
        return self.bpf['task_states'][ct.c_uint32(pid)]

    def normalize_profile(self, profile_key: int):
        try:
            rc = Lib.normalize_profile(profile_key)
        except Exception as e:
            logger.error(f'Unable to normalize profile.', exc_info=e)
            return -1
        if rc < 0:
            logger.error(f'Unable to normalize profile: {os.strerror(ct.get_errno())}')
        return rc



    def _register_ring_buffers(self) -> None:
        logger.info('Registering ring buffers...')

        @ringbuf_callback(self.bpf, 'new_profile_events')
        def new_profile_events(ctx, event, size):
            """
            new_profile_events.

            Callback for new profile creation.
            Logs creation and caches key -> pathname mapping
            for later use.
            """
            pathname = event.pathname.decode('utf-8')
            self.profile_key_to_exe[event.profile_key] = pathname

            if self.debug:
                logger.info(
                    f'Created new profile for {pathname} ({event.profile_key}).'
                )
            else:
                logger.info(f'Created new profile for {pathname}.')

        @ringbuf_callback(self.bpf, 'anomaly_events')
        def anomaly_events(ctx, event, size):
            """
            anomaly_events.

            Log anomalies.
            """
            exe = self.profile_key_to_exe[event.profile_key]
            syscall_number = event.syscall
            syscall_name = self.syscall_number_to_name[syscall_number]
            misses = event.misses
            pid = event.pid
            count = event.task_count

            logger.audit(
                f'Anomalous {syscall_name} ({misses} misses) '
                f'in PID {pid} ({exe}) after {count} calls.'
            )

        @ringbuf_callback(self.bpf, 'new_sequence_events')
        def new_sequence_events(ctx, event, size):
            """
            new_sequence_events.

            Log new sequences.
            """
            exe = self.profile_key_to_exe[event.profile_key]
            sequence = [
                self.syscall_number_to_name[call]
                for call in event.sequence
                if call != defs.BPF_DEFINES['EBPH_EMPTY']
            ]
            sequence = reversed(sequence)
            pid = event.pid
            profile_count = event.profile_count
            task_count = event.task_count

            logger.debug(
                f'New sequence in PID {pid} ({exe}), task count = {task_count}, profile count = {profile_count}.'
            )
            logger.sequence(f'PID {pid} ({exe}): ' + ', '.join(sequence))

        @ringbuf_callback(self.bpf, 'start_normal_events')
        def start_normal_events(ctx, event, size):
            """
            start_normal_events.

            Log when a profile starts normal monitoring.
            """
            exe = self.profile_key_to_exe[event.profile_key]
            profile_count = event.profile_count
            sequences = event.sequences
            train_count = event.train_count
            last_mod_count = event.last_mod_count

            in_task = event.in_task
            task_count = event.task_count
            pid = event.pid

            if in_task:
                logger.info(
                    f'PID {pid} ({exe}) now has {train_count} '
                    f'training calls and {last_mod_count} since last '
                    f'change ({profile_count} total).'
                )
                logger.info(
                    f'Starting normal monitoring in PID {pid} ({exe}) '
                    f'after {task_count} calls ({sequences} sequences).'
                )
            else:
                logger.info(
                    f'{exe} now has {train_count} '
                    f'training calls and {last_mod_count} since last '
                    f'change ({profile_count} total).'
                )
                logger.info(
                    f'Starting normal monitoring for {exe} '
                    f'with {sequences} sequences.'
                )

        @ringbuf_callback(self.bpf, 'stop_normal_events')
        def stop_normal_events(ctx, event, size):
            """
            stop_normal_events.

            Log when a profile stops normal monitoring.
            """
            exe = self.profile_key_to_exe[event.profile_key]
            anomalies = event.anomalies
            anomaly_limit = event.anomaly_limit

            in_task = event.in_task
            task_count = event.task_count
            pid = event.pid

            if in_task:
                logger.info(
                    f'Stopped normal monitoring in PID {pid} ({exe}) '
                    f'after {task_count} calls and {anomalies} anomalies '
                    f'(limit {anomaly_limit}).'
                )
            else:
                logger.info(
                    f'Stopped normal monitoring for {exe} '
                    f'with {anomalies} anomalies (limit {anomaly_limit}).'
                )

    def _generate_syscall_defines(self, flags: List[str]) -> None:
        from bcc.syscall import syscalls

        for num, name in syscalls.items():
            name = name.decode('utf-8').upper()
            self.syscall_number_to_name[num] = name
            definition = f'-DEBPH_SYS_{name}={num}'
            flags.append(definition)

    def _calculate_boot_epoch(self):
        boot_time = time.monotonic() * int(1e9)
        boot_epoch = time.time() * int(1e9) - boot_time
        return int(boot_epoch)

    def _set_cflags(self) -> None:
        logger.info('Setting cflags...')

        self.cflags.append(f'-I{defs.BPF_DIR}')
        for k, v in defs.BPF_DEFINES.items():
            self.cflags.append(f'-D{k}={v}')

        if self.debug:
            self.cflags.append('-DEBPH_DEBUG')

        for flag in self.cflags:
            logger.debug(f'Using {flag}...')

        self.cflags.append(
            f'-DEBPH_BOOT_EPOCH=((u64){self._calculate_boot_epoch()})'
        )
        self._generate_syscall_defines(self.cflags)

    def _load_bpf(self) -> None:
        assert self.bpf is None
        logger.info('Loading BPF program...')

        with open(defs.BPF_PROGRAM_C, 'r') as f:
            bpf_text = f.read()

        self.bpf = BPF(
            text=bpf_text, usdt_contexts=[Lib.usdt_context], cflags=self.cflags
        )
        # FIXME: BPF cleanup function is segfaulting, so unregister it for now.
        # It actually doesn't really do anything particularly useful.
        atexit.unregister(self.bpf.cleanup)

    def _cleanup(self) -> None:
        self.save_profiles()
        del self.bpf
        self.bpf = None