# https://docs.python.org/2/library/io.html
# https://pythontips.com/2014/01/15/the-open-function-explained/ - usefulness of the io.open encoding parameter


import io, codecs, fcntl, os, time


def io_open_identity():
    """
    io.open is identical to open is False for Python 2, but True for Python 3 as expected.
    - In Python 3, both file objects are instances of <class '_io.TextIOWrapper'>
    """
    print(io.open is open)
    with open(os.path.join(os.path.dirname(__file__), 'test.txt'), 'w') as f:
        print(type(f)) # <type 'file'>
    with io.open('test.txt', 'w') as f:
        print(type(f)) # <type '_io.TextIOWrapper'>


def codecs_open_identity():
    """There is another open function in the codecs package. codecs.open is not the same as io.open or open in Python 2 or 3"""
    print(codecs.open is io.open) # False
    print(codecs.open is open) # False


def io_open_locking():
    """
    The standard open() function and io.open() function can both be locked with fcntl.flock (or another lock type). fcntl operates on a file
    descriptor (an integer) or an object that implements a fileno() method. Both the Python <type 'file'> and <type '_io.TextIOWrapper'> implement a
    fileno() method 
    """
    filepath = os.path.join(os.path.dirname(__file__), 'test.txt')
    with io.open(filepath, 'w', encoding='utf8') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(unicode('hello from io_open_locking()'))
        fcntl.flock(f, fcntl.LOCK_UN)


if __name__ == "__main__":
    #io_open_identity()
    #codecs_open_identity()
    io_open_locking()