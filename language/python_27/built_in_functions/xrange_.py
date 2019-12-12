# https://docs.python.org/2/library/functions.html#xrange


def use_xrange():
    '''
    The xrange() function is totally different from the range() function. It does not return a list. I can think of it as a generator. It has the same
    method signature as range()
    '''
    x = xrange(1, 10)
    print(x) # xrange(1, 10)
    print(type(x)) # <type 'xrange'>


def supported_operations():
    '''
    These are supported on xrange() objects:
    - indexing
    - len()
    - "in"

    No slicing!
    '''
    r = xrange(0, 10)
    print(r[1]) # 1
    print(len(r)) # 10
    #print(r[0:9:2]) # [0, 2, 4, 6, 8]
    print(5 in r) # True


if __name__ == '__main__':
    #use_xrange()
    supported_operations()