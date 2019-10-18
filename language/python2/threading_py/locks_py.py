# https://stackoverflow.com/questions/10525185/python-threading-how-do-i-lock-a-thread
# https://stackoverflow.com/questions/3384385/python-3-2-gil-good-bad - deeper exploration of GIL
# http://www.dabeaz.com/python/GIL.pdf - actual presentation on GIL
# https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.2.0/com.ibm.zos.v2r2.bpxbd00/rtwaip.htm - explain waitpid()
# https://stackoverflow.com/questions/11295298/waiting-for-threads-of-another-process-using-waitpid - waitpid() example problem


import threading, multiprocessing, time, os, logging


"""
Thread locks:
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
    logging.warning('{}: about to acquire lock...'.format(threading.current_thread().name))
    good_lock.acquire()
    logging.warning('{}: got the lock!'.format(threading.current_thread().name))
    #bad_lock.acquire()
    for x in range(limit):
        logging.warning('{}: {}{}'.format(threading.current_thread().name, space, x))
        time.sleep(snooze)
    good_lock.release()
    logging.warning('{}: lock released!'.format(threading.current_thread().name))
    #bad_lock.release()


def thread_acquire_lock():
    """
    In POSIX systems (to which Linux and macOS are related), when a child process inherits from a parent process that has multiple currently executing
    threads, the child process only inherits from the thread that called fork(). 

    The threads in the parent process work with the lock just fine, but the child process forces the parent process to pause indefinitely. Why? I
    never explicitly joined the child process to the parent process, so why does the parent process wait? There is a clue in the stack trace. The
    parent process always appears to be paused on os.waitpid(). This system call "suspends the calling process until the system gets status
    information on the child."

    - The child process pauses indefinitely when:
        - The threads in the main process acquire the lock and don't join() to the parent process main thread
        - The threads in the parent process join() to the parent process main thread AFTER starting the child process
        - The threads in the main process don't run at all, but the main thread itself acquires and never releases the lock
    - The child process executes fine when:
        - The threads in the parent process don't acquire the lock
        - The threads in the parent process don't run at all
        - The parent main thread acquires the lock, but releases it at some arbitrary point in time
        - The threads in the parent process join() to the parent process main thread BEFORE starting the child process

    This leads me to believe that the child process inherits a lock object that is currently locked. Since the child process's thread lock is never
    released, the child process waits indefinitely.

    - Here's what must be happening. The child process gets a COPY of the parent process's address space. When the child gets its copy, it inherits a
      threading.Lock() object that is already locked. But wouldn't that mean it also inherited the executing threads from the parent process too?
    """
    logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'my-log.txt'), filemode='w', format='%(asctime)s: PID: %(process)s: %(message)s')
    logging.warning('started parent process')

    t0 = threading.Thread(target=print_numbers, args=[10, 0.5, ""])
    t1 = threading.Thread(target=print_numbers, args=[10, 0.2, "  "])
    #good_lock.acquire()
    p0 = multiprocessing.Process(target=print_numbers, args=[10, 0.1, "      "])
    #time.sleep(5)
    #good_lock.release()
    t0.start()
    t1.start()
    #t0.join()
    #t1.join()
    p0.start()
    #t0.join()
    #t1.join()


if __name__ == "__main__":
    thread_acquire_lock()