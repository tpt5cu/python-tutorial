# https://docs.python.org/2/library/functions.html#type


def get_class_object():
    """type(<obj>) returns the type object (i.e. a class object) that created the instance object."""
    l = []
    print(type(l)) # <type 'list'>


def define_class_object():
    """
    type(<name>, <bases>, <dict>) is essentially a dynamic 'class' statement. It also returns a class object. <name> is the name of the class, the
    <bases> tuple contains bases classes (order matters), and <dict> contains a mapping of class attributes to their values.
    """
    # These two class definitions are equivalent. However, even though the class definitions are identical, they have absolutely no relationship to
    # one another because 1) they are two different class/type objects in memory and 2) they don't define __cmp__() or __eq__() so any kind of
    # identity comparison will check their memory locations
    class A(object):
        val = 1
    B = type('A', (object,), {'val': 1})

    a = A()
    b = B()
    print(type(a) is type(b)) # False
    print(type(a) == type(b)) # False
    print(type(a)) # <class '__main__.A'>
    print(type(b)) # <class '__main__.A'>
    print(A.__dict__ == B.__dict__) # False
    print(A.__dict__.keys() == B.__dict__.keys()) # True because the keys are strings
    # False because the values in each list are objects, who will then be compared memory-wise to their respective counterparts
    print(A.__dict__.values() == B.__dict__.values()) 




if __name__ == '__main__':
    #get_class_object()
    define_class_object()