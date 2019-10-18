# https://docs.python.org/2.7/reference/expressions.html#comparisons
# https://stackoverflow.com/questions/36921558/how-int-object-uses-operator-without-eq-method-in-python2 - interger comparison with __cmp__


import inspect


"""
The default behavior for equality comparison (i.e. "==" and "!=") is based on the identity of the objects. However, comparison operators will deviate
from this default behavior if rich comparison methods or a __cmp__ method have been defined.
"""


class SpecialNumber(int):
    """I can't modify the __cmp__ attribute of regular integers, so I'll make a wrapper class instead."""
    def __cmp__(self, other):
        """This method is used when rich comparison functions are not defined"""
        return 0


def incorrect_way_to_change_equality_behavior():
    """
    In Python 2, the built-in integer type has a __cmp__ but no __eq__ method (this is actually reversed in Python 3. Insane!). In Python 3, the
    __cmp__ method isn't used anymore!
    """
    print(dir(5))
    #print(type(5) # <type 'int'>
    #print(hasattr(5, "__cmp__")) # True
    #print(hasattr(5, "__eq__")) # False
    x = 5
    #setattr(x, "__cmp__", None) # AttributeError '__cmp__' is read-only


def compare_special_numbers():
    """
    There is NO way to modify how comparison works for built-in types like int. Creating a wrapper class doesn't change this, but this example does
    show that overriding __cmp__() works.
    """
    #x = 5
    #y = 5
    #print(hash(x)) # 5
    #print(hash(y)) # 5
    #print(5 == 5) # True
    x = SpecialNumber(4)
    #print(type(x)) # <class '__main__.SpecialNumber'>
    #print(hasattr(x, "__cmp__")) # True
    #print(x.__cmp__) # <bound method SpecialNumber.__cmp__ of ...>
    y = SpecialNumber(77)
    # SpecialNumber doesn't define __hash__, so the __hash__ of int is used
    #print(hasattr(4, "__hash__")) # True
    print(hash(x)) # 4
    print(hash(y)) # 77
    print(x == y) # Would be False for regular ints, but is True for SpecialNumbers


if __name__ == "__main__":
    #incorrect_way_to_change_equality_behavior()
    compare_special_numbers()