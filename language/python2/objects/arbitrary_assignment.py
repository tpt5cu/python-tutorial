"""
https://stackoverflow.com/questions/1529002/cant-set-attributes-of-object-class
"""

"""
In order for ANY object instance to support arbitrary attribute assignment, the object must have a __dict__ attribute. Built-in type instances do NOT
have a __dict__ attribute for optimization reasons.
- A dictionary for holding arbitrary values takes up a lot of space, and most of the time I'm not adding random attributes to built-in types like
  lists and dictionaries. Therefore, it doesn't make sense to bloat Python by giving every object a __dict__.

In Python (i.e. CPython, the original implementation of Python), all of the built-in types and data structures are simply classes implemented in C.
These built-in types do NOT allow arbitrary attributes to be tacked on at runtime. Any custom subclass of any built-in type CAN have arbitrary
attributes, but these subclass instances will be MUCH larger than the built-in types. This is fine for my purposes, but if every built-in type had a
__dict__ attribute, the core Python code would be bloated.
"""


def cannot_add_attribute():
    """'All of these lines throw an AttributeError because built-in type instances don't have a __dict__ attribute """
    d = {}
    #d.cool = 5
    l = []
    #l.cool = 5
    t = ()
    #t.cool = 5
    o = object()
    #o.foo = "bar"


class MyDict(dict):

    def __init__(self, cool=5):
        self.cool = cool


def create_custom_attribute():
    """
    MyDict is a custom class. A class object has its own __dict__ for class attributes and any instances created from the class object will have their
    own individual __dict__ attribute for storing arbitrary values.
    """
    MyDict.foo = "bar"
    print(MyDict.__dict__) # {'foo': 'bar', ...}
    obj = MyDict()
    obj.baz = "boom"
    print(obj.__dict__) # {'baz': 'boom', 'cool': 5}
    print(obj.foo) # 'foo' does not exist in the instance __dict__, so it is looked-up and found in the class __dict__


if __name__ == "__main__":
    #cannot_add_attribute()
    create_custom_attribute()