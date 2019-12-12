'''This code works in Python 2 and 3'''


def traverse_iterable():
    '''
    The next() built_in function merely calls an iterator's next() method (Python 2) or __next__() method (Python 3). It provides a version-compatible way
    to retrieve values from an iterator
    '''
    string = 'Twenty Thousand Leagues Under the Sea'
    iterator = iter(string)
    print(next(iterator)) # T
    print(next(iterator)) # w
    print(next(iterator)) # e
    print(next(iterator)) # n
    print(next(iterator)) # t
    print(next(iterator)) # y


if __name__ == '__main__':
    traverse_iterable()