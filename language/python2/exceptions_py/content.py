# https://docs.python.org/2/library/sys.html


import sys


def raise_exception():
    e = Exception("This is a custom exception message.")
    raise e


def raise_StopIteration():
    my_list = []
    my_list.__iter__().next()


def view_exception_message():
    """
    I don't need to use sys.exc_info()[1] when Exceptions have their own "message" attribute! Exceptions don't have to have a message. For example,
    StopIteration has no message.
    """
    try:
        #raise_exception()
        raise_StopIteration()
    except Exception as e:
        print(e.args) # ('This is a custom exception message.',)
        print(e.message) # This is a custom exception message
        print(sys.exc_info()[1]) # This is a custom exception message


if __name__ == "__main__":
    view_exception_message()
    
