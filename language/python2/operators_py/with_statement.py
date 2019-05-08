"""
https://effbot.org/zone/python-with-statement.htm
"""

"""
The with-statement can be used on any object that has an __enter__ and an __exit__ method. Whatever is returned by __enter__ is assigned to the "as"
part of of the with statement, and the code in the __exit__ method is always called when the with-statement scope exits.

This is not the same thing as a @context_manager
"""

class MyClass(object):

    def __init__(self):
        print("MyClass instance created")

class OtherClass(object):
    """ These exact method signatures are required to implement these methods """

    def __enter__(self):
        return "Context was entered"

    def __exit__(self, type, value, traceback):
        pass

def my_class_with():
    """ Without both the __enter__ and __exit__ methods defined on this object, this code will throw an exception """
    with MyClass() as thing:
        print("hello from with-statement")

def other_class_with():
    with OtherClass() as o:
        print(o)

if __name__ == "__main__":
    #my_class_with()
    other_class_with()
