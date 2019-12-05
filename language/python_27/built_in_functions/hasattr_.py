# https://docs.python.org/2.7/library/functions.html#hasattr
# https://stackoverflow.com/questions/903130/hasattr-vs-try-except-block-to-deal-with-non-existent-attributes


import timeit


def see_if_attribute_exists():
    '''
    hasattr() returns True if the object has the attribute, otherwise False
    - Under the hood, hasattr() calls getattr() and sees whether or not an exception is raised
    '''
    i = 5
    s = 'hi'
    print(hasattr(i, '__len__')) # False
    print(hasattr(s, '__len__')) # True
    print(hasattr(i, '__cmp__')) # True
    print(hasattr(s, '__cmp__')) # False


class Foo(object):

    def __getattr__(self, attribute):
        #raise BaseException('No attribute "{}"'.format(attribute))
        #raise KeyboardInterrupt('No attribute "{}"'.format(attribute))
        raise Exception('No attribute "{}"'.format(attribute))


def swallow_exception():
    '''
    hasattr() swallows any Exeception object (i.e not BaseException or KeyboardInterrupt) that would be caused by accessing a nonexistant attribute
    '''
    f = Foo()
    #print(getattr(f, 'foo')) # BaseException
    print(hasattr(f, 'foo')) # False


def try_except_vs_hasattr():
    '''
    TLDR: hasattr() is faster than try-except across the board
    - hasattr() is faster than try-except when an exception is thrown because hasattr() does exception handling in C while try-except does it in
      Python bytecode (see Stack Overflow)
        - This is consistently True for Python 2 and Python 3
    - Stack Overflow says hasattr() is slower than try-except when the attribute exists because try-except doesn't do anything while hasattr() performs a look-up
        - However, the results show that hasattr() is usually faster than try-except in Python 2.7 and just about always faster in Python 3.7.5
    '''
    # Python 2: 0.815373182297
    # Python 3: 0.24359389999999997
    print(timeit.timeit(setup='i = 5', stmt='hasattr(i, "__len__")'))
    # Python 2: 1.30319809914
    # Python 3: 1.026395133
    print(timeit.timeit(setup='i = 5', stmt='try:\n getattr(i, "__len__")\nexcept:\n pass'))
    # Python 2: 0.196892023087
    # Python 3: 0.13797200899999984
    print(timeit.timeit(setup='i = 5', stmt='hasattr(i, "__cmp__")'))
    # Python 2: 0.231602191925
    # Python 3: 0.9696569750000001
    print(timeit.timeit(setup='i = 5', stmt='try:\n getattr(i, "__cmp__")\nexcept:\n pass'))


if __name__ == '__main__':
    #see_if_attribute_exists()
    #swallow_exception()
    try_except_vs_hasattr()