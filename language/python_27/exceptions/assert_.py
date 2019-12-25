'''

assert and raise statements both raise exceptions.
- assert statements can be disabled, so don't rely on them for production debugging. They are essentially for runtime debugging.
- raise statements are for raising exceptions normally.
'''


def assert_with_custom_message():
    '''
    Assert is a keyword, not a function, but it can take two arguments
    - Syntax: assert <condition> [<custom message>]
    '''
    # This never is triggered because there is no AssertionError
    assert 1==1, 'This is the first assertion error message'
    #assert 1==2, 'This is the second assertion error message'


def assert_nonempty_tuple():
    '''Any non-empty sequence is always True, hence the syntax warning'''
    assert (1==2, 'Some string') # SyntaxWarning: always true


def assert_multiple_conditions():
    #assert 1 == 1 and 2 == 2 and 3 == 4 # AssertionError
    # No AssertionError
    assert 1 == 1 and 2 == 2 and 3 == 3
    # No AssertionError. That's because 5 == 5 is always True
    assert 1 == 0 and 2 == 3 or 5 == 5
    # No AssertionError. That's because 6 == 6 and 7 == 7 is always True
    assert 1 == 2 or 6 == 6 and 7 == 7


def assert_grouping(x, y, z):
    '''I want to assert that x is True, and either y or z is also True.'''
    # No AssertionError because even if x and y are False, z is True. BAD!
    #assert x and y or z
    # AssertionError because x is False
    assert x and (y or z)


if __name__ == '__main__':
    assert_with_custom_message()
    #assert_nonempty_tuple()
    #assert_multiple_conditions()
    #assert_grouping(False, False, True)