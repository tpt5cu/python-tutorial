# https://docs.python.org/2.7/howto/descriptor.html
# https://docs.python.org/2.7/reference/datamodel.html#implementing-descriptors
# http://martyalchin.com/2007/nov/23/python-descriptors-part-1-of-2/


"""
At a high level, a descriptor is a regular Python object that encapsulates a class attribute or an instance attribute so that additional logic can be
defined beyond normal property accesses on objects. Descriptor objects are similar to JavaScript getters and setters, C# properties, and Java getters
and setters.

In order for a descriptor object to be used as a descriptor (and not just as a regular Python object that happens to have some methods), the
descriptor object must be "owned" by a class. That is, the descriptor object must be assigned as a value of some attribute of the owner class. 
- A descriptor will NOT work if it is assigned as a value of an instance attribute. If that happens the descriptor will behave like a normal Python
  object, which is confusing because this normal Python object will have the same attributes as if it were a descriptor!

The descriptor protocol states that if 1) a regular Python class defines a special set of method signatures and 2) an instance of that class is
assigned as an attribute of another class, then the instance will behave as a descriptor object. 
- If a regular old Python class defines just __get__(), it is a non-data descriptor
- If a regular old Python class defines __get__() and (__set__() and/or __delete__()), it is a data descriptor

The descriptor protocol is low-level. High-level structures like Python properties, bound and unbound methods, static methods, class methods, and
super() are all based on the descriptor protocol.

Python's attribute look-up process is complicated. I cannot accurately state how the internal implementation works. I can only state the precedence
order of the look-up operation:
- Data descriptors come before instance attributes
- Instance attributes take precedence over non-data descriptors
- There cannot be a conflict with a regular class attribute! Read on to see why!
- __getattr__() has the lowest priority
    - __getattr__() is NOT part of the descriptor protocol, but it can influence attribute look-up, so it is worth mentioning

A descriptor is useful because it allows me to implement custom behavior on top of regular-plain-old attribute read/write access. Normally, attributes
are just stored in an object's __dict__. But what happens if I start out using plain-old attributes, and then decide later on that I need to add
additional behavior? Perhaps I want to validate some input before I set an attribute to be the input. Descriptors allow me to implement that behavior
without modifying any existing code at all! That isn't possible in Java, which is why I was taught to always write getter() and setter() methods for
every class.
"""


class BadDivider(object):

    def __init__(self, divisor):
        assert divisor != 0
        self._divisor = divisor

    def divide(self, dividend):
        return dividend / self._divisor


# Since instances of the Divisor class will be instantiated inside of other classes, this class must be defined first in the file!
class Divisor(object):
    """
    The Divisor class will create descriptor objects. These function signatures are required by the descriptor protocol. A descriptor object is
    supposed to encapsulate 1 and only 1 attribute of another class.

    Since the data descriptor will intercept every access on the instance, I can technically use whatever attribute name I want.
    - In this case I use "_nonsense_value" to illustrate the point
    """
    def __init__(self):
        print("Created Divisor descriptor!")
        # I don't want any class-level state to be stored in this object because it's confusing.
        #assert divisor != 0
        #self._nonsense_value = divisor
        pass

    def __get__(self, instance, owner):
        """
        'self' refers to this descriptor object, 'instance' refers to the object that has this descriptor as an attribute, and 'owner' refers to the
        class that owns the descriptor. Descriptor objects are defined as class attributes ONLY. 'instance' could be None if this descriptor were
        referenced from a class as opposed to an instance.
        - The use of 'instance.__dict__' is how to avoid infinte recursion. The dot access still invokes object.__getattribute__(), but the instance's
          __dict__ is returned instead of the data descriptor. Accessing the instance's __dict__ has nothing to do with any descriptor, so __get__()
          won't be invoked recursively
        """
        #print("Getting descriptor value!")
        # This line will cause infinte recursion. The instance looks up "_divisor", which turns out to be a data descriptor, which calls its __get__()
        # method, which looks up "_divisor" on the instance, and the cycle repeats.
        #return instance._divisor
        # If the instance does not actually have the "_nonsense_value" attribute, a KeyError will be raised
        return instance.__dict__["_nonsense_value"]
        # This is line is probably not want I want, because 1) it would return the integer divisor stored in the descriptor object itself and 2) it
        # would imply that there is some shared state stored in the descriptor object, which there isn't by design.
        #return self._nonsense_value

    def __set__(self, instance, value):
        """
        'self' referes to the descriptor object (which is an instance of the Divisor class), 'instance' refers to the object that is looking up the
        attribute that is this descriptor, 'value' is the value that this descriptor will be set to.
        """
        #print("Setting descriptor value!")
        if value == 0:
            raise Exception("The divisor value cannot be 0!!!")
        # This line will cause infinite recursion. Python looks for "_divisor" defined on the instance, and finds that it is a data descriptor on the
        # class. Since the descriptor is trying to be set to a value, its __set__() method gets called, which triggers the instance to look up the
        # divisor, and the cycle repeats
        #instance._divisor = value
        # This line does what I want because it does not access the descriptor
        instance.__dict__["_nonsense_value"] = value
        # This line will change the integer value stored inside this object. That's probably not what I want.
        #self._nonsense_value = value 


# Pretend that this class is a refactor of the BadDivider. The class API hasn't changed, but descriptors are now used under the hood.
class GoodDivider(object):

    # This invokes the __init__() method of the descriptor object, nothing else. Class attributes are evaluated exactly one time when the class object
    # is created. In other words, this line doesn't run everytime a GoodDivider instance is created.
    _divisor = Divisor()

    def __init__(self, divisor):
        # This invokes the __set__() method of the descriptor. The __set__() method of the descriptor will eventually add an integer "_nonsense_value"
        # attribute to the __dict__ of this instance.
        self._divisor = divisor

    def divide(self, dividend):
        return dividend / self._divisor


def compare_descriptor_across_instances():
    """
    Isn't it cool? There is exactly one object that manages all access for "_divisor" attribute across all instances, AND the "_divisor" attribute
    looks like a normal attribute
    """
    gd1 = GoodDivider(10)
    print("gd1.divisor value: " + str(gd1._divisor)) # 10
    print("100/10 is {}".format(gd1.divide(100))) # 10
    gd2 = GoodDivider(5)
    print("gd2.divisor value: " + str(gd2._divisor)) # 5
    print(gd2.divide(100)) # 20
    print("gd1.divisor value again: " + str(gd1._divisor)) # 10
    print(gd1._divisor is gd2._divisor) # False


def use_descriptor_validation():
    """This shows one use case for descriptors: validating the getting and setting of regular old properties."""
    bd = BadDivider(2)
    bd._divisor = 0 # no validation here!
    #bd.divide(100) # ZeroDivisionError
    gd = GoodDivider(2)
    gd._divisor = 0 # Raises an exception, like it should!
    gd.divide(100)


if __name__ == "__main__":
    #compare_descriptor_across_instances()
    use_descriptor_validation()