"""
https://docs.python-guide.org/writing/documentation/
https://stackoverflow.com/questions/35230635/type-hinting-in-python-2
"""


"""
Sphinx is the most popular documentation engine for Python.
"""


"""
PEP 484 for Python 3.5 added type hinting to allow a programmer to document function parameters. It also specified an optional syntax for doing the same thing in
Python 2.7. The "# type: (param1 type, param2 type, ...) -> <return value> " annotation must go BEFORE the docstring.
"""


"""
I like the idea of separating the type annotation from the docstring. The docstring does not mention types, so if the function changes, the docstring
is less likely to need a change. Default arguments need no type annotation.
"""
def add_numbers(x, y, useless=100, *z):
    # type: (float, float, *float) -> float
    """ Add at least 2 numbers together and return the result """
    z_sum = reduce(lambda a, b: a + b, z, 0)
    return z_sum + x + y


if __name__ == "__main__":
    print(add_numbers(1, 2))
    print(add_numbers(1, 2, 3, 4))