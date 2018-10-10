# https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
# https://www.python.org/dev/peps/pep-0257/


"""Turing a docstring into a function signature is verbose and brittle because if I change the function then
I have to change the docstring. Use function annotations?
"""

# docstrings go inside of a module, function, class, or method.
def docstring():
    """ Including a string literal as the first line of module, function, class, or method definition sets
    the __doc__ special attribute of the respective object to be that literal. The summary line of a docstring
     should roughly follow the format: "Do <something> and return <something>".
    """
    print("This function has a docstring that is accessible via the __doc__ special property.")


"""Here is an example of a real doctring"""
def add_numbers_function_example():
    """Return the result of adding two ints"""
    pass


# User-defined classes use Pascal case. Built-in classes are all Snake case (lower case).
class MyCustomClass:
    """A class docstring summarizes its behavior and lists public methods and instance variables.

    A multi-line docstring always has a one-line summary line, followed by a blank line, followed by
    additional information. A class docstring will specify additional information if the class is a subclass.
    """
    def method1(self):
        pass

    def method2(self):
        pass
