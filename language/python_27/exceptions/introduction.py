# https://docs.python.org/2.7/library/exceptions.html - list of built-in exception, includes hierarchy at the end
# https://realpython.com/python-exceptions/
# https://stackoverflow.com/questions/2903827/why-are-python-exceptions-named-error
# https://docs.python.org/2.7/tutorial/errors.html
# https://portingguide.readthedocs.io/en/latest/exceptions.html - don't rely on StandardError because Python 3 doesn't use it and porting Python 2
# code is hard


import sys, os


"""
Python has regular old errors. These can occur before execution time (e.g. SyntaxError). I'm not supposed to recover from regular old errors during
execution time. 

According to the docs, "errors detected during execution are called exceptions". Exceptions are divided into two subtypes: Errors and Warnings. I am
supposed to recover from exceptions. Thus "except Exception:" is correct while there is no such thing as "except Error:"
- try-except cannot be done in a single line in Python
- There is no StandardError in Python 3. 

sys.exc_info() returns a 3-tuple of (<type>, <message>, <traceback>)
"""

def catch_all_explicit():
    '''
    Excepting "Exception" will catch all Exceptions that inherit from Exception. This includes:
    - StandardError
        - AttributeError
        - etc.
    - StopIteration

    It does NOT include BaseException
    '''
    try:
        with open("./blablah", 'r') as f:
            text = f.read()
        #raise StandardError
    except Exception as e:
        print(type(e)) # <type 'exceptions.IOError'>
        print(e.message) # <empty string>


def catch_all_implicit():
    '''A bare except statement implicitly will catch BaseException, and therefore all other Exceptions.'''
    try:
        raise BaseException('hello there')
    except:
        print(sys.exc_info()[0]) # <type 'exceptions.BaseException'>
        print(sys.exc_info()[1]) # hello there
        print(sys.exc_info()[2]) # <traceback object at ...>


def bare_except_alias():
    '''I cannot use an alias with a bare except statement. It is a SyntaxError.'''
    try:
        raise IOError("There was an IOError")
    #except as e: # SyntaxError
    #except as e: # e is an undefined variable, so this is also a SyntaxError
    except Error as e:
        print(e.message)
    print("Hello from bare_except_alias()")


def catch_specific_exception():
    '''try-blocks can have multiple except blocks, and each except block can catch 1 or more exceptions.'''
    try:
        with open("./blablah", 'r') as f: # This line throws an IOError
            text = f.read()
        str(x)
    except ValueError:
        print("Caught ValueError") # This is ignored because the try-block threw an IOError or NameError
    except (IOError, NameError):
        print("The caught error was: " + str(sys.exc_info()[0]))
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        with open(os.path.join(os.path.dirname(__file__), "error.txt"), 'w') as f:
            f.write(str(sys.exc_info()[1]))


def catch_system_exit():
    """sys.exit() raises a SystemExit exception, which is actually a subclass of BaseException, not Exception. See the exception hierarchy link."""
    try:
        raise SystemExit(0) # 0 integer error code indicates successful process termination
    except Exception:
        print("This will never run") # Never runs
    except BaseException as e:
        if not isinstance(e, SystemExit):
            raise
        else:
            if e.code != 0:
                raise
        print("Do nothing because the exception was a SystemExit(0)")


def create_exception_object():
    '''Simply creating an exception object does not raise any exception, just like other languages'''
    e = Exception()


if __name__ == "__main__":
    #catch_all_explicit()
    catch_all_implicit()
    #bare_except_alias()
    #catch_specific_exception()
    #catch_system_exit()
    #create_exception_object()