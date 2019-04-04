# https://stackoverflow.com/questions/19473185/what-is-a-none-value


def identify_none():
    """None is its own type, and there is exactly one instance of None. This single instance is of the class Nonetype.
    None is Python's version of null.
    """
    a = None
    b = None
    print(id(a))
    print(id(b))
    print(type(None))
    if None is None:
        print("None is None!")


def return_none(foo=None):
    """If a function doesn't return anything, then it implicitly returns None. That's why I see the word None
    appear at seemingly random times.

    None is often used as a default value to signal that nothing was passed.
    """
    if foo is not None:
        print("I'm doing something cool now")


if __name__ == "__main__":
    # identify_none()
    print(return_none("whoo"))
