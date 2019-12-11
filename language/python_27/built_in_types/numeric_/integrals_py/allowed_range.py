# https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
# https://mortada.net/can-integer-operations-overflow-in-python.html 


import sys


"""
The plain int type is unbounded in Python 3, since in Python 3 an int is still named 'int' but it is really a long. In Python, the range of a numeric
value is only limited by the amount of memory on my machine, not by the word size of 64 bits. Therefore, integers cannot overflow/underflow in pure
Python because Python integers have arbitrary precision.
- This is not true with numpy/pandas because they use C stuff
"""


def show_max_int():
    """sys.maxint is the maximum value for a 64-bit integer."""
    x = sys.maxint
    print(x) # 9223372036854775807
    print(type(x)) # <type 'int'>
    print(x == 2**63 - 1) # True


def show_max_int_plus_one():
    """Python switches from ints to long after sys.maxint has been exceeded."""
    x = sys.maxint + 1
    print(x) # 9223372036854775808
    print(type(x)) # <type 'long'>


def show_max_value():
    x = sys.maxsize
    print(x)
    print(type(x))


if __name__ == "__main__":
    #show_max_int()
    #show_max_int_plus_one()
    show_max_value()