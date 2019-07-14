

def assert_grouping(x, y, z):
    """I want to assert that x is True, and either y or z is also True."""
    # No AssertionError because even if x and y are False, z is True. BAD!
    #assert x and y or z
    # AssertionError because x is False
    assert x and (y or z)


if __name__ == "__main__":
    assert_grouping(False, False, True)