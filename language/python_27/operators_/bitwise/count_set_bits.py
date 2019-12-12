# https://stackoverflow.com/questions/9829578/fast-way-of-counting-non-zero-bits-in-positive-integer


"""I have not resolved the issue of negative numbers in Python"""


def introduction(num):
    """
    This needs to work with negative numbers. 
    - bin(-1) = -0b1
    - ~-1 = 0
    - bin(~-1) = 0
    - 0 ^ 1 = 1
    """
    # Simulate a word size. If I don't negative numbers don't work well with this function
    num %= 2**32
    #print(num)
    #print(bin(num))
    #print('set_bits: {}'.format(bin(num).count('1')))
    set_bits = 0
    while num != 0:
        num = num & num
        if num > 0:
            set_bits += 1
        num -= 1
    return set_bits


def examine_negative_one():
    print(bin(-1)) # -0b1
    print(bin(1)) # 0b1
    print(-1 & 1) # 1 because all the 0s of 1 cancel out all of the 1s of -1


def easy_count_set_bits(num):
    """
    This is the easiest and one of the fastest ways to count the number of set bits for positive integers. Since Python has infinite precision for
    signed integers, it's difficult to actually count the number of set bits for a negative number
    - It presents a problem when trying to use a bit vector to count the number of set bits. If I use this method, I'll have to generate a new
      immutable str object every time I want to count the number of set bits in a bit vector (i.e. an integer)
    - It just doesn't work for negative numbers, period
    """
    print('Counted {} set bits'.format(bin(num).count('1')))


def example_count_set_bits(value):
    """This does not work with negative numbers. It runs forever"""
    n = 0
    while value:
        n += 1
        value &= value-1
    return n

    
if __name__ == '__main__':
    #examine_negative_one()
    #easy_count_set_bits(6003) # 9
    #easy_count_set_bits(-1) # 1 wrong!
    #print(example_count_set_bits(6003)) # 9
    #print(example_count_set_bits(-1))