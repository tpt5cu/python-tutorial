# https://realpython.com/python-exceptions/
# https://stackoverflow.com/questions/2903827/why-are-python-exceptions-named-error
# https://docs.python.org/2.7/tutorial/errors.html
# https://riptutorial.com/python/example/5535/exception-hierarchy - very useful hierarchy
# https://portingguide.readthedocs.io/en/latest/exceptions.html - don't rely on StandardError because Python 3 doesn't use it and porting Python 2
# code is hard


import sys, os


"""
Python has regular old errors. These can occur before execution time (e.g. SyntaxError). I'm not supposed to recover from regular old errors during
execution time. According to the docs, "errors detected during execution are called exceptions". Exceptions are divided into two subtypes: Errors and
Warnings. I am supposed to recover from exceptions. Thus "except Exception:" is correct while there is no such thing as "except Error:"

try-except cannot be done in a single line in Python

There is no StandardError in Python 3. 
"""

def catch_all_explicit():
    """
    Excepting "Exception" will catch all Exceptions that inherit from Exception. A bare except will catch Exception, BaseException, and StandardError
    and their subclasses.
    """
    try:
        with open("./blablah", 'r') as f:
            text = f.read()
    except Exception:
        print("Explicit catch all exceptions that inherit from Exception")


def catch_all_implicit():
    """Excepting nothing implicitly is catching Exception and StandardError and BaseException"""
    try:
        with open("./blablah", 'r') as f:
            text = f.read()
    except:
        print("Implicit catch all exceptions")


def bare_except_alias():
    """I cannot use an alias with a bare except statement. It is a SyntaxError."""
    try:
        raise IOError("There was an IOError")
    #except as e: # SyntaxError
    except e: # e is an undefined variable, so this is also a SyntaxError
        print(e.message)
    print("Hello from bare_except_alias()")


def catch_specific_exception():
    """try-blocks can have multiple except blocks, and each except block can catch 1 or more exceptions."""
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
    """
    sys.exit() raises a SystemExit exception, which is actually a subclass of BaseException, not Exception. See the exception hierarchy link.
    """
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


if __name__ == "__main__":
    #catch_all_explicit()
    #catch_all_implicit()
    bare_except_alias()
    #catch_specific_exception()
    #catch_system_exit()