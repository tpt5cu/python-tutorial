# https://docs.python.org/2.7/reference/lexical_analysis.html#integer-and-long-integer-literals - different numeric literals
# https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex - long integers
# https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints


import sys


def int_to_long():
    '''
    After an integer exceeds a system-dependent value, the integer becomes a long instead of an int
    - 2^63 - 1 = 9223372036854775807
    - The size of a long is only constrained by memory
    '''
    print(sys.maxint) # 9223372036854775807
    max_int = 9223372036854775807
    print(type(max_int)) # <type 'int'>
    first_pos_long = 9223372036854775808
    print(type(first_pos_long)) # <type 'long'>
    min_int = -sys.maxint - 1
    print(type(min_int)) # <type 'int'>
    print(min_int) # -9223372036854775808
    first_neg_long = min_int - 1
    print(type(first_neg_long)) # <type 'long'>
    print(first_neg_long) # -9223372036854775809


def different_base():
    # Create a base-28 number. "r" in base-28 is 27
    print(int("r", 28)) # 27
    # Create a base-28 number. (27 * 28) + 27 = 783
    print(int("rr", 28)) # 783


def literal_representations():
    # Binary
    print(0b1001) # 9
    print(0B1001) # 9
    # Hex
    print(0x9) # 9
    print(0X9) # 9
    # Octal
    print(0o11) # 9
    x = 0O11
    print(x) # 9
    print(type(x)) # <type 'int'>
    y = 9L 
    print(y) # 9 
    print(type(y)) # <type 'long'>
    # '0' prefixed numbers are interpeted as base-8
    print(0600) # (8^2) * 6 = 384, SyntaxError in Python 3


if __name__ == "__main__":
    #int_to_long()
    #different_base()
    literal_representations()