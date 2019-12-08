# https://docs.python.org/2.7/tutorial/errors.html - general introduction to exceptions
# https://docs.python.org/2.7/library/exceptions.html - list of built-in exception, includes hierarchy at the end
# https://realpython.com/python-exceptions/ - general introduction to exception handling
# https://stackoverflow.com/questions/2903827/why-are-python-exceptions-named-erro - why are some exception names named with "Error" in Python?


import sys


'''
Python has regular old errors. These can occur before execution time (e.g. SyntaxError). I'm not supposed to recover from regular old errors during
execution time. 

According to the docs, 'errors detected during execution are called exceptions'. Exceptions are divided into two subtypes: Errors and Warnings. I am
supposed to recover from exceptions. Thus 'except Exception:' is correct while there is no such thing as 'except Error:'
- try-except cannot be done in a single line in Python
- sys.exc_info() returns a 3-tuple of (<type>, <message>, <traceback>)
'''


def try_except_else_finally():
    '''
    There can be 1 optional else-clause that can follow all except-clauses. The else-clause will execute after the try-clause if and only if the
    try-clause did not raise any exceptions
    - If a try-clause returns, an else-clause will not execute
    - A finally-clause will always execute regardless of what happens elsewhere
        - If the try-clause returns, the finally-clause gets executed first
        - If an except-clause does not handle an exception, the exception is re-raised after the finally-clause
    '''
    try:
        with open('made-up-file-hahah.txt') as f:
            print(f.read())
        # UnboundLocalError
        #asdf = asdf 
        #x = 1
        #return x
    except IOError as e:
        print('There was an IOError!')
    # This else-clause is valid, but there can be no other else statements nor except statements after the single else statement
    #else:
    #    print('Invalid syntax')
    except ZeroDivisionError as e:
        print('There was a ZeroDivisionError!')
    else:
        print('Continuing to execute as normal')
    finally:
        print('This always executes no matter if the try-clause returns or an exception was raised')


def catch_all_explicit():
    '''
    Excepting "Exception" will catch all Exceptions that inherit from Exception.
    - This includes: StandardError, AttributeError, StopIteration, etc.
    - It does NOT include BaseException
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


def catch_specific_exception():
    '''
    try-blocks can have multiple except blocks, and each except block can catch 1 or more exceptions.
    - Be careful about catching multiple exceptions in the same except statement. If I want to do this the, except statement should be followed by a
      tuple with parentheses. If I don't use parentheses, then the second item in the tuple is not a tuple item at all, but the alias of the caught
      exception!
    '''
    try:
        # This line throws an IOError
        with open("./blablah", 'r') as f: 
            text = f.read()
    except ValueError:
        # This is ignored because the try-block threw an IOError or NameError
        print("Caught ValueError") 
    # This is a tricky bug
    except IOError, NameError:
        print 'hi'
        print NameError # [Errno 2] No such file or directory: './blablah'
    # This is correct
    except (IOError, NameError):
        print("The caught error was: " + str(sys.exc_info()[0])) # The caught error was: <type 'exceptions.IOError'>
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        with open(os.path.join(os.path.dirname(__file__), "error.txt"), 'w') as f:
            f.write(str(sys.exc_info()[1]))


def catch_system_exit():
    '''
    sys.exit() raises a SystemExit exception, which is actually a subclass of BaseException, not Exception. See the exception hierarchy link.
    - The "code" attribute indicates the system exit status
        - If the error code is 0, it indicates successful process termination
        - If the error code is 1 or anything != 0, it indicates an error
    '''
    try:
        raise SystemExit(0) 
    except Exception:
        print('This will never run') # Never runs
    except BaseException as e:
        if not isinstance(e, SystemExit):
            raise
        else:
            if e.code != 0:
                raise
        print('Do nothing because the exception was a SystemExit(0)')


if __name__ == '__main__':
    #val = try_except_else_finally()
    #print('val was: ' + str(val))
    #catch_all_explicit()
    #catch_all_implicit()
    #catch_specific_exception()
    catch_system_exit()