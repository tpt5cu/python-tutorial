# https://stackoverflow.com/questions/1529002/cant-set-attributes-of-object-class

"""In order for ANY object instance to support arbitrary attribute assignment, the object must have a __dict__
attribute. Built-in type instances do NOT have a __dict__ attribute for optimization reasons.

In Python (i.e. CPython, the original implementation of Python), all of the built-in types and data structures are
simply classes implemented in C. These built-in types do NOT allow arbitrary attributes to be tacked on at runtime.
Any custom subclass of any built-in type CAN have arbitrary attributes, but these subclass instances will be MUCH
larger than the built-in types. This is fine for my purposes, but if every built-in type had a
__dict__ attribute, the core Python code would be bloated.
"""


def cannot_add_attribute():
    """All of these lines throw AttributeError because built-in type instances don't have a __dict__ attribute"""
    d = {}
    # d.cool = 5
    l = []
    # l.cool = 5
    o = ()
    o.cool = 5


class MyDict(dict):

    def __init__(self, cool=5):
        self.cool = cool


def create_custom_attribute():
    """MyDict is a subclass of dictionary, so I can add arbitrary attributes."""
    obj = MyDict()
    obj.cool = 10
    obj.foo = 77
    print(obj.get(5))


if __name__ == "__main__":
     cannot_add_attribute()
    # create_custom_attribute()