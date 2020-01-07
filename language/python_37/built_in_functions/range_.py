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


def float_length():
    '''The range() function only accepts integers!'''
    #gen = range(4.89) # TypeError: 'float' object cannot be interpreted as an integer
    gen = range (4.89//1)
    list_ = list(gen)
    print(list_)


if __name__ == '__main__':
    #print_numbers()
    #supported_operations()
    float_length()