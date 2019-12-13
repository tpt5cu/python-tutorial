# https://stackoverflow.com/questions/11949808/what-is-the-difference-between-a-function-an-unbound-method-and-a-bound-method - these notes are
# deceptively technical
# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy - see callable section at top. Has built-in function attributes


'''
TLDR: all of these notes talk about the internal implementation of fucntions vs methods and the metadata that makes using them possible. I probably
won't need this stuff
- Even better: desciptors (gasp) do the real work of making everything happen
- Invoking an function from a class instance object transforms it into a bound method. A bound method merely supplies the instance itself as the
  first parameter, which is conventionally called "self"
- A function will never be bound to a class object unless it is explicitly made into a class method
'''


class CoolClass(object):

    def cool_method(self):
        print('such a cool method')


def examine_bound_method_attributes():
    '''
    - im_self: the instance that called the method
    - im_class: same as above
    - im_func: same as above
    '''
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


if __name__ == "__main__":
    examine_bound_method_attributes()