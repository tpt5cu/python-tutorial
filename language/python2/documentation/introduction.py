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
It seems that docstring conventions in Python are quite loose, so I shouldn't worry about using a specific format. I should only worry about writing
docstrings that the rest of the team can understand.
"""


"""
I like the idea of separating the type annotation from the docstring. The docstring does not mention types (except for perhaps the return type), so if
the function changes, the docstring is less likely to need a change. Default arguments need no type annotation.

Actually, in I must be careful to intentionally NOT mention the return type in the docstring if I want to separate a type annotation from the
docstring. If I mentioned the return type in the docstring, then what's the point of using a type annotation in the first place?
"""
def add_numbers(x, y, useless=100, *z):
    # type: (float, float, *float) -> float
    """ Add at least 2 numbers together and return the result """
    z_sum = reduce(lambda a, b: a + b, z, 0)
    return z_sum + x + y


if __name__ == "__main__":
    print(add_numbers(1, 2))
    print(add_numbers(1, 2, 3, 4))