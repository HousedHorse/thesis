# ebpH

## Description

ebpH stands for Extended BPF Process Homeostasis.

ebpH is a modern host-based intrusion detection system for Linux 5.8+ that
leverages the power of Extended BPF (eBPF) to monitor processes and detect anomalous behavior.
This effectively constitutes an eBPF implementation of [pH (Process Homeostasis)](https://people.scs.carleton.ca/~mvvelzen/pH/pH.html).

## Disclaimer

This product comes with no warranty, and is built as a research system. It should be perfectly safe to run on your system due to the safety guarantees of eBPF, but we make no claims about functionality.

## Papers

### ebpH

- [My thesis](https://www.cisl.carleton.ca/~will/written/coursework/undergrad-ebpH-thesis.pdf)

### pH

- [My supervisor's original dissertation on pH](https://people.scs.carleton.ca/~soma/pubs/soma-diss.pdf)
- [A Sense of Self for UNIX Processes](https://www.cs.unm.edu/~immsec/publications/ieee-sp-96-unix.pdf)
- [Lightweight Intrustion Detection for Networked Operating Systems](http://people.scs.carleton.ca/~soma/pubs/jcs1998.pdf)
- [Lookahead Pairs and Full Sequences: A Tale of Two Anomaly Detection Methods](http://people.scs.carleton.ca/~soma/pubs/inoue-albany2007.pdf)

## Prerequisites

1. Linux 5.8+ compiled with at least `CONFIG_BPF=y`, `CONFIG_BPF_SYSCALL=y`, `CONFIG_BPF_JIT=y`, `CONFIG_TRACEPOINTS=y`, `CONFIG_BPF_LSM=y`, `CONFIG_DEBUG_INFO=y`, `CONFIG_DEBUG_INFO_BTF=y`, `CONFIG_LSM="bpf"`. pahole >= 0.16 must be installed for the kernel to be built with BTF info.
1. Either the latest version of bcc from https://github.com/iovisor/bcc or bcc version 0.16+.
    - If building from source, be sure to include `-DPYTHON_CMD=python3` in your the cmake flags
1. Python 3.8+

## Installation

1. Install the prerequisites (see above).
1. `git clone https://github.com/willfindlay/ebpH`
1. `cd ebpH && make install` (You will be asked for your password)
1. To install the systemd unit: `make systemd` (You will be asked for your password)

## How to Use / Examples

1. Run `$ sudo ebphd start` to start the daemon.
1. Run `$ sudo ebph admin status` to check daemon status.
1. Run `$ sudo ebph ps` to check monitored processes.
1. Run `$ sudo ebph ps -p` to list all active profiles.

Or, with systemd:

1. Run `$ sudo systemctl start ebphd` to start the daemon if not already running.
