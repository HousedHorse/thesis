#! /usr/bin/env python3

# ebpH --  Monitor syscall sequences and detect anomalies
# Copyright 2019 Anil Somayaji (soma@scs.carleton.ca) and
# William Findlay (williamfindlay@cmail.carleton.ca)
#
# Based on Sasha Goldshtein's syscount
#  https://github.com/iovisor/bcc/blob/master/tools/syscount.py
#  Copyright 2017, Sasha Goldshtein.
# And on Anil Somayaji's pH
#  http://people.scs.carleton.ca/~mvvelzen/pH/pH.html
#  Copyright 2003 Anil Somayaji
#
# USAGE: ebpH.py <COMMAND>
#
# Licensed under GPL v3 License

from time import sleep, strftime
import subprocess
import argparse
import textwrap
import errno
import itertools
import sys
import signal
import os
from bcc import BPF
from bcc.utils import printb
from bcc.syscall import syscall_name, syscalls
import ctypes as ct
from pprint import pprint

# TODO: change this to a directory in root somewhere
# directory in which profiles are stored
PROFILE_DIR = "./profiles"
# path of profile loader executable
LOADER_PATH = os.path.abspath("profile_loader")
# length of sequences
SEQLEN = 8

# signal handler
def signal_ignore(signal, frame):
    print()

def handle_errno(errstr):
    try:
        return abs(int(errstr))
    except ValueError:
        pass

    try:
        return getattr(errno, errstr)
    except AttributeError:
        raise argparse.ArgumentTypeError("couldn't map %s to an errno" % errstr)

def print_sequences():
    # fetch BPF hashmap
    seq_hash = bpf["seq"]

    # print system time
    print()
    print("[%s]" % strftime("%H:%M:%S %p"))

    # print sequence for each inspected process
    for p, s in seq_hash.items():
        pid = p.value >> 32
        names = map(syscall_name, s.seq);
        calls = map(str, s.seq);

        # separator
        print()
        print("----------------------------------------------------------")
        print()

        # print the process and the sequence length
        print("%-8s %-20s %-8s" % ("PID","COMM","COUNT"))
        print("%-8d %-20s %-8s" % (pid, s.comm.decode('utf-8'), s.count));

        # list of sequences by "Call Name(Call Number),"
        print()
        print('Sequence:')
        arr = []
        for i,(call,name) in enumerate(zip(calls,names)):
            if i >= SEQLEN or i >= s.count:
                break;
            arr.append("%s(%s)" % (name.decode('utf-8'), call))
        print(textwrap.fill(", ".join(arr)))
        print()

# save profiles to disk
# TODO: replace comm with /proc/<PID>/exe contents
def save_profiles(profiles):
    for k,profile in profiles:
        comm = profile.comm.decode('utf-8')
        comm = comm.replace(r'/',r'')
        profile_path = os.path.join(PROFILE_DIR, comm)
        with open(profile_path, "w") as f:
            printb(profile,file=f)

# load profiles from disk
def load_profiles():
    for profile in os.listdir(PROFILE_DIR):
        profile_path = os.path.join(PROFILE_DIR, profile)
        # run the profile_loader which is registered with a uretprobe
        subprocess.run([LOADER_PATH,profile_path])

# load a bpf program from a file
def load_bpf(code):
    with open(code, "r") as f:
        text = f.read()

    return text

# main control flow
if __name__ == "__main__":
    commands = ["start", "stop"]

    parser = argparse.ArgumentParser(description="Monitor system call sequences and detect anomalies.")
    #parser.add_argument("command", metavar="COMMAND", type=str.lower, choices=commands,
    #                    help="Command to run. Possible commands are %s." % ', '.join(commands))
    # TODO: implement this functionality (or perhaps remove it since it's only useful for testing)
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="write to a log file specified by <output>")
    args = parser.parse_args()

    # TODO: daemonize the process
    # TODO: use command to control daemonized process
    #command = args.command

    # check privileges
    if not ('SUDO_USER' in os.environ and os.geteuid() == 0):
        print("This script must be run with root privileges! Exiting.")
        exit()

    # read BPF embedded C from bpf.c
    text = load_bpf("./bpf.c")

    # compile ebpf code
    bpf = BPF(text=text)
    # register callback to load profiles
    bpf.attach_uretprobe(name=LOADER_PATH, sym='load_profile', fn_name='load_profile')

    # load in any profiles
    load_profiles()

    # create PROFILE_DIR if it does not exist
    if not os.path.exists(PROFILE_DIR):
        os.mkdir(PROFILE_DIR)

    print("Tracing syscall sequences of length %s... Ctrl+C to quit." % SEQLEN)
    exiting = 0
    while True:
        # update the hashmap of sequences
        try:
            sleep(1)
        except KeyboardInterrupt: # handle exiting gracefully
            exiting = 1
            signal.signal(signal.SIGINT, signal_ignore)

        # exit control flow
        if exiting:
            # maybe redirect output
            if args.output is not None:
                sys.stdout = open(args.output,"w+")

            print_sequences()
            seq_hash = bpf["seq"]
            save_profiles(seq_hash.items())

            # clear the BPF hashmap
            seq_hash.clear()

            # reset stdout
            if args.output is not None:
                sys.stdout.close()
                sys.stdout = sys.__stdout__

            print()
            print("Detaching...")
            exit()
