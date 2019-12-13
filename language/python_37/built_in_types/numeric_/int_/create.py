import sys


def int_to_long():
    '''The int class is unbounded in Python 3'''
    #print(sys.maxint) # AttributeError
    old_max_int = 9223372036854775807
    print(type(old_max_int)) # <class 'int'>
    just_another_int = 9223372036854775808
    print(type(just_another_int)) # <class 'int'>
    old_min_int = -9223372036854775808
    print(type(old_min_int)) # <class 'int'>
    just_another_int = old_min_int - 1
    print(type(just_another_int)) # <class 'int'>


def literal_representations():
    '''
    - "L" suffix for explicit long literals is removed
    - "0" prefix for explicit octal literals is removed
    '''
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
    #y = 9L # SyntaxError
    #print(0600) # SyntaxError

if __name__ == '__main__':
    #int_to_long()
    literal_representations()