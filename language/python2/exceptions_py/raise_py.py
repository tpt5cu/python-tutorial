"""
https://stackoverflow.com/questions/40182944/difference-between-raise-try-and-assert
"""

"""
assert and raise statements both raise exceptions.
- assert statements can be disabled, so don't rely on them for production debugging. They are essentially for runtime debugging.
- raise statements are for raising exceptions normally.
"""

def my_assert():
    """
    assert is a STATEMENT, not a function.
    Syntax: assert <condition>
    NOT syntax: assert(<condition>, <condition>, etc.)
    """
    #assert 1 == 2 # This is correct usage
    # This will never throw an error because bool( (1 == 2, "Hello") ) will always be True. I am asserting that a non-empty tuple is True, which it
    # always will be
    assert (1 == 2, "Hello")

def raise_exception():
    raise Exception("This is my Exception")

if __name__ == "__main__":
    my_assert()
    #raise_exception()