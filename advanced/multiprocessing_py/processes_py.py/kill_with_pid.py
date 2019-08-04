# https://stackoverflow.com/questions/173278/is-there-a-way-to-prevent-a-systemexit-exception-raised-from-sys-exit-from-bei


import os, sys, signal, multiprocessing, time
from exceptions import SystemExit


"""
Hard way:
1) Users submits a DELETE request.
2) I look up the PID.txt file in their directory, which contains the PID of their process
3) Pass that specific PID into a message to all worker Process
4) Worker processes will check to see if their PID matches the PID I want to kill
5) Worker with matching PID terminates itself, that PID is removed from the messages

Even harder way:
Store PIDs of ongoing processes in memory and don't use the filesystem to handle process coordination.

Easy way:
1) Get the PID to kill
2) Use os.kill(<PID>, <signal>)
"""


def create_process(limit, wait, spaces, should_raise=False):
    p = multiprocessing.Process(target=print_numbers, args=(limit, wait, spaces, should_raise))
    p.start()
    return p


def print_numbers(limit, wait, spaces, should_raise):
    try:
        for x in range(limit):
            print(spaces + str(x))
            time.sleep(wait)
        if should_raise:
            # This is the exact same exception and error integer that I'm getting in web.py
            #raise SystemExit(0)
            raise Exception() # raise something else to test
    except Exception:
        print("There was an exception")
    except SystemExit as e:
        if e.code == 0:
            print("SystemExit occurred successfully")


def spawn_processes():
    """
    I must join the child processes to the main process in order to use the debugger to inspect a child process. If I
    don't, then when the main process exits, the debugger will shut down, even if the child processes were still executing.
    """
    p1 = create_process(5, 1.0, " ")
    p2 = create_process(5, 1.5, "    ", True)
    p3 = create_process(5, 2, "        ")
    p1.join()
    p2.join()
    p3.join()
    #time.sleep(4)
    #os.kill(p1.pid, signal.SIGTERM)
    #os.kill(p2.pid, signal.SIGTERM)


if __name__ == "__main__":
    spawn_processes()