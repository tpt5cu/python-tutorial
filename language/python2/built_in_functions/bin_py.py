# https://docs.python.org/2.7/library/functions.html#bin
# https://stackoverflow.com/questions/34300336/negative-numbers-to-binary-system-with-python


"""Unfortunately, the immutable str type is no good for any bitwise operations"""


def examine_bin():
    """
    bin() converts an int number (or an object that implements an __index__() method that returns an int) to a binary string. By "binary string" it
    simply means in instance of the immutable str type
    """
    val = bin(22)
    print(type(val)) # <type 'str'>
    print(val) # 0b10110
    val = val * 2
    print(val) # 0b101100b10110


def print_binary_representation():
    """
    - Python works hard to represent positive numbers as infinitely extending to the left with zeros, and negative numbers as infinitely extending to
      the left with 1s. Therefore, it would be impossible to print the binary representation of -1, because it would fill up the whole screen and
      more. That's why -0b1 is printed instead
    - 
    """
    print(bin(-1)) # -0b1
    simulated_word_size = -1 % 2**32
    print(bin(simulated_word_size))
    print(bin(simulated_word_size).count('1')) # 32



def count_set_bits(num):
    """
    This needs to work with negative numbers. 
    """
    neg = False
    if num < 0:
        num = ~num
        neg = True
    print(num)
    print(bin(num))
    print('set_bits: {}'.format(bin(num).count('1')))
    set_bits = 0
    while num != 0:
        if neg:
            set_bits += num ^ 1
        else:
            set_bits += num & 1
        num >>= 1
    return set_bits



if __name__ == '__main__':
    #examine_bin()
    print_binary_representation()
    #print('Counted {} set bits'.format(count_set_bits(6003))) # 9
    #print('Counted {} set bits'.format(count_set_bits(-1)))