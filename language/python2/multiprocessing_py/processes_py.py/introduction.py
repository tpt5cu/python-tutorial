# https://docs.python.org/2/library/msltiprocessing.html


import os
from multiprocessing import Process
import time


"""
The multiprocessing module has a start() method. This start() method calls Popen(self). This Popen() constructor (from forking.py) calls os.fork()
inside of it. fork() is a system call that creates a child process with the same address space as the parent process. The address space is shared
until the child or parent writes to the address space, at which point both processes get a unique copy of the data in the address space (see my
notes).
- The Popen() constructor is NOT the same the subprocess Popen().
"""


global_variable = []


def create_and_join_process():
    """
    The most important parameters of the Process() constructor are target, args, and (maybe) kwargs.
    - target: the callable object that will be invoked by the run() method. Note that start() arranges for the run() method to run in a separate
    process
    - args: arguments to be passed to the callable object. If there is only one argument, it MUST be followed by a comma!
    - kwargs: keyword arguments to be passed to the callable object
    """
    # args also accepts a list instead of a tuple!
    #p = Process(target=print_numbers, args=(10,))
    p = Process(target=print_numbers, args=[10])
    p.start()
    print(p.pid) # <Number>
    print(p.is_alive()) # True
    p.join()


def print_numbers(start):
    """
    The global_variable (a list) starts as empty, then the main process adds an item to the list. Next, the child process is forked because that's how
    the multiprocessing module works. Thus, the child process gets a copy of the global_variable which already has one element in it. Next, the child
    process adds another element to this NEW list which is a copy of the old list. I'm sure that it's modifying a NEW list because in
    check_address_space() the global_variable is unchanged after the child process runs.
    - In the main process the print out is:
        - []
        - ['Added from main process']
    - In the child process the print out is:
        - ['Added from main process']
        - ['Added from main process', 'Added from child process']
    """
    for num in range(start, start + 5):
        time.sleep(1)
        print(num)
    global global_variable
    print(global_variable)
    if start == 10:
        global_variable.append("Added from child process")
    else:
        global_variable.append("Added from main process")
    print(global_variable)


def check_address_space():
    # Start in main process.
    print_numbers(0)
    # Start same function in child process. Also set global variable
    time.sleep(0.5)
    create_and_join_process()
    global global_variable
    # This line always prints as ['Added from main process']
    print(global_variable)


def view_pid():
    """The pid of a process doesn't exist until the process is spawned (i.e. after start() is called)."""
    ref = []
    p = Process(target=view_pid_from_subprocess, args=(ref,))
    ref.append(p)
    print("PID is: " + str(p.pid)) # None
    p.start()
    print("PID is: " + str(p.pid)) # <number>


def view_pid_from_subprocess(reference):
    # This is a bad way
    print("PID from inside subprocess is: " + str(reference[0].pid)) # Number
    # This is the good way
    print("PID from inside subprocess is: " + str(os.getpid()))


if __name__ == "__main__":
    check_address_space()
    #view_pid()