

def x():
    """ The xrange() function is totally different from the range() function. It does not return a list. """
    x = xrange(1, 10)
    print(x)
    print(type(x)) # <type 'xrange'>


if __name__ == "__main__":
    x()