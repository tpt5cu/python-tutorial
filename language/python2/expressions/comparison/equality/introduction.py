# https://docs.python.org/2.7/reference/expressions.html#comparisons
# https://stackoverflow.com/questions/36921558/how-int-object-uses-operator-without-eq-method-in-python2 - interger comparison with __cmp__


import inspect


"""
The default behavior for equality comparison (i.e. "==" and "!=") is based on the identity of the objects. However, comparison operators will deviate
from this default behavior if rich comparison methods or a __cmp__ method have been defined.
"""


class SpecialNumber(object):
    """I can't modify the __cmp__ attribute of regular integers, so I'll make a wrapper class instead."""
    def __init__(self, val):
        self.val = val


    def __cmp__(self, other):
        """This method is used when rich comparison functions are not defined"""





def default_equality_behavior():
    """
    In Python 2, the built-in integer type has a __cmp__ but no __eq__ method (this is actually reversed in Python 3. Insane!). In Python 3, the
    __cmp__ method isn't used anymore!
    """
    #print(dir(5))
    #print(hasattr(5, "__cmp__")) # True
    #print(hasattr(5, "__eq__")) # False
    x = 5
    setattr(x, "__cmp__", None)
    y = 7
    setattr(y, "__cmp__", None)


if __name__ == "__main__":
    default_equality_behavior()