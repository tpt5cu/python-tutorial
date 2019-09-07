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
- If a regular old Python class defines at least 1 of 3 functions, __get__(), __set__(), and/or __delete__(), then instances of that class follow the
  descriptor protocol and are called "descriptors".

The descriptor protocol is low-level. High-level structures like Python properties, bound and unbound methods, static methods, class methods, and
super() are all based on the descriptor protocol.

When Python looks up an attribute, it checks to see if the attribute is actually a descriptor object. If it is, Python MIGHT invoke the descriptor
object's behavior instead of reading/writing the attribute normally, depending on the precedence of the descriptor in the attribute look-up process.
The override order of data descriptors vs. non-data descriptors vs. regular attributes in Python's attribute look-up process is very important.
- If an object implements __get__() and __set__(), it is a "data descriptor"
    - For an instance object, a data descriptor (which exists as a class attribute) will take precedence over an instance attribute with the same name
      or a non-data descriptor with the same name
- If an object implements only __get__(), then it is a "non-data descriptor"
    - For an instance object, an instance attribute will take precedence over a non-data descriptor attribute with the same name.

A descriptor is useful because it allows me to implement custom behavior on top of regular-plain-old attribute read/write access. Normally, attributes
are just stored in an object's __dict__. But what happens if I start out using plain-old attributes, and then decide later on that I need to add
additional behavior? Perhaps I want to validate some input before I set an attribute to be the input. Descriptors allow me to implement that behavior
without modifying any existing code at all! That isn't possible in Java, which is why I was taught to always write getter() and setter() methods for
every class, no matter how simple.
"""


class BadDivider(object):

    def __init__(self, divisor):
        assert divisor != 0
        self.divisor = divisor

    def divide(self, dividend):
        return dividend / self.divisor


# Since instances of the Divisor class will be instantiated inside of other classes, this class must be defined first in the file!
class Divisor(object):
    """
    The Divisor class will create descriptor objects. These function signatures are required by the descriptor protocol, but the names of the
    parameters may be whatever I want (of course). A descriptor object is supposed to encapsulate 1 and only 1 attribute of another class.
    """
    def __init__(self):
        print("Created Divisor descriptor!")
        # I don't want any class-level state to be stored in this object because it's confusing.
        #assert divisor != 0
        #self.divisor = divisor

    def __get__(self, instance, owner):
        """
        'self' refers to this descriptor object, 'instance' refers to the object that has this descriptor as an attribute, and 'owner' refers to the
        class that owns the descriptor. Descriptor objects are defined as class attributes ONLY. 'instance' could be None if this descriptor were
        referenced from a class as opposed to an instance.
        - The use of 'instance.__dict__' is how to avoid going through Python's automatic attribute look-up process that occurs with '.' notation.
          That's why I can avoid infinite recursion.
        """
        print("Getting descriptor value!")
        # This line will cause infinte recursion. The instance looks up "divisor", which turns out to be a data descriptor, which calls its __get__()
        # method, which looks up "divisor" on the instance, etc.
        #return instance.divisor
        # If an instance did not have a "divisor" property defined on it, this would return None. In that way, the __dict__ of an instance is
        # different from a regular dictionary because a regular dictionary would throw a KeyError. However, no instance should ever lack this
        # attribute because __set__() will assign the instance this attribute when it is created.
        return instance.__dict__["divisor"]
        # This is line is probably not want I want, because 1) it would return the integer divisor stored in the descriptor object itself and 2) it
        # would imply that there is some shared state stored in the descriptor object, which there isn't by design.
        #return self.divisor


    def __set__(self, instance, value):
        """
        'self' referes to the descriptor object (which is an instance of the Divisor class), 'instance' refers to the object that is looking up the
        attribute that is this descriptor, 'value' is the value that this descriptor will be set to.
        """
        print("Setting descriptor value!")
        if value == 0:
            raise Exception("The divisor value cannot be 0!!!")
        # This line will cause infinite recursion. Python looks for "divisor" defined on the instance, and finds that it is a data descriptor on the
        # class. Since the descriptor is trying to be set to a value, its __set__() method gets called, which triggers the instance to look up the
        # divisor, etc.
        #instance.divisor = value
        # This line does what I want because it bypasses the normal Python attribute look-up.
        instance.__dict__["divisor"] = value
        # This line will change the integer value stored inside this object. That's probably not what I want.
        #self.divisor = value 


# Pretend that this class is a refactor of the BadDivider. The class API hasn't changed, but descriptors are now used under the hood.
class GoodDivider(object):

    # This invokes the __init__() method of the descriptor object, nothing else. Class attributes are evaluated exactly one time when the class object
    # is created. In other words, this line doesn't run everytime a GoodDivider instance is created.
    divisor = Divisor()


    def __init__(self, divisor):
        # This invokes the __set__() method of the descriptor. The __set__() method of the descriptor will eventually add an integer "divisor"
        # attribute to the __dict__ of this instance.
        self.divisor = divisor


    def divide(self, dividend):
        return dividend / self.divisor


def compare_descriptor_across_instances():
    """
    Isn't it cool? There is exactly one object that manages all validation code for the "divisor" attribute, AND the "divisor" attribute looks like a normal attribute
    (because it is), AND the divisor descriptor object could store state within itself if I wanted!
    """
    gd1 = GoodDivider(10)
    print("gd1.divisor value: " + str(gd1.divisor)) # 10
    print(gd1.divide(100)) # 10
    gd2 = GoodDivider(5)
    print("gd2.divisor value: " + str(gd2.divisor)) # 5
    print(gd2.divide(100)) # 20
    print("gd1.divisor value again: " + str(gd1.divisor)) # 10
    print(gd1.divisor is gd2.divisor) # False


def use_descriptor_validation():
    """This shows one use case for descriptors: validating the getting and setting of regular old properties."""
    bd = BadDivider(2)
    bd.divisor = 0 # no validation here!
    #bd.divide(100) # ZeroDivisionError
    gd = GoodDivider(2)
    gd.divisor = 0 # Raises an exception, like it should!
    gd.divide(100)


if __name__ == "__main__":
    #compare_descriptor_across_instances()
    use_descriptor_validation()
