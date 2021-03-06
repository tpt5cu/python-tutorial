import sys

"""The underlying type of all integral types (regardless of base) is int."""


def integer_precision():
    """The largest practical integer value is equal to the sys.maxsize variable.
    Using a value greater than sys.maxsize may result in an OverflowError depending on usage.
    """
    print("sys.maxsize equals 2^63 - 1 on 64-bit platforms: " + str(sys.maxsize))

    """However, integers have unlimited precision in Python (Precision is limited by the available memory)."""
    big_num = 1000**1000
    print("big_num: " + str(big_num))
    print("big_num type: " + str(type(big_num)))


def different_bases():
    binary = 0b10001
    print(binary)
    octal = 0o21
    print(octal)
    hexadecimal = 0x11
    print(hexadecimal)


if __name__ == "__main__":
    # integer_precision()
    different_bases()
