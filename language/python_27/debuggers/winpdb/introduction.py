import time
from multiprocessing import Process


"""
bp <number>: set a breakpoint
bl: list breakpoints
bc <number>: clear the breakpoint
go: continue execution
l: list source code (alias for 'list')

Unfortunately, this hasn't been the simple fix I was hoping for multiprocessing code
"""


def spawn_process():
    p = Process(target=print_numbers)
    p.start()
    p.join()


def print_numbers():

    for i in range(10):
        i += 1
        print(i)
        time.sleep(0.5)


if __name__ == "__main__":
    spawn_process()