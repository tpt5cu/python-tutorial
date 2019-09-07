# https://stackoverflow.com/questions/641420/how-should-i-log-while-using-multiprocessing-in-python - The 'logging' module


import fcntl, os, time, multiprocessing, logging
from contextlib import contextmanager


"""
- The 'logging' module does not use process-shared locks. In other words, using the locks provided in that module will only lock threads within that
  process. It will not lock with other processes.
"""


logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), "my-log.txt"), filemode='w', format="%(asctime)s %(message)s")
filepath = os.path.join(os.path.dirname(__file__), 'test.txt')


@contextmanager
def locked_open(filepath, mode='r'):
    """The file object MUST be unlocked before it is closed. This is not optional and makes sense."""
    if mode in ['r', 'rb']:
        lock_mode = fcntl.LOCK_SH
    elif mode in ['r+', 'r+b', 'w', 'wb', 'w+', 'w+b', 'a', 'ab', 'a+', 'a+b']:
        lock_mode = fcntl.LOCK_EX
    else:
        raise Exception("Unrecognized file access mode")
    f = open(filepath, mode)
    fcntl.flock(f, lock_mode)
    yield f
    fcntl.flock(f, fcntl.LOCK_UN)
    f.close()
    #fcntl.flock(f, fcntl.LOCK_UN) # ValueError


def prepare_file():
    logging.warning("hello from prepare_file()")
    with locked_open(filepath, 'w') as f:
        f.write("Prepared the file!")


def read_and_log_file():
    logging.warning("hello from read_and_log_file()")
    with locked_open(filepath) as f:
        data = f.read()
    logging.warning("hello from read_and_log_file(), read data:\n" + data)


def write_file():
    logging.warning("hello from write_file()")
    with locked_open(filepath, 'w') as f:
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