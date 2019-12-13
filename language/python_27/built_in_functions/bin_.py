# https://docs.python.org/2.7/library/functions.html#bin
# https://stackoverflow.com/questions/34300336/negative-numbers-to-binary-system-with-python
# https://stackoverflow.com/questions/9829578/fast-way-of-counting-non-zero-bits-in-positive-integer


'''
- Unfortunately, the immutable str type is no good for any bitwise operations
- Also, Python does not have built-in unsigned integers
'''


def examine_bin():
    '''
    bin() converts an int number (or an object that implements an __index__() method that returns an int) to a binary string. By 'binary string' it
    simply means in instance of the immutable str type
    '''
    val = bin(22)
    print(type(val)) # <type 'str'>
    print(val) # 0b10110
    val = val * 2
    print(val) # 0b101100b10110


def print_binary_representation():
    '''
    - Python works hard to represent positive numbers as infinitely extending to the left with zeros, and negative numbers as infinitely extending to
      the left with 1s. Therefore, it would be impossible to print the binary representation of -1, because it would fill up the whole screen and
      more. That's why -0b1 is printed instead
    '''
    print(bin(-1)) # -0b1
    simulated_word_size = -1 % 2**32 # This is 2^32 - 1, or '00000000 11111111 11111111 11111111 11111111', which is one less than 2^32, or '00000001 00000000 00000000 00000000 00000000'
    print(bin(simulated_word_size)) # 0b1111 1111 1111 1111 1111 1111 1111 1111
    print(bin(simulated_word_size).count('1')) # 32
    print(bin(simulated_word_size) == bin(2**32 - 1)) # True


if __name__ == '__main__':
    #examine_bin()
    print_binary_representation()