"""
https://stackoverflow.com/questions/4015417/python-class-inherits-object (Why is the 'object' constructor important from an inheritance perspective?)
https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
https://stackoverflow.com/questions/865911/is-everything-an-object-in-python-like-ruby ???
https://github.com/python/cpython (the source code of Python itself!)
https://docs.python.org/2.7/library/functions.html#object
"""

"""
The built-in object() constructor doesn't seem to be that important on its own. Thus, while "everything in Python inherits from object" is an axiom,
that does not mean that most of the functionality in Python comes from the 'object' class object.

In Python3, all custom classes automatically subclass 'object'. In Python2, this must be done explicitly.
"""

class MyClass(object):
    """
    Inheriting from the 'object' constructor is done simply by making MyClass a subclass of 'object'. 'object' itself is just an object that is also a
    callable constructor. Subclassing the 'object' constructor provides MyClass with additional useful behavior:
    - Support for descriptors: 
    - x

    I need to come back to this...
    """
    pass
