# https://docs.python.org/2.7/reference/lexical_analysis.html#integer-and-long-integer-literals - different numeric literals
# https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex - long integers


def long_integer():
    """Long integers have unlimited precision"""
    val = 9999999999999999999999999999999 ** 99
    print(val)
    print("")
    print(bin(val))


def different_base():
    print(int("r", 28)) # Create a base-28 number. "r" in base-28 is 27
    print(int("rr", 28)) # Create a base-28 number. (27 * 28) + 27 = 783


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
    #long_integer()
    #different_base()
    literal_representations()