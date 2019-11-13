"""
https://docs.python.org/2.7/library/functions.html#round
"""


def round_to_digits():
    """ round() will round a float to the specified precision, which is 0 by default. """
    print(round(0.4256, 3)) # 0.425
    print(round(0.4256, 2)) # 0.43
    print(round(0.4256, 1)) # 0.4
    print(round(0.4256, 0)) # 0.0
    print(round(0.4256)) # 0.0
    print(round(0.5)) # 1.0
    print(round(2)) # 2.0


def binary_approximation_rounding():
    """
    I would think that the examples below would give the same result, but they don't. This is because 2.675 is an approximation of the actual binary
    decimal value stored in my machine, which is 2.6749999.... If this matters, I should use the "decimal" module instead of just round().
    """
    print(round(2.675, 2)) # 2.67
    print(round(2.676, 2)) # 2.68



if __name__ == "__main__":
    round_to_digits()
    #binary_approximation_rounding()