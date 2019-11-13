# https://docs.python.org/2.7/library/functions.html#dir


"""
dir() is more of a convenience function than a rigorously defined object inspector function. It does slightly different things depending on the type
of the object that is being inspected
"""

class OldClass():

    def __init__(self, number):
        self.number = number


class MyClass(object):

    class_property = "Nice class property"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello my name is " + self.name)


def inspect_oldclass_instance():
    """Old-style classes do no inherit from the Python 'object', therefore the attributes of 'object' won't be found"""
    obj = OldClass(11)
    print(dir(obj)) # ['__doc__', '__init__', '__module__', 'number']
    # Why isn't __class__ seen by dir()? I don't know but it exists
    print(obj.__class__) # __main__.OldClass
    print(obj.__dict__) # {'number': 11}
    #print(obj.__getattribute__) # AttributeError
    #print(obj.__hash__) # AttributeError
    #print(obj.__reduce__) # AttributeError
    #print(obj.__setattr__) # AttributeError
    #print(obj.__delattr__) # AttributeError
    #print(obj.__new__) # AttributeError
    #print(obj.__subclasshook__) # AttributeError
    #print(obj.__weakref__) # AttributeError


def inspect_instance():
    """
    When inspecting an object instance, dir() returns a list that contains:
    - the object's attribute names: 'name'
    - the names of its class's attributes: 'class_property', 'say_hello'
    - the attributes of its base classes: everything defined on 'object'

    As demonstrated by comparing with OldClass, the Python 'object' implements the following so that only its subclasses can use the methods without
    explicitly defining them:
    - __getattribute__
    - __hash__
    - __reduce__
    - __setattr__
    - __delattr__
    - __new__
    - __subclasshook__
    - __weakref__
    - others!
    The Python 'object' does not appear to have the following attributes:
    - __class__
    """
    obj = MyClass("Jello")
    print(dir(obj))
    print("")
    print(obj.__dict__) # {'name': 'Jello'}
    #print(obj.__getattribute__) # <method-wrapper ...>
    #print(obj.__hash__) # <method-wrapper ...>
    #print(obj.__reduce__) # <method-wrapper ...>
    #print(obj.__setattr__) # <method-wrapper ...>
    #print(obj.__delattr__) # <method-wrapper ...>
    #print(obj.__new__) # <method-wrapper ...>
    #print(obj.__subclasshook__) # <method-wrapper ...>
    #print(obj.__weakref__) # None
    # I didn't expect this to be defined on 'object' anyway
    #print(obj.__getattr__) # AttributeError


def inspect_type():
    """
    When inspecting a type (class) object, dir() returns the attributes defined on the class and those of its base classes:
    - 'class_property'
    - 'say_hello'
    - everything defined on 'object'
    """
    obj = MyClass("Jello")
    #print(dir(MyClass))
    #print(MyClass.__class__) # <type 'type'> This must be a metaclass object
    #print(MyClass.__dict__)
    print(MyClass.__dict__.__dict__)
    #print(MyClass.__weakref__) # <attribute '__weakref__' ...>


if __name__ == "__main__":
    #inspect_oldclass_instance()
    #inspect_instance()
    inspect_type()