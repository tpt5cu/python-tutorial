# https://stackoverflow.com/questions/11949808/what-is-the-difference-between-a-function-an-unbound-method-and-a-bound-method/26943327
# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy - see callable section at top


"""
A function object is created by a def statement or a lambda expression. When a function appears within the body of a class statement, it is
transformed into an "unbound method" (only in Python 2. Python 3 doesn't have unbound methods).
- Invoking an unbound method from a class instance (i.e object) transforms it into a bound method. A bound method merely supplies the class instance
  to itself as the first parameter, which is conventionally called "self"
"""


class CoolClass(object):

    def cool_method(self):
        print("such a cool method")


def examine_unbound_method_attributes():
    """
    - im_self (i.e. __self__): None
    - im_class: the class which the method was created from
    - im_func: the original function object which does not appear to be accessible by itself without use of the class or a class instance
    """
    m = CoolClass.cool_method 
    print(dir(m))
    print(m) # <unbound method CoolClass.cool_method>
    print(m.im_self)  # The method is unbound, so by definition __self__ is None
    print(m.im_self is m.__self__) # True for compatibility reasons
    print(m.im_class) # <class '__main__.CoolClass'>
    print(m.im_func) # <function cool_method>


def examine_bound_method_attributes():
    """
    - im_self: the instance that called the method
    - im_class: same as above
    - im_func: same as above
    """
    obj = CoolClass()
    m = obj.cool_method
    print(m) # <bound method CoolClass.cool_method>
    print(m.im_self)  # The method is bound, so by definition __self__ is the invoking instance
    print(m.im_self is m.__self__) # True for compatibility reasons
    print(m.__self__ is obj) # True
    print(m.im_class) # <class '__main__.CoolClass'>
    print(m.im_func) # <function cool_method>
    print(CoolClass.cool_method.im_func is obj.cool_method.im_func) # True


if __name__ == "__main__":
    #examine_unbound_method_attributes()
    examine_bound_method_attributes()