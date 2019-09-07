"""
https://stackoverflow.com/questions/6930144/underscore-vs-double-underscore-with-variables-and-methods
https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
"""


class MyClass:
    """
    A single underscore indicates that a variable is nominally private. In other words, it's a regular variable but I'm telling other programmers not
    to touch it. However, nominally private variables won't be imported when stuff from their module is imported with 'from M import *'.
    """
    _my_private_var = 22
    """
    Double underscores mangle the name of the variable. Now, this variable cannot be used as 'MyClass.__mangled_var'. It must be used as
    '_MyClass__mangled_var. Don't do this.
    """
    __mangled_var = "Why?"
