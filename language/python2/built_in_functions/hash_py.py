# https://docs.python.org/2/library/functions.html#hash
# https://docs.python.org/2.7/reference/datamodel.html#object.__hash__ - relationship between __hash__, __eq__, immutability, etc.
# https://docs.python.org/2.7/glossary.html#term-hashable - hashable definition
# https://stackoverflow.com/questions/34402522/difference-between-hash-and-id - Python 3 explanation, but nice intro


"""
All objects have identity and value.
- The value of an object might only be its id() value but that's okay
Some objects also need a hash value, which is sublty different from both of those other properties.

Why do I care about how the hash() function works? Because only hashable objects can be used in set, frozenset, and as dict keys. These notes are for
Python 2 only. Python 3 is slightly different.

In order to be hashable, an object must:
- Have a hash value which never changes during the lifetime of the object
    - Thus, mutable objects must retain the hash value based on id(), otherwise hashing based on mutable attributes would change the hash value itself
- Hashable objects which compare equal must have the same hash value
    - If objects are compared via identity (default implementation), then hashing based on identity is also valid (default implementation) 
    - If objects are compared via custom comparison (__cmp__() or __eq__()), then hashing based on identity is invalid
        - Therefore, mutable objects that ALSO define custom comparison are never hashable. Mutable objects that don't define custom comparison ARE
          hashable
            - Therefore, user-defined classes are hashable by default: they compare unequal with everything except themselves and their hash value is
              derived from their id()
        - Also, immutable objects are ALWAYS hashable because they can define custom comparison AND hash based on custom attributes

Two unequal objects ARE allowed to have the same hash value!

An object can exist in 3 states with regard to hashing:
1) It is explicitly unhashable, and the interpreter will recognize it as such. This is valid.
    - It can be an unhashable built-in mutable type
    - It can be defined as explicitly unhashable
2) It is not explicitly unhashable, but in reality is not correctly hashable. Treating it like it is hashable could raise subtle bugs. This is
   invalid.
    - It defines __cmp__() or __eq__() but not __hash__()
        - This would violate a property of being correctly hashable: objects which compare equal must have the same hash value. Such invalid objects
          could compare equality, but would retain the __hash__() implementation based on id(), so they would never have the same has id hash value
    - It defines __hash__() but not __cmp__() or __eq__()
        - Similar reasoning as above. Such objects could have the same hash value, but would never compare equal
    - The class defines mutable objects and implements __cmp__() or __eq__()
        - See above
3) It is hashable and can be used anywhere a hashable object is expected. This is valid
    - It can be hashable based on id() (default behavior)
    - It can be hashable based on custom implementation
"""

class NotHashable(object):
    """
    A class can explicitly mark itself as unhashable with the shown syntax. The alternative is to define a custom __hash__() function which will raise
    a TypeError on purpose. This is the only way to tell the interpreter that instances of this class are 1) not usable in hashed collections and 2)
    cannot be hashed at all. Including or not including __cmp__ or __eq__ has no bearing on this.
    """

    def __init__(self, num):
        self.num = num

    __hash__ = None


def examine_not_hashable():
    obj1 = NotHashable(3)
    obj2 = NotHashable(3)
    #print(hash(obj1)) # TypeError: unhashable type
    #my_dict = {obj1: "val"} # TypeError: unhashable type


class InvalidHashable(object):
    """There a few ways to define a class that will create invalid objects with regard to hashing"""

    def __init__(self, num):
        self.num = num

    def __cmp__(self, other):
        if self.num < other.num:
            return -1
        elif self.num == other.num:
            return 0
        else:
            return 1


def examine_invalid_hashable():
    """This is dangerous because the interpreter cannot tell me that I've written a bad implementation"""
    obj1 = InvalidHashable(6)
    obj2 = InvalidHashable(6)
    print(hash(obj1))
    print(obj1 == obj2) # True
    print(hash(obj1) == hash(obj2)) # False
    my_dict = {obj1: "val"}


def examine_hash():
    """__hash__ (and therefore hash(), which calls __hash__), returns an integer"""
    x = 2
    y = 2
    print(hash(x)) # 2
    print(hash(x) == hash(y)) # True


def compare_identity():
    """
    All objects have identity, as returned by the id() function. In CPython, id() returns an integer representing the memory address of the object
    (that's an implementation detail). 
    - "is" compares the identify of two objects
    - "==" uses "is" unless some custom __cmp__() or __eq__() method has been defined
    """
    a = 6
    b = 6
    print(id(a))
    print(id(a) == id(b)) # True
    print(a is b) # True
    print(a == b) # True


if __name__ == "__main__":
    #examine_not_hashable()
    examine_invalid_hashable()
    #examine_not_usable_in_hashed_collection()
    #examine_hash()
    #compare_identity()
    #compare_value()