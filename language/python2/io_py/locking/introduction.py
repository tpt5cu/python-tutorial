# https://stackoverflow.com/questions/641420/how-should-i-log-while-using-multiprocessing-in-python - The 'logging' module
# https://docs.python.org/2/library/fcntl.html#fcntl.lockf - LOCK_NB and os error codes
# https://docs.python.org/2/library/errno.html - yes, errno is its own module!
# https://stackoverflow.com/questions/8392640/how-to-implement-a-lock-with-a-timeout-in-python-2-7 - great example of lock with timeout
# https://stackoverflow.com/questions/2654113/how-to-get-the-callers-method-name-in-the-called-method - get caller function name


import fcntl, os, time, multiprocessing, logging, errno, inspect
from contextlib import contextmanager


"""
The 'logging' module does not use process-shared locks. In other words, using the locks provided in that module will only lock threads within that
process. It will not lock with other processes.
"""


logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), "my-log.txt"), filemode='w', format="%(asctime)s %(message)s")
filepath = os.path.join(os.path.dirname(__file__), 'test.txt')


# This is the original context manager. The other one is stripped down
@contextmanager
#def locked_open(filepath, mode='r', timeout=30):
def debug_locked_open(filepath, mode='r', timeout=30):
    """
    It's really cool how often different process will get the lock first. The results of the locking are not consistent.
    - The file object MUST be unlocked before it is closed. This is not optional and makes sense.
        - That is to say that it is an error to unlock a closed file object
    - It is not an error to unlock a file that was never locked
    - A blocking lock will raise an IOError with a specific errno of either EAGAIN or EACCES depending on the operating system. For mac, the errno is
      EAGAIN, not EACCES
    - I put a timeout just in case someone misuses this context manager because without a timeout this could block forever
        - I could make the context mananger accept the timeout as an argument
    """
    if mode in ['r', 'rb']:
        lock_mode = fcntl.LOCK_SH
    elif mode in ['r+', 'r+b', 'w', 'wb', 'w+', 'w+b', 'a', 'ab', 'a+', 'a+b']:
        lock_mode = fcntl.LOCK_EX
    else:
        raise Exception("Unrecognized file access mode")
    f = open(filepath, mode)
    ### Debugging introspection
    current_frame = inspect.currentframe() # current frame object
    outer_frames = inspect.getouterframes(current_frame) # list of tuples, each tuple contains a frame object and some other stuff
    caller_name = outer_frames[2][3] # get a tuple, then get the invoking function name associated with the frame object
    message = caller_name + ". "
    #import pdb; pdb.set_trace()
    start_time = time.time()
    while True:
        logging.warning(message + "Trying to acquire lock...")
        try:
            fcntl.flock(f, lock_mode | fcntl.LOCK_NB)
            logging.warning(message + "Got the lock!")
            break
        except IOError as e:
            if e.errno != errno.EACCES and e.errno != errno.EAGAIN:
                raise
        if time.time() >= start_time + timeout:
            raise IOError("File lock {timeout}-second timeout reached. Either a file-locking operation is taking more than {timeout} seconds "
                "or there was a programmer error that would have resulted in permanent lock-blocking.".format(timeout=timeout))
        time.sleep(0.1) # sleep to reduce log output
    # Don't yield the file object until it has been locked!
    yield f
    fcntl.flock(f, fcntl.LOCK_UN)
    f.close() 


@contextmanager
def locked_open(filepath, mode='r', timeout=30):
    if mode in ['r', 'rb']:
        lock_mode = fcntl.LOCK_SH
    elif mode in ['r+', 'r+b', 'w', 'wb', 'w+', 'w+b', 'a', 'ab', 'a+', 'a+b']:
        lock_mode = fcntl.LOCK_EX
    else:
        raise Exception("Unrecognized file access mode")
    f = open(filepath, mode)
    start_time = time.time()
    while True:
        try:
            fcntl.flock(f, lock_mode | fcntl.LOCK_NB)
            break
        except IOError as e:
            if e.errno != errno.EACCES and e.errno != errno.EAGAIN:
                raise
        if time.time() >= start_time + timeout:
            raise IOError("File lock {timeout}-second timeout reached. Either a file-locking operation is taking more than {timeout} seconds "
                "or there was a programmer error that would have resulted in permanent lock-blocking.".format(timeout=timeout))
    yield f
    fcntl.flock(f, fcntl.LOCK_UN)
    f.close() 


def prepare_file():
    logging.warning("hello from prepare_file()")
    with locked_open(filepath, 'w') as f:
        f.write("Prepared the file!")


def read_and_log_file():
    logging.warning("hello from read_and_log_file()")
    with locked_open(filepath, timeout=5) as f:
    #with locked_open("blahblah.txt", timeout=5) as f: # raise a regular IOError
        data = f.read()
    logging.warning("hello from read_and_log_file(), read data:\n" + data)


def write_file():
    logging.warning("hello from write_file()")
    with locked_open(filepath, 'w') as f:
        #time.sleep(7) # Trigger an error in the read_and_log_file() processes
        for x in range(10):
            f.write("Line: " + str(x) + "\n")
            time.sleep(0.4)


def test():
    for mode in ['r+', 'r+b', 'w', 'wb', 'w+', 'w+b', 'a', 'ab', 'a+', 'a+b']: 
        with locked_open(filepath, mode) as f:
            f.truncate()
            f.write(mode + ": I wrote some new content\n")
        print("mode: " + mode)


def multiprocessing_test():
    """
    Locking appears to work just fine. Disabling the locks works as expected too.
    """
    prepare_file()
    p0 = multiprocessing.Process(target=read_and_log_file)
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_and_log_file)
    p0.start()
    # This sleep completely changes the log output!
    #time.sleep(1)
    p1.start()
    p2.start()
    

if __name__ == "__main__":
    #read_and_log_file()
    #test()
    multiprocessing_test()