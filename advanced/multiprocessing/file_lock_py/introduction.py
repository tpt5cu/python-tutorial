import fcntl, os, time, errno
from multiprocessing import Process


"""
https://gavv.github.io/articles/file-locks/ - Detailed summary of types of file locks
https://stackoverflow.com/questions/9907616/python-fcntl-does-not-lock-as-expected - Describes confusing behavior for a user that doesn't understand locks
https://docs.python.org/2.7/library/fcntl.html#fcntl.flock
https://stackoverflow.com/questions/5507185/what-does-lock-nb-mean-in-flock
"""


"""
fcntl.fcntl and fcntl.flock don't return lock objects (they don't return anything, so they return None), so don't bothering assigning variables to
invocations of these functions

LOCK_NB means "non-blocking" lock. Thus, if a process tries to get a lock, but it can't, then this flag makes the process continue instead of waiting
to acquire the lock. In Python, an exception will be thrown if the process can't instantly get the lock.
"""


my_path = os.path.join(os.path.dirname(__file__), "output.txt")


def shared_exclusive_lock():
    """
    This code uses a flock-type lock on the same file descriptor. At the system level, flock ensures that duplicated (or the same) file descriptors in
    the SAME process SHARE the lock acquisition. That's why no blocking occurs.
    """
    with open(my_path, 'w') as f: # There is only 1 file descriptor here
        fcntl.flock(f, fcntl.LOCK_EX)
        fcntl.flock(f, fcntl.LOCK_EX)
        foo = f.write("hi")


def deadlock():
    """
    If fcntl.flock is used, the function never completes. flock locks created on independent file descriptors in the same process do NOT share
    exclusive locks. The first lock is still in place when I try to acquire the second lock. The code will wait forever while it waits to acquire the
    second exclusive lock. THIS IS GOOD FOR FLASK WHICH IS MULTI-THREADED.

    If fcntl.fcntl is used, any file descriptors within the same process share an exclusive lock, so there is no deadlock. fcntl.lockf is identical to
    fcntl.fcntl in this regard, and very similar in other aspects.
    """
    with open(my_path, 'w') as f1:
        fcntl.flock(f1, fcntl.LOCK_EX)
        #fcntl.fcntl(f1, fcntl.LOCK_EX)
        f1.write("hello")
        print("first")
        with open(my_path, 'w') as f2:
            print("second")
            fcntl.flock(f2, fcntl.LOCK_EX)
            #fcntl.fcntl(f2, fcntl.LOCK_EX)
            f2.write("bye") # This never executes if fcntl.flock is the locking mechansim
            print("third") # This never prints if fcntl.flock is the locking mechanism


def hold_lock():
    f = open(my_path)
    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    start = time.time()
    while True:
        print("Lock 1 has a lock")
        time.sleep(1.0)
        if (time.time() > start + 10.0):
            fcntl.flock(f, fcntl.LOCK_UN)
            break


def bad_get_lock():
    """
    When this function executes in a separate process, it will silently be blocked while it tries to acquire an exclusive lock on the already-locked
    file descriptor.
    """
    f = open(my_path)
    while True:
        time.sleep(1.0)
        fcntl.flock(f, fcntl.LOCK_EX)
        print("Lock 2 has a lock") # Never prints


def good_get_lock():
    """
    When I do fcntl.LOCK_EX | fcntl.LOCK_NB, an IOError will be raised during an occurance of lock blocking. Without catching the error,
    the function will terminate with the exception and the process will terminate. I can adjust this behavior by 1) raising unrelated errors (in case
    something else happened) and 2) re-trying to acquire the lock after some time.
    """
    f = open(my_path)
    waiting = True
    while True:
        time.sleep(1.0)
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            waiting = False
            print("Lock 2 acquired the lock")
            break
        except IOError as e:
            # A blocking lock will raise an IOError with a specific errno of either EAGAIN or EACCES depending on the operating system. For mac, the
            # errno is EAGAIN, not EACCES
            if e.errno != errno.EAGAIN and e.errno != errno.EACCES:
                raise
            print("Detected lock blocking")
        if waiting:
            print("Lock 2 waiting for lock")


def blocking_lock():
    """
    If 1 process has an exclusive lock and another process is trying to get an exclusive lock on the same file, the first process will silently block
    the second process from acquiring the lock. Only if fcntl.LOCK_NB is OR-d with fcntl.LOCK_EX or fcntl.LOCK_SH will an IOError be raised if
    blocking happens.
    """
    p1 = Process(target=hold_lock)
    #p2 = Process(target=bad_get_lock) # Silently blocks
    p2 = Process(target=good_get_lock) # Throws an exception upon lock detection
    p1.start()
    p2.start()


if __name__ == "__main__":
    #shared_exclusive_lock()
    #deadlock()
    #what()
    blocking_lock()