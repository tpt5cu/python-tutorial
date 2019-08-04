# https://stackoverflow.com/questions/40182944/difference-between-raise-try-and-assert
# https://stackoverflow.com/questions/16706956/is-there-a-difference-between-raise-exception-and-raise-exception-without


"""
assert and raise statements both raise exceptions.
- assert statements can be disabled, so don't rely on them for production debugging. They are essentially for runtime debugging.
- raise statements are for raising exceptions normally.
"""


def assert_py():
    """
    assert is a STATEMENT, not a function.
    Syntax: assert <condition>
    NOT syntax: assert(<condition>, <condition>, etc.)
    """
    #assert 1 == 2 # This is correct usage
    # This will never throw an error because bool( (1 == 2, "Hello") ) will always be True. I am asserting that a non-empty tuple is True, which it
    # always will be
    assert (1 == 2, "Hello")


def assert_multiple_conditions():
    # AssertionError
    #assert 1 == 1 and 2 == 2 and 3 == 4
    # No AssertionError
    assert 1 == 1 and 2 == 2 and 3 == 3
    # No AssertionError. That's because 5 == 5 is always True
    assert 1 == 0 and 2 == 3 or 5 == 5
    # No AssertionError. That's because 6 == 6 and 7 == 7 is always True
    assert 1 == 2 or 6 == 6 and 7 == 7


def raise_exception():
    """
    Exception and Exception() both do the same thing because using the class automatically creates an instance. It's perfectly okay to use the class.
    In fact, it's common to use the class when no arguments need to be passed.
    """
    raise Exception("This is my Exception")


def re_raise():
    pass


if __name__ == "__main__":
    #assert_py()
    assert_multiple_conditions()
    #raise_exception()