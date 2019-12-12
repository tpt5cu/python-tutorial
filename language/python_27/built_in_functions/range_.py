# https://docs.python.org/2.7/library/functions.html#range
# https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x


'''
The built-in range() function in Python 2 returns a list of the specified size immediately upon invocation.
This is different from xrange(), which returns an xrange type. An xrange type is an iterable, but it is not an iterator. It is also not a generator.
- range() can take 1, 2, or 3 arguments
- xrange() takes less memory. Neither has particularly better performance
'''


def print_numbers():
    '''Prints from 0-9 '''
    for num in range(0, 10):
        print(num)


def supported_operations():
    '''
    These are supported on range() objects:
    - indexing
    - len()
    - slicing (returns a new list)
    - "in"
    '''
    r = xrange(0, 10)
    print(r[1]) # 1
    print(len(r)) # 10
    print(r[0:9:2]) # [0, 2, 4, 6, 8]
    print(5 in r) # True


def repeated_iteration():
    '''Both range() and xrange() support repeated iteration in Python 2'''
    r = range(0, 10)
    #r = xrange(0, 10)
    for e in r:
        print(e)
    print('')
    for e in r:
        print(e)


def print_with_step():
    for num in range(0, 10, 2):
        print(num) # 0\n2\n4\n6\n8


def print_backwards():
    for num in range(10, 0, -1):
        print(num) # 10 -> 1


if __name__ == '__main__':
    #print_numbers()
    #supported_operations()
    repeated_iteration()
    #print_with_step()
    #print_backwards()