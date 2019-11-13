# https://docs.python.org/2/library/functions.html#format


"""format(<value>, <format_spec>) is syntactic sugar for <value>.__format__(<format_spec>)."""


def hex_int():
    print(format(16, "X")) # 10
    # This is invalid
    #16.__format__("X")
    print(format(15, "X")) # F
    print(format(14, "X")) # E


def get_type():
    """The format() build-in function returns a string, regardless of the original data type."""
    f = 1.987654321
    x = format(f, ".3")
    print(x) # 1.99
    print(type(x)) # <type 'str'>


def specify_precision():
    """Using format() returns a string, so it is not the same as using the round() build-in function."""
    f = 1.987654321
    print(format(f, ".0")) # 2e+00
    print(format(f, ".1")) # 2e+00
    print(format(f, ".2")) # 2.0
    print(format(f, ".3")) # 1.99
    x = round(f, 2)
    print(format(f, ".3") == x) # False


if __name__ == "__main__":
    hex_int()
    #get_type()
    #specify_precision()