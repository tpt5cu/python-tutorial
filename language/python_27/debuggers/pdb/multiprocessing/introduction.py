# https://stackoverflow.com/questions/4716533/how-to-attach-debugger-to-a-python-subproccess
# https://stackoverflow.com/questions/34914704/bdbquit-raised-when-debugging-python


import time
from multiprocessing import Process


'''
These notes are useful because they show that using regular pdb won't work in the OMF Flask architecture. Almost everything that I want to debug is in
a background process, and on macOS pdb.set_trace() doesn't work in a forked multiprocessing child.
- In the Flask background process, a job will have appeared to fail, but in reality it was just that BdbQuit was raised

- rpdb2 is useless too because I can't figure out how to inspect variables
'''


def spawn_process():
    #import pdb; pdb.set_trace()
    p = Process(target=print_numbers)
    p.start()
    p.join()


def print_numbers():
    # This line raise BdbQuit
    #import pdb; pdb.set_trace()
    # This works
    #ForkedPdb().set_trace()
    for i in range(10):
        i += 1
        print(i)
        time.sleep(0.5)


import sys
import pdb


# This works! I don't know why
class ForkedPdb(pdb.Pdb):
    """A Pdb subclass that may be used from a forked multiprocessing child"""
    def interaction(self, *args, **kwargs):
        _stdin = sys.stdin
        try:
            sys.stdin = open('/dev/stdin')
            pdb.Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = _stdin


if __name__ == "__main__":
    spawn_process()