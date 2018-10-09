# https://stackoverflow.com/questions/980249/difference-between-dir-and-vars-keys-in-python
# https://stackoverflow.com/questions/25440694/whats-the-purpose-of-dictproxy
# https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a


class Superclass:

    superclass_attribute = "I'm a class attribute of the superclass"

    def superclass_method(self):
        print("hello from superclass method")


class Subclass:

    subclass_attribute = "I'm a class attribute of the subclass"

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def subclass_method(self):
        print("Hello from subclass method")


def use_vars():
    """Strictly, vars() returns the __dict__ attribute of a module, class, or object. It throws a type error if the
    argument does not have the __dict__ attribute. A class has a distinct namespace, and each instance of that class
    has a distinct namespace. These namespaces are represented by the __dict__ attribute.

    1) For an object, __dict__ is a dictionary that contains all of the attributes defined on the object itself. This
    does not include attributes of the class (e.g. methods and class attributes)
    2) For a class, __dict__ is actually of the type mappingproxy.
    3) For a module ...
    """
    obj = Subclass("Austin", "Red")
    print(vars(obj))
    print(obj.__dict__)
    if vars(obj) == obj.__dict__:
        print(True)
    print(type(vars(obj)))
    """This throws a TypeError because built-in types do not have a __dict__ attribute."""
    # print(vars(0))


def use_dir():
    """dir() does more than vars(). It returns a LIST of defined names in a namespace. This refers to the object's
    attributes, its class's attributes, and recursively the attributes of its class's base classes.
    However, this list only contains the attributes, not their values.
    """
    obj = Subclass("David", "Blue")
    print(dir(obj))
    print(type(dir(obj)))
    """There is no link to the values that go with the attributes. When I look up an element inside of the list 
    returned by dir(), the element is just a string!"""
    print(type(dir(obj)[-3]))


if __name__ == "__main__":
    # use_vars()
     use_dir()
