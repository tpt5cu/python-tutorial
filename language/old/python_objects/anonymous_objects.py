# https://stackoverflow.com/questions/652276/is-it-possible-to-create-anonymous-objects-in-python
# https://stackoverflow.com/questions/37161275/what-is-the-difference-between-simplenamespace-and-empty-class-definition
# https://www.programiz.com/python-programming/methods/built-in/type

from types import SimpleNamespace as _
from collections import namedtuple


def create_simplenamespace():
    """There is no anonymous object syntax in Python. Trying to create anonymous objects is hacky. Using simpleNamespace
    is the least hacky way of doing it.
    """
    obj1 = _(foo=1)
    obj1.random = "Whoa"
    print(obj1)
    obj2 = _(foo=2, bar="Yipee!")
    print(obj2)
    obj3 = _(foo=5, bar=4.0, boo=["list", "with", "strings"])
    print(obj3)


def create_namedtuple():
    """This approach isn't so good because I cannot add custom attributes on the fly.
    I can use namedtuple() in Python 2 because Simplenamespace doesn't exist. namedtuple() returns a new
    tuple SUBCLASS called <typename>. In this example, 'Thing' is a variable that references a class
    called 'MyCoolTuple' and 'obj' is an instantiation of 'MyCoolTuple'
    """
    Thing = namedtuple("MyCoolTuple", "field1 field2")
    obj = Thing(1, 2)
    # Throws AttributeError
    #obj.random = "Whoa"
    print(Thing)
    print(obj)


def create_new_type():
    """When passed a single argument, type() returns a type object. It returns the type (i.e. class object)
    of the passed object."""
    string = "I'm a string"
    print(type(string))
    """When passed 3 arguments, type() acts like a dynamic 'class' statement. It returns a new class object (see
    metaclassses notes)
    """
    thing = type("SuperCoolClass", (), {})
    thing.random = 4.556
    print(type(thing))
    print(vars(thing))
    print(thing)


if __name__ == "__main__":
    #create_Simplenamespace()
    #create_namedtuple()
    create_new_type()
