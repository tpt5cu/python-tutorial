# https://stackoverflow.com/questions/12274606/theres-no-next-function-in-a-yield-generator-in-python-3


def consume_generator():
    '''
    Python 3 renamed the next() method of iterators (and therefore generators) to __next__().
    - Since the next() built-in function already retrieves the next element from an iterator, use it instead of invoking __next__()
    '''
    gen = (l for l in 'Hyper')
    print(next(gen)) # H


if __name__ == '__main__':
    consume_generator()