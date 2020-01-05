# ebpH --  An eBPF intrusion detection program.
# -------  Monitors system call patterns and detect anomalies.
# Copyright 2019 William Findlay (williamfindlay@cmail.carleton.ca) and
# Anil Somayaji (soma@scs.carleton.ca)
#
# Based on Anil Somayaji's pH
#  http://people.scs.carleton.ca/~mvvelzen/pH/pH.html
#  Copyright 2003 Anil Somayaji
#
# USAGE: ebphd <COMMAND>
#
# Licensed under GPL v2 License

import os, sys
import json
import time
from functools import wraps

import config

def path(f):
    """
    Return the path of a file relative to the root dir of this project (parent directory of "src").
    """
    curr_dir = os.path.realpath(os.path.dirname(__file__))
    project_dir = os.path.realpath(os.path.join(curr_dir,".."))
    path = os.path.realpath(os.path.join(project_dir, f))
    return path

def locks(lock):
    """
    Decorated functions take the specified lock before invoking and release it after returning.
    Usage:
        @lock(the_lock)
        def func ...
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            lock.acquire()
            ret =  func(*args, **kwargs)
            lock.release()
            return ret
        return inner
    return decorator

def to_json_bytes(x, encoding='utf-8'):
    """
    Serialize json.
    """
    return json.dumps(x).encode(encoding)

def from_json_bytes(x, encoding='utf-8'):
    """
    Unserialize json.
    """
    return json.loads(x.decode(encoding))

def receive_message(sock):
    """
    Receive a message of arbitrary length over a stream socket.
    Stop when we see config.sentinel or the connection closes (whichever happens first).
    """
    total_data = []
    sentinel = False

    while True:
        msg = sock.recv(config.socket_buff_size)
        msg = msg.strip()
        if not msg:
            break
        if bytes([msg[-1]]) == config.socket_sentinel:
            msg = msg[:-1]  # Remove sentinel from message
            sentinel = True # Mark that we have seen it
        total_data.append(msg)
        if sentinel:
            break

    return b"".join(total_data)

def send_message(sock, data):
    """
    Send a message over a stream socket, terminating automatically with config.sentinel.
    """
    sock.send(b"".join([data, config.socket_sentinel]))