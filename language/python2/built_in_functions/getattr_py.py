# https://docs.python.org/2/library/functions.html#getattr
# https://stackoverflow.com/questions/19123707/why-use-setattr-and-getattr-built-ins


"""
Often, getattr() is the same as regular old "." syntax. However, what happens if I want to access an attribute on an object, but I don't know actual
attribute name? I need getattr()!
"""

class Foo(object):
    
    def __init__(self):
        self.name = "Douglas"


def attribute_in_variable():
    foo = Foo()
    x = "name"
    print(getattr(foo, x)) # Douglas


def get_nonexistent_attribute():
    """Provided a default value to return, otherwise accessing a nonexistent attribute raises an AttributeError"""
    foo = Foo()
    #getattr(foo, "thing") # AttributeError
    print(getattr(foo, "thing", "default!"))


if __name__ == "__main__":
    #attribute_in_variable()
    get_nonexistent_attribute()