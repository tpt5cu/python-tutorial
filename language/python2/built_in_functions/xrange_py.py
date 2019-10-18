# https://docs.python.org/2/library/functions.html#xrange

def x():
    """
    The xrange() function is totally different from the range() function. It does not return a list. I can think of it as a generator. It has the same
    method signature as range()
    """
    x = xrange(1, 10)
    print(x)
    print(type(x)) # <type 'xrange'>


if __name__ == "__main__":
    #x()
    x, y = 5, 5
    print(x)
    print(y)