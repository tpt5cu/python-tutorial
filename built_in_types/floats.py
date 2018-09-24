def float_precision():
    """The maximum floating point value is just under 1.08e308, which is 64-bit double precision.
    Any floating point value greater than that is represented by the string 'inf'."""
    print(1.79e308)
    print(1.8e308)
    print(1.79e309)
    """The smallest positive floating point value is about 5.0e-324. Anything less is 0."""
    print(5.0e-324)
    print(5.0e-325)
    print(3.0e-324)
    """Most decimal fractions cannot be perfectly represented by binary fractions, so a floating point value
    is often an approximation of a decimal fraction."""


def scientific_notation():
    """Using 'e' or 'E' with a floating point value uses scientific notation"""
    # 40,000
    print(4.0e5)
    # .0041
    print(4.1e-3)


if __name__ == "__main__":
    float_precision()
    # scientific_notation()
