# https://docs.python.org/2.7/library/functions.html#bytearray
# https://stackoverflow.com/questions/9099145/where-are-python-bytearrays-used


"""
A bytearray is a mutable sequence of integers, each of which must in the range of [0, 255]. The contents of a bytearray can be treated as integers or
characters. Bytearrays are superior to the str type when the byte object is being modified. The str type is an immutable sequence of bytes while bytearray type
is a mutable sequence of bytes.
- bytearray is THE mutable string type in Python
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


def bad_bit_vector():
    """
    Remember: passing an integer to a bytearray merely creates a bytearray with all 0 values of that size
    - A bytearray will include the '0b' if a bin() call is used to instantiate the bytearray
    - A bytearray contains bytes! Therefore, I only need a bytearray of 1 byte!
    """
    #ba = bytearray(2**16 - 1) # wrong
    # Wrong because I don't want to include 0b
    ba = bytearray(bin(2**16 - 1))
    print(ba) # 0b1111111111111111
    print(len(ba)) # 18
    print(ba[0]) # 48 because the ascii value of 0 is 48
    print(ba[1]) # 98 because the ascii value of b is 98
    # Wrong because this is 8 bytes, where each byte is the character '1'
    ba = bytearray('11111111')
    print(ba) # 11111111
    print(len(ba)) # 8
    print(ba[0]) # 49


def good_bit_vector():
    """
    - Do I even need a bytearray to implement a bit vector? No, I just need the value 255. But how do I count how many bits are set in an integer?
    - XOR ^ is equivalent to subtraction
    """
    ba = bytearray(chr(255))
    print(int(ba[0])) # 255
    print(ba[0] ^ 5) # 250 because 11111111 ^ 00000101 = 11111010 = 250
    print(255 ^ 5) # 250


def print_bytearray():
    """A bytearray prints just fine"""
    s = "hi there"
    ba = bytearray(s)
    print(ba)


if __name__ == '__main__':
    #create_bytearray()
    #bad_bit_vector()
    #good_bit_vector()
    print_bytearray()