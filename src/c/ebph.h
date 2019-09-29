/* ebpH --  An eBPF intrusion detection program.
 * -------  Monitors system call patterns and detect anomalies.
 * Copyright 2019 William Findlay (williamfindlay@cmail.carleton.ca) and
 * Anil Somayaji (soma@scs.carleton.ca)
 *
 * Based on Anil Somayaji's pH
 *  http://people.scs.carleton.ca/~mvvelzen/pH/pH.html
 *  Copyright 2003 Anil Somayaji
 *
 * USAGE: ebphd <COMMAND>
 *
 * Licensed under GPL v2 License */

#ifndef EBPH_H
#define EBPH_H

#include "defs.h"

/* Struct definitions below this line ------------------- */

struct ebpH_profile
{
    u8 frozen;
    u8 normal;
    u64 normal_time;
    u64 window_size;
    u64 normal_count;
    u64 last_mod_count;
    u64 train_count;
    u64 anomalies;
    u8 flags[EBPH_LOOKAHEAD_ARRAY_SIZE];
    u64 key;
    char comm[EBPH_FILENAME_LEN];
#if LINUX_VERSION_CODE >= KERNEL_VERSION(5,1,0)
    struct bpf_spin_lock lock;
#endif
};

struct ebpH_locality
{
    u8 win[EBPH_LOCALITY_WIN];
    int lfc;
    int lfc_max;
};

struct ebpH_process
{
    struct ebpH_locality lf;
    u64 seq[EBPH_SEQLEN];
    u64 count;
    u64 pid_tgid;
    u64 exe_key;
#if LINUX_VERSION_CODE >= KERNEL_VERSION(5,1,0)
    struct bpf_spin_lock lock;
#endif
};

struct ebpH_anomaly
{
    u32 pid;
    u64 syscall;
    int anomalies;
    u64 key;
    char comm[EBPH_FILENAME_LEN];
};

struct ebpH_information
{
    u32 pid;
    u64 key;
    char comm[EBPH_FILENAME_LEN];
};

static int ebpH_reset_ALF(struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_seq_to_lookahead(struct ebpH_profile *profile, struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_test(struct ebpH_profile *profile, struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_process_normal(struct ebpH_profile *profile, struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_train(struct ebpH_profile *profile, struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_start_normal(struct ebpH_profile *profile, struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_stop_normal(struct ebpH_profile *profile, struct ebpH_process *process, struct pt_regs *ctx);
static int ebpH_set_normal_time(struct ebpH_profile *profile, struct pt_regs *ctx);
static int ebpH_check_normal_time(struct ebpH_profile *profile, struct pt_regs *ctx);
static int ebpH_process_syscall(struct ebpH_process *, u64 *, struct pt_regs *);
static int ebpH_on_profile_exec(u64 *, u64 *, struct pt_regs *, char *);
static int ebpH_start_tracing(struct ebpH_profile *, u64 *, struct pt_regs *);
static u64 ebpH_get_ppid_tgid();

#endif
/* EBPH_H */