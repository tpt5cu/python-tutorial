# https://stackoverflow.com/questions/11837428/whats-the-difference-between-an-exclusive-lock-and-a-shared-lock


import fcntl, os, time, errno
from multiprocessing import Process


"""
Exclusvie locks are only for writing.
- Only one exclusive lock can exist on a file object at a time. Thus, only one process can write to a file at a time.
- If a process has an exclusive lock, no other exclusive locks may be created and no other shared locks can be created. 

Shared locks are only for reading.
- More than one shared lock can be held on a file, but while a shared lock is held, no exclusive lock can be held on the file.
- Multiple processes can each have a shared lock on a file
"""


def read_file():
    """ The number of read lines is inconsistent because no locks are used """
    with open(os.path.join(os.path.dirname(__file__), "output.txt")) as f:
        lines = 0
        time.sleep(.5)
        for line in f:
            lines += 1
    # Counts 391 lines or 196 lines
    print("Counted lines: " + str(lines))


def write_file():
    with open(os.path.join(os.path.dirname(__file__), "output.txt"), 'w') as f:
        for x in range(1000):
            f.write("1,2,3,4,5,6,7,8,9,10\n")
            time.sleep(.001)


def no_lock():
    p1 = Process(target=read_file)
    p2 = Process(target=write_file)
    p2.start() # write
    p1.start() # read
    # Join because I want to empty the file after these processes both complete
    p1.join()
    p2.join()


def good_read_file():
    """
    This is how to properly acquire shared lock before reading. Try commenting out the lock lines to make this function bad like the first one
    """
    with open(os.path.join(os.path.dirname(__file__), "output.txt")) as f:
        fcntl.flock(f, fcntl.LOCK_SH)
        lines = 0
        time.sleep(.5)
        for line in f:
            lines += 1
        fcntl.flock(f, fcntl.LOCK_UN)
    # Always counts 1000 lines
    print("Counted lines: " + str(lines))


def good_read_file_alternative():
    """
    This is how to properly acquire shared lock before reading. Try commenting out the lock lines to make this function bad like the first one
    """
    with open(os.path.join(os.path.dirname(__file__), "output.txt")) as f:
        start = time.time()
        while True:
            # This will throw an IOError 
            try:
                fcntl.flock(f, fcntl.LOCK_SH | fcntl.LOCK_NB)
                lines = 0
                time.sleep(.5)
                for line in f:
                    lines += 1
                fcntl.flock(f, fcntl.LOCK_UN)
                # Always counts 1000 lines
                print("Counted lines: " + str(lines))
                break
            except IOError as e:
                if e.errno == errno.EAGAIN:
                    pass
                print("Waiting to acquire shared lock...")
                if time.time() > start + 1:
                    print("Lock timeout!")
                    break

def good_write_file():
    with open(os.path.join(os.path.dirname(__file__), "output.txt"), 'w') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        for x in range(1000):
            f.write("1,2,3,4,5,6,7,8,9,10\n")
            time.sleep(.001)
        fcntl.flock(f, fcntl.LOCK_UN)


def lock():
    #p1 = Process(target=good_read_file)
    p1 = Process(target=good_read_file_alternative)
    p2 = Process(target=good_write_file)
    p2.start() # Write
    p1.start() # Read
    # Join because I want to empty the file after these processes both complete
    p2.join()
    p1.join()


def empty_file():
    with open(os.path.join(os.path.dirname(__file__), "output.txt"), 'w') as f:
        f.write("")

if __name__ == "__main__":
    #no_lock()
    lock()
    empty_file() # Make the file empty after each operation