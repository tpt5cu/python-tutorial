import sys


def raise_exception():
    '''StandardError was removed in Python 3'''
    raise FloatingPointError('There was a floating point error!')


def use_discontinued_syntax():
    '''Using a comma to deliniate a VARIABLE for a caught exception object was confusing and is now a SyntaxError'''
    try:
        raise_exception()
    #except MemoryError, ArithmeticError: # Invalid syntax
    #    pass
    except:
        pass


def use_valid_syntax():
    '''
    - Bare except statements are valid
    - Using a tuple to catch multiple exceptions is valid
    - Using an alias with 'as' is recommended
    '''
    try:
        raise_exception()
    except:
        print(sys.exc_info()[1])
    except (MemoryError, ArithmeticError):
        print(sys.exc_info()[1]) # There was a floating point error
    except FloatingPointError as f:
        print(f) # There was a floating point error!


if __name__ == '__main__':
    #use_discontinued_syntax()
    use_valid_syntax()