# https://stackoverflow.com/questions/10525185/python-threading-how-do-i-lock-a-thread
# https://stackoverflow.com/questions/3384385/python-3-2-gil-good-bad - deeper exploration of GIL
# http://www.dabeaz.com/python/GIL.pdf - actual presentation on GIL


import threading, multiprocessing, time


"""
The threading.Lock class returns a Python Lock object. There's nothing more complicated to it than that. From my standpoint as an application
programmer, there are no system calls or other configuration I need to know about. This is probably happening in the source code, but I don't need to
know about it.
"""


good_lock = threading.Lock()


def print_numbers(limit, snooze, space):
    """
    All threads that run this function are working with the same good_lock object. Threads must synchronize on the SAME lock object, not different
    ones!
    - If I forget to release the lock, it will block all other threads forever and any non-daemon threads will keep the process alive forever! Control
      + C cannot kill the process if this happens because 1) signal handlers can only run in the main thread 2) the main thread is blocked by an
        uninterruptable lock 3) since it's blocked, the main thread never gets scheduled to run any kind of signal handler 
    """
    #bad_lock = threading.Lock()
    good_lock.acquire()
    #bad_lock.acquire()
    for x in range(limit):
        print(space + str(x))
        time.sleep(snooze)
    good_lock.release()
    #bad_lock.release()

    10:46



def thread_acquire_lock():
    """
    The threads work with the lock object just fine, but the separate process appears to never run!
    - The separate process runs fine when there is no lock object at all
    - 
    """
    t0 = threading.Thread(target=print_numbers, args=[10, 0.7, ""])
    t1 = threading.Thread(target=print_numbers, args=[10, 0.5, "  "])
    p0 = multiprocessing.Process(target=print_numbers, args=[10, 0.2, "      "])
    t0.start()
    t1.start()
    p0.start()



if __name__ == "__main__":
    thread_acquire_lock()