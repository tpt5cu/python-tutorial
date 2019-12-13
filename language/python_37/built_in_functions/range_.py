'''The range() function now behaves like the old xrange() function (i.e. like an iterator), and xrange() function no longer exists'''


def print_numbers():
    '''Prints from 0-9 '''
    r = range(0, 10)
    print(r) # range(0, 10)
    for num in r:
        print(num)


def supported_operations():
    '''
    These are still supported on range() objects, but can return different things from Python 2
    - indexing
    - len()
    - slicing (returns a new range() object)
    - "in"
    - Repeated iteration over the same range() object
    '''
    r = range(0, 10)
    print(r[1]) # 1
    print(len(r)) # 10
    print(r[0:9:2]) # range(0, 9, 2)
    print(5 in r) # True


if __name__ == '__main__':
    #print_numbers()
    supported_operations()