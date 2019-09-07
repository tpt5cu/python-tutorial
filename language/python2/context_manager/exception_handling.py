# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
# https://docs.python.org/2.7/library/stdtypes.html#typecontextmanager - strict, official definition of exactly what a context manager is 


import sys, traceback


"""
The context manager protocol defines two methods: __enter__() and __exit__()
"""


class ExceptionHandling(object):


    def __init__(self):
        """
        The initializer will execute before any methods, so an error here can't possibly be handled by __exit__(). Remember that __init__() is the
        initializer (sets the state of an object) while __new__() is the constructor (actually creates the object)
        """
        #raise ZeroDivisionError("You divided by zero!!!")
        pass


    def __enter__(self):
        """
        If an exception occurs here, it must be handled here or outside of the context manager. The main point is that the exception never even
        reaches the __exit__() function, so it won't be handled there.
        """
        #raise ValueError("There was a ValueError!")
        pass


    def __exit__(self, exception_type, exception_value, exception_traceback):
        """
        If an exception occurred within the BODY of the with statement, then exc_type, exc_val, and exc_tb will be present, otherwise they are all
        None.
        - If the __exit__() function returns True, the with statement will suppress the exception
        - If the __exit__() function returns False, the exception will propagate up the stack
            - Never re-raise the Exception. Return False instead
        If an exception is raised within __exit__() method, the new exception replaces any exception that was being handled. Additionally, the new
        exception must be handled separately because __exit__() never returns and therefore the with statement never has the opportunity to suppress
        the new exception 
        """
        #raise OSError("There was an OSError!")
        #print(exception_type) # <type 'exceptions.TypeError'>
        #print(exception_value) # There was a TypeError!
        #print(exception_traceback) # <traceback object at ...>
        (e_type, e_val, e_tb) = sys.exc_info()
        print(e_type) # <type 'exceptions.TypeError'>
        print(e_val) # There was a TypeError!
        print(e_tb) # <traceback object at ...>
        # traceback.format_exc() actually uses sys.exc_info() to print the formatted stack trace, so this is the best way
        print(traceback.format_exc()) # Actually print the stack trace
        return True
        #return False


def use_context_manager():
    with ExceptionHandling():
        print("Inside the run-time context")
        raise TypeError("There was a TypeError!") 
    print("Outside run-time context") # This may or may not execute depending on the implementation of the context manager


if __name__ == "__main__":
    use_context_manager()
