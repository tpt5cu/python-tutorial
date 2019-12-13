'''Python 3 removed StandardError'''


def use_exception_outside_context_manager():
    '''Python 2 doesn't care if I use an exception outside of a context manager, but Python 3 gives an UnboundLocalError'''
    try:
        raise Exception('foobar')
    except Exception as e:
        print(e.args) # ('foobar',)
        f = e
    #print(e.args) # UnboundLocalError
    print(f.args) # ('foobar',)


def iterate_exception():
    '''Exceptions are not iterable objects anymore'''
    e = Exception(1, 2, 3, 4)
    for i in e: # TypeError
        print(i)


if __name__ == '__main__':
    #use_exception_outside_context_manager()
    iterate_exception()