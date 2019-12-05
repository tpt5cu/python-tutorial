# https://docs.python.org/2/library/functions.html#getattr
# https://stackoverflow.com/questions/19123707/why-use-setattr-and-getattr-built-ins
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute - __getattr__() and __getattribute__() are
# unique
# https://stackoverflow.com/questions/30961069/what-is-the-python-attribute-get-and-set-order - attribute lookup process, nice graph!


'''
Often, getattr() is the same as regular old '.' syntax. However, what happens if I want to access an attribute on an object, but I don't know actual
attribute name? I need getattr()!

__getattr__() and __getattribute__() are methods that CAN be defined in a class. They are not the same as the built-in getattr() function. These two
methods allow the programmer to define finer behavior for nonexistent attribute access than always raising an AttributeError
- __getattr__(): invoked when Python discovers that the attribute that's being looked up actually doesn't exist on the object
- __getattribute__(): always invoked anytime there is any attribute access on an object. Very powerful and easy to mess up
- See attribute_lookup.py notes for better explanation of these two functions
'''


class Foo(object):

    name = 'Class property!'
    
    def __init__(self):
        self.name = 'Douglas'

    def __getattribute__(self, a):
        #return self.__getattribute__(a) # Infinite recursion b/c the method keeps calling itself!
        print('Hello from custom __getattribute__(): ' + a) # Now every attribute access will print this!
        return object.__getattribute__(self, a) # Almost always the correct way implement this method


def attribute_in_variable():
    foo = Foo()
    x = 'name'
    print(getattr(foo, x)) # Douglas


def get_nonexistent_attribute():
    '''Provide a default value to return, otherwise accessing a nonexistent attribute raises an AttributeError'''
    foo = Foo()
    #getattr(foo, 'thing') # AttributeError
    print(getattr(foo, 'thing', 'default!')) # default!


def attribute_lookup_order():
    foo = Foo()
    #print(foo.name) # Douglas
    print(dir(foo))
    #print(foo.__members__)


def get_factory_function():
    f_factory = getattr(__builtins__, 'float')
    f = f_factory('1.3')
    print(type(f)) # <type 'float'>
    print(f) # 1.3


if __name__ == '__main__':
    #attribute_in_variable()
    #get_nonexistent_attribute()
    #attribute_lookup_order()
    get_factory_function()