"""
https://stackoverflow.com/questions/489861/locking-a-file-in-python - Overview of locking in Python
http://tilde.town/~cristo/file-locking-in-python.html - If two processes try to acquire an exclusive lock on the same file, an error CAN be thrown if
I want
https://stackoverflow.com/questions/11853551/python-multiple-users-append-to-the-same-file-at-the-same-time
http://0pointer.de/blog/projects/locking.html - I don't know how much of the content of this article is wrong
"""

"""
Linux primarily supports "advisory" locks. If some process, A, is not aware that another process, B, has a lock on a file, then A will ignore B's
lock. The kernal does not enforce locks, but application-level code can choose to coordinate and obey locks.
- In other words, unless a process checks for a lock, it will ignore any existing locks.
- A lock is bound to a process, not to a file descriptor.
    - This is only a problem if threads within the same process need to synchronize on a file descriptor (they can't)
- If a process exits or terminates, any locks that it had are released.
    - If any thread inside of the process calls "close" on a file descriptor, the lock is released for the entire process (and hence all other
    threads)

Mandatory locks are not reliably implemented in Linux.
"""


import fcntl, os, time, errno
from multiprocessing import Process


def write_Q_character():
    with open(os.path.join(os.path.dirname(__file__), "input1.txt")) as f1:
        with open(os.path.join(os.path.dirname(__file__), "bad.txt"), 'a') as f2:
            for line in f1:
                f2.write(line)
                time.sleep(.0001)


def write_Z_character():
    with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f1:
        with open(os.path.join(os.path.dirname(__file__), "bad.txt"), 'a') as f2:
            for line in f1:
                f2.write(line)
                time.sleep(.0003)


def write_T_character():
    with open(os.path.join(os.path.dirname(__file__), "input3.txt")) as f1:
        with open(os.path.join(os.path.dirname(__file__), "good.txt"), 'a') as f2:
            while True:
                try:
                    fcntl.flock(f2, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    for line in f1:
                        f2.write(line)
                    fcntl.flock(f2, fcntl.LOCK_UN)
                    break
                except IOError as e:
                    if e.errno != errno.EACCES and e.errno != errno.EAGAIN:
                        raise
                    print("T write is waiting...")


def write_O_character():
    with open(os.path.join(os.path.dirname(__file__), "input4.txt")) as f1:
        with open(os.path.join(os.path.dirname(__file__), "good.txt"), 'a') as f2:
            while True:
                try:
                    fcntl.flock(f2, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    for line in f1:
                        f2.write(line)
                    fcntl.flock(f2, fcntl.LOCK_UN)
                    break
                except IOError as e:
                    if e.errno != errno.EACCES and e.errno != errno.EAGAIN:
                        raise
                    print("O write is waiting...")


def no_lock_write():
    """
    Neither process does any locking nor checks for a lock, so the writing operations alternate back and forth as evidenced by a mix of "Z" lines and
    "Q" lines.
    """
    my_path = os.path.join(os.path.dirname(__file__), "bad.txt")
    if os.path.exists(my_path):
        os.remove(my_path)
    p1 = Process(target=write_Q_character)
    p2 = Process(target=write_Z_character)
    p1.start()
    p2.start()


def lock_write():
    """
    Both processes try to acquire exclusive locks. It works as evidenced by completely separate blocks of T's and O's.
    - If I don't do LOCK_EX | LOCK_NB, then the first exclusive lock will silently block the second exclusive lock. When the first exclusive lock is
      released, the other process can acquire the second exclusive lock and code will proceed as normal.
    - If I do LOCK_EX | LOCK_NB, the second exclusive lock will throw an IOError when it is blocked by the first exclusive lock. I can recover from
      the error however I want. I like this approach better because silent errors are bad.
    """
    my_path = os.path.join(os.path.dirname(__file__), "good.txt")
    if os.path.exists(my_path):
        os.remove(my_path)
    p1 = Process(target=write_T_character)
    p2 = Process(target=write_O_character)
    p2.start()
    p1.start()


if __name__ == "__main__":
    #no_lock_write()
    lock_write()