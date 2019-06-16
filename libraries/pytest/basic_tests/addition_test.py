def func(x):
    """
    This is a function that I want to test. It could be any function
    """
    return x + 1

def test_answer():
    """
    This function is prefixed with "text*", so pytest detects it and runs it
    """
    # This is wrong on purpose
    assert func(3) == 5