# https://docs.python.org/3.7/library/exceptions.html


'''
Use a ValueError to represent illegal argument combinations in functions.
'''


def io_exception():
    '''Raising an IOError now actually raises an OSError because IOError is just an alias for OSError now'''
    print(IOError is OSError) # True
    #raise IOError


if __name__ == '__main__':
    io_exception()