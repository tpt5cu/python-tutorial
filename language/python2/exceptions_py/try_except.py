"""
https://realpython.com/python-exceptions/
https://stackoverflow.com/questions/2903827/why-are-python-exceptions-named-error
https://docs.python.org/2.7/tutorial/errors.html
"""


import sys, os


"""
Python has regular old errors. These can occur before execution time (e.g. SyntaxError). I'm not supposed to recover from regular old errors during
execution time. According to the docs, "errors detected during execution are called exceptions". Exceptions are divided into two subtypes: Errors and
Warnings. I am supposed to recover from exceptions. Thus "except Exception:" is correct while there is no such thing as "except Error:"
"""


"""
try-except cannot be done in a single line in Python
"""

def catch_all_explicit():
    """ Excepting "Exception" (or just a bare except) will catch all exceptions """
    try:
        with open("./blablah", 'r') as f:
            text = f.read()
    except Exception:
        print("Explicit catch all exceptions")

def catch_all_implicit():
    """ Excepting nothing implicitly is catching "Exception" """
    try:
        with open("./blablah", 'r') as f:
            text = f.read()
    except:
        print("Implicit catch all exceptions")


def catch_specific_exception():
    """ try-blocks can have multiple except blocks, and each except block can catch 1 or more exceptions. """
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


if __name__ == "__main__":
    #catch_all_explicit()
    #catch_all_implicit()
    catch_specific_exception()