"""
https://realpython.com/python-exceptions/
"""
import sys, os

"""
try-except cannot be done in a single line in Python
"""

def catch_all_explicit():
    """ Excepting "Exception" will catch all exceptions """
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