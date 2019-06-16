import os
from multiprocessing import Process
import time

"""
https://docs.python.org/2/library/msltiprocessing.html
"""

"""
Fun background:
- A callable object is any object that has a special __call__ method. All Python functions are just regular old objects that have a __call__ method.
"""

def create_process():
    """
    The most important parameters of the Process() constructor are target, args, and (maybe) kwargs.
    - target: the callable object that will be invoked by the run() method. Note that start() arranges for the run() method to run in a separate
    process
    - args: arguments to be passed to the callable object. If there is only one argument, it MUST be followed by a comma!
    - kwargs: keyword arguments to be passed to the callable object
    """
    p = Process(target=print_numbers, args=(10,))
    p.start()
    print(p.pid)
    print(p.is_alive())
    p.join()

def print_numbers(start):
    for num in range(start, start + 5):
        time.sleep(1)
        print(num)

def join_process():
    create_process()
    print_numbers(0)

def view_pid():
    """ The pid of a process doesn't exist until the process is spawned (i.e. after start() is called) """
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
    #join_process()
    view_pid()