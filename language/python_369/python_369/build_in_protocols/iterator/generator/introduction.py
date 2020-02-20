# https://stackoverflow.com/questions/12274606/theres-no-next-function-in-a-yield-generator-in-python-3


def consume_generator():
    '''
    Python 3 renamed the next() method of iterators (and therefore generators) to __next__().
    - Since the next() built-in function already retrieves the next element from an iterator, use it instead of invoking __next__()
    '''
    gen = (l for l in 'Hyper')
    print(next(gen)) # H


def slice_iterator():
    '''An iterator is not subscriptable, therefore it is not slicable'''
    m = map(lambda x: x / 2, [2, 4, 6, 8])
    print(list(m)[0]) # 1.0
    #print(m[0]) # TypeError: 'map' object is not subscriptable
    #print(m[1:3]) # TypeError: 'map' object is not subscriptable


if __name__ == '__main__':
    #consume_generator()
    slice_iterator()