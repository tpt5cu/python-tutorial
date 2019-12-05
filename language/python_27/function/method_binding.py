# https://stackoverflow.com/questions/11949808/what-is-the-difference-between-a-function-an-unbound-method-and-a-bound-method - these notes are
# deceptively technical
# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy - see callable section at top. Has built-in function attributes


'''
TLDR: all of these notes talk about the internal implementation of fucntions vs methods and the metadata that makes using them possible. I probably
won't need this stuff much
- Even better: desciptors (gasp) do the real work of making everything happen
'''


'''
A function object is created by a def statement or a lambda expression. When a function appears within the body of a class statement, it is
transformed into an "unbound method" (only in Python 2. Python 3 doesn't have unbound methods).
- Invoking an unbound method from a class instance transforms it into a bound method. A bound method merely supplies the class instance to itself as
  the first parameter, which is conventionally called "self"
'''


class CoolClass(object):

    def cool_method(self):
        print("such a cool method")


def examine_unbound_method_attributes():
    """
    - im_self (i.e. __self__): None
    - im_class: the class which the method was created from
    - im_func: the original function object which is accessible a variety of ways
    """
    m = CoolClass.cool_method 
    print(dir(m))
    print(m) # <unbound method CoolClass.cool_method>
    # The method is unbound, so by definition __self__ is None
    print(m.im_self) # None
    # True for compatibility reasons
    print(m.im_self is m.__self__) # True
    print(m.im_class) # <class '__main__.CoolClass'>
    print(m.im_func) # <function cool_method at ...>


def examine_bound_method_attributes():
    """
    - im_self: the instance that called the method
    - im_class: same as above
    - im_func: same as above
    """
    obj = CoolClass()
    m = obj.cool_method
    print(m) # <bound method CoolClass.cool_method of <__main__.CoolClass object at ...>>
    # The method is bound, so by definition __self__ is the invoking instance
    print(m.im_self) # <__main__.CoolClass object at ...>
    # True for compatibility reasons
    print(m.im_self is m.__self__) # True
    print(m.__self__ is obj) # True
    print(m.im_class) # <class '__main__.CoolClass'>
    print(m.im_func) # <function cool_method at ...>
    print(CoolClass.cool_method.im_func is obj.cool_method.im_func) # True


def function_vs_unbound_method():
    '''
    The primary difference is that an unbound method knows which class it is bound to
    - __class__: the class/type of the the object it was referenced from
    - im_class: the class of the instance (for bound methods) or the class that the method was referenced from (for unbound methods)
    '''
    ubm = CoolClass.cool_method 
    print(ubm) # <unbound method CoolClass.cool_method>
    f = CoolClass.__dict__['cool_method']
    print(f) # <function cool_method at ...>
    print(ubm.__class__) # <type 'instancemethod'>
    print(ubm.im_class) # <class '__main__.CoolClass'>
    print(f.__class__) # <type 'function'>
    # Function objects of course have no associated class. This distinction between functions and unbound doesn't seem that useful. No wonder
    # unbound methods were removed in Python 3
    #print(f.im_class) # AttributeError


if __name__ == "__main__":
    #examine_unbound_method_attributes()
    #examine_bound_method_attributes()
    function_vs_unbound_method()