# https://docs.python.org/2.7/library/exceptions.html - exception contents
# https://docs.python.org/2/library/sys.html


import sys


def variable_exception_initialization():
    '''
    How exception objects are initialized determines whether or not there is a non-empty "message" attribute
    - This behaivor exists because more specific exceptions use the "args" attribute uniquely
        - E.g. IOError can contain something like: (2, 'No such file or directory') yet have no "message" attribute
    '''
    # This is typically how exceptions are created. There will be a filled-in "args" attribute and a filled-in "message" attribute
    e = Exception('hello world')
    print(e.args) # ('hello world',)
    print(e.message) # hello world
    # Exceptions can also be created with a variable number of arguments. In that case, the "message" attribute is guaranteed to be an empty string
    e = Exception('foo', 'bar', 'baz')
    print(e.args) # ('foo', 'bar', 'baz')
    print(e.message) # ""


def raise_exception():
    e = Exception("This is a custom exception message.")
    raise e


def raise_StopIteration():
    my_list = []
    my_list.__iter__().next()


def view_exception_message():
    '''
    I don't need to use sys.exc_info()[1]. Instead, I can examine the "args" attribute of an exception.
    - Don't use the unreliable "message" attribute on exceptions; it may or may not be an empty string
    '''
    try:
        raise_exception()
        #raise_StopIteration()
    except StopIteration as e:
        print(e.args) # ()
        # Don't use the message attribute
        #print(type(e.message)) # <type 'str'>
        #print(e.message if e.message != '' else 'message was ""') # message was ""
    except Exception as e:
        print(e.args) # ('This is a custom exception message.',)
        print(sys.exc_info()[1]) # This is a custom exception message
        # Don't use the message attribute
        #print(e.message) # This is a custom exception message
        #print(type(e.message)) # <type 'str'>


def view_exception_type():
    try:
        raise ZeroDivisionError('Cannot divide by zero!')
    except Exception as e:
        print(type(e)) # <type 'exceptions.ZeroDivisionError'>
        print(isinstance(e, GeneratorExit)) # False
        print(isinstance(e, BaseException)) # True


def view_exception_traceback():
    '''I believe this must be done with sys.exc_info()[2]. There is no traceback attribute directly on an exception'''
    pass


if __name__ == "__main__":
    #variable_exception_initialization()
    view_exception_message()