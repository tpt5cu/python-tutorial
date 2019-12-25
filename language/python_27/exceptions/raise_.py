# https://stackoverflow.com/questions/40182944/difference-between-raise-try-and-assert
# https://stackoverflow.com/questions/16706956/is-there-a-difference-between-raise-exception-and-raise-exception-without


def raise_exception():
    '''
    Exception and Exception() both do the same thing because using the class automatically creates an instance. It's perfectly okay to use the class.
    In fact, it's common to use the class when no arguments need to be passed.
    - Using a plain 'raise' statement will automatically re-raise the current exception
    '''
    try:
        raise Exception('This is my Exception')
    except Exception as e:
        print('Handled the exception')
        raise


if __name__ == '__main__':
    raise_exception()