# https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x
# http://treyhunner.com/2018/02/python-3-s-range-better-than-python-2-s-xrange/
# https://docs.python.org/3/library/functions.html#func-range


def examine_range():
    """In Python2, range() creates a list in memory of the specified size. In Python3, range() is equivalent (actually
     it's better than) to xrange().

    In this example, running this script with python2 will print a list containing the elements 0 through 999. Running
    this script with python3 will literally print 'range(0, 1000)'
    """
    range_list = range(0, 1000)
    print(range_list)


def examine_xrange():
    """xrange is an immutable sequence type that is evaluated lazily. It is not a generator. """

    """xrange() is not defined in Python3 (range() acts like xrange()), so the code throws a NameError.
     In Python2, this code prints '(xrange(1, 1000)'
    """
    # my_xrange = xrange(1, 1000)
    # print(my_xrange)


def use_range():
    """My interpreter is set to Python3. A range is an immutable sequence type in Python3"""
    for num in range(0, 100):
        print(num)


if __name__ == "__main__":
    # examine_range()
    # examine_xrange()
    use_range()
