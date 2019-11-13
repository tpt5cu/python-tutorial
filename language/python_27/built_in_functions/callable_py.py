# https://docs.python.org/2/library/functions.html#callable
# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy
# https://docs.python.org/2.7/reference/expressions.html#calls


"""
Callable objects:
- classes
- class instances (i.e. objects) provided they have defined a __call__() method
- functions
- methods

The callable concept is simple. Its underlying implementation details are not. See function notes
"""


class CallableObject(object):

    def __call__(self):
        print("I was called")

    def cool_method(self):
        print("This is a cool method")


def use_callable():
    """
    callable() returns True if the object appear callable, otherwise False. Just be this function return True doesn't mean the object can be
    successfully called
    """
    print(callable(CallableObject)) # True
    obj = CallableObject() # class objects are of course always callable
    print(callable(obj)) # True
    obj() # this object has __call__, so it is also callable
    print(callable(5)) # False
    print(callable([])) # False


def examine_method_attributes():
    obj = CallableObject()
    print(dir(obj.cool_method))
    # __self__ is merely the instance object of a method
    print(obj.cool_method.__self__ is obj) # True
    # These are the same for forward compatibility
    print(obj.cool_method.__self__ is obj.cool_method.im_self) # True

    print(CallableObject.cool_method)
    print(obj.cool_method.im_func)
    print(obj.cool_method.im_func is CallableObject.cool_method)
    

if __name__ == "__main__":
    use_callable()