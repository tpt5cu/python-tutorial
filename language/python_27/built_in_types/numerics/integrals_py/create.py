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
    print(0b1001) # 9
    print(0B1001) # 9
    print(0x9) # 9
    print(0X9) # 9
    print(0o11) # 9
    print(0O11) # 9
    print(9L) # 9 # SyntaxError in Python 3
    print(0600) # 8^2 * 6 = 384, SyntaxError in Python 3


if __name__ == "__main__":
    #long_integer()
    #different_base()
    literal_representations()