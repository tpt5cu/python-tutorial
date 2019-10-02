# https://docs.python.org/2.7/library/functions.html#bytearray
# https://stackoverflow.com/questions/9099145/where-are-python-bytearrays-used


"""
A bytearray is a mutable sequence of integers, each of which must in the range of [0, 255]. The contents of a bytearray can be treated as integers or
characters. Bytearrays are superior to the str type when the byte object is being modified. The str type is an immutable sequence of bytes while bytearray type
is a mutable sequence of bytes.
"""


def create_bytearray():
    """
    - If <source> is an iterable (like str), then each element of the iterable must be in the range of [0, 255].
    - If <source> is an integer, then the bytearray takes that size and initializes each element to a null byte
    """
    ba = bytearray('hello')
    print(len(ba)) # 5
    print(ba) # hello
    print(bin(ba[0])) # 0b1101000 = 104 decimal = h
    ba = bytearray(5)
    print(len(ba)) # 5
    print(ba)
    print(bin(ba[0])) # 0b0


if __name__ == '__main__':
    create_bytearray()