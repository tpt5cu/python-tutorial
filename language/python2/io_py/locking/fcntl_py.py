# -*- coding: UTF-8 -*-

# https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/flock.2.html - macOS flock API
# https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html - macOS fcntl API
# https://stackoverflow.com/questions/9907616/python-fcntl-does-not-lock-as-expected - somebody at least providing an example of using fcntl.fcntl


import fcntl, os, io, time
from multiprocessing import Process


def use_fcntl():
    """
    BSD fcntl.flock() locks work fine on macOS and Linux. However, I'm having some trouble with fcntl.fcntl() locks on mac OS because it looks like the
    system call API is slightly different for flock vs fcntl on macOS. I actually cannot even get fcntl.fcntl() to lock correctly, so I can't use it
    for now.

    fcntl.fcntl possible operation values on macOS
    - F_RDLCK: shared lock
    - F_WRLCK: exclusive lock
    - F_UNLCK: unlock
    """
    filepath = os.path.join(os.path.dirname(__file__), 'test.txt')
    with open(filepath, 'w') as f:
        fcntl.fcntl(f, fcntl.F_WRLCK) # No errors, and the macOS manual mentions this, so I think it's right
        #fcntl.fcntl(f, fcntl.LOCK_EX) # No errors, but is this correct?
        f.write("hello from use_fcntl()")
        fcntl.fcntl(f, fcntl.F_UNLCK) 
        #fcntl.fcntl(f, fcntl.LOCK_UN) # IOError [Errno 14] Bad address
    with open(filepath) as f:
        fcntl.fcntl(f, fcntl.F_RDLCK)
        #fcntl.fcntl(f, fcntl.LOCK_SH) # No errors, but is this correct?
        data = f.read()
        fcntl.fcntl(f, fcntl.F_UNLCK)
        #fcntl.fcntl(f, fcntl.LOCK_UN) # IOError [Errno 14] Bad address
    print('Data was: ' + data)


def write_with_fcntl(sleep_time):
    """I haven't been able to get fcntl.fcntl() to work at all!"""
    filepath = os.path.join(os.path.dirname(__file__), 'test.txt')
    # This string is encoded in utf8. This is only needed in Python 2, in Python 3 unicode() is undefined
    string = unicode('hello from io_open_locking()😀', 'utf8') # Python 2
    #string = 'hello from io_open_locking()😀' # Python 3
    with io.open(filepath, 'a', buffering=1, encoding='utf8') as f:
        #fcntl.flock(f, fcntl.LOCK_EX)
        fcntl.fcntl(f, fcntl.F_WRLCK)
        for _ in range(0, 10):
            f.write(string + unicode('sleep_time: {}\n'.format(sleep_time)))
            time.sleep(sleep_time)
        #fcntl.flock(f, fcntl.LOCK_UN)
        fcntl.fcntl(f, fcntl.F_UNLCK)
    # This data will be decoded in this weird encoding that is not utf8, so the data that I'm reading looks different from what I wrote because it was
    # decoded incorrectly
    with io.open(filepath, 'r', encoding='csptcp154') as f: 
        fcntl.flock(f, fcntl.F_RDLCK)
        data = f.read()
        fcntl.flock(f, fcntl.F_UNLCK)
    print(data)


def spawn_fcntl_processes():
    """
    In order to test the effectiveness of the fcntl.fcntl() locks, io.open()'s bufferring must be switched from the default mode (block-sized
    bufferring), because I presume that the supposedly competing process writes are somehow ordered by the bufferring.
    - line bufferring (bufferring=1) seems to do the trick of garbling the output because once a line is written the buffer is flushed
    - The output is STILL garbled when the fcntl.fcntl() locks are enabled! Why?  
    - fcntl.flock() works fine. The output is always nicely ordered. Why doesn't fcntl.fcntl() work?
    """
    filepath = os.path.join(os.path.dirname(__file__), 'test.txt')    
    with open(filepath, 'w'):
        pass
    p1 = Process(target=write_with_fcntl, args=(.2,))
    p2 = Process(target=write_with_fcntl, args=(.5,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    #use_fcntl()
    spawn_fcntl_processes()