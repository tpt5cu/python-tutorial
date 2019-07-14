"""
https://stackoverflow.com/questions/40182944/difference-between-raise-try-and-assert
"""

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


def 


def raise_exception():
    raise Exception("This is my Exception")


if __name__ == "__main__":
    #assert_py()
    assert_multiple_conditions()
    #raise_exception()