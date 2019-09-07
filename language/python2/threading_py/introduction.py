# https://docs.python.org/2.7/glossary.html#term-global-interpreter-lock - brief description of GIL
# https://stackoverflow.com/questions/3384385/python-3-2-gil-good-bad - deeper exploration of GIL
# https://realpython.com/intro-to-python-threading/ - long tutorial for Python 3.6 and up
# https://docs.python.org/2.7/library/threading.html - threading doc


import time, threading


"""
In C-Python (my implementation of Python), the GIL only allows a single thread can execute Python code at a time. That means threading is only useful
for simultaneous I/O bound tasks
"""


def print_numbers(limit, snooze, space):
    for x in range(limit):
        print(space + str(x))
        time.sleep(snooze)
        

def create_and_run_threads():
    """The threading interface is very similar to the multiprocessing interface (or should I say it's the other way around)."""
    t0 = threading.Thread(target=print_numbers, args=[10, 0.9, ""]) 
    t1 = threading.Thread(target=print_numbers, args=[7, 1, "   "])
    t0.start()
    t1.start()


def run_daemon_thread():
    """
    Python has a specific meaning for daemon threads that does not align with the concept of Unix thread
    - The main thread is never a daemon thread 
    - A thread can be set as a daemon thread with a Boolean, otherwise it will inherit the daemon status of the creating parent thread
    - The entire Python process shuts down when only daemon threads are remaining. Thus, if a thread is a daemon, the entire Python process can shut
      it down abruptly without properly disposing of resources
    - If a thread is not a daemon, the entire Python process must wait for the thread to finish
        - In the source, all sunch non-daemonic threads are join()-ed to the main thread
    """
    daemon = threading.Thread(target=print_numbers, args=[100, 1, ""])
    daemon.daemon = True
    daemon.start()


def run_and_join():
    """Whether or not a thread is a daemon, if it is joined then the entire Process will wait for it to finish before terminating"""
    daemon = threading.Thread(target=print_numbers, args=[10, 1, ""])
    daemon.daemon = True
    daemon.start()
    daemon.join()


if __name__ == "__main__":
    #create_and_run_threads()
    #run_daemon_thread() # This will only count up as long as the main thread is alive
    #run_and_join()
    print("main thread finished")