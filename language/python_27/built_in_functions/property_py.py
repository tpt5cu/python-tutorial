# https://docs.python.org/2/library/functions.html#property
# https://www.python-course.eu/python3_properties.php


"""
The Pythonic way to handle attributes is to make them public or use properties. Avoid manual getter and setter methods to make attributes private.
- If a property includes no setter, then it is read-only
- If a property includes no getter, then it doesn't exist! Silly!
- If a property includes no deleter, then it can't be deleted
"""


class NoEncapsulation(object):
    """
    This implementation is elegant and Pythonic, but there is indeed no data encapsulation. The Python solution to this is properties. Properties are
    a high-level concept that is made possible by the descriptor protocol.
    """
    def __init__(self, x):
        self.x = x


class UndecoratedPropertyExample(object):
    """
    There is a class attribute called "value" that is also a property. I show 3 ways of handling the control of an instance attribute through the
    property.
    """
    def __init__(self, val):
        """Use the setter in the initializer to apply all validation logic easily."""
        self.swell_setter(val)

    def nice_getter(self):
        """
        - If I try to access an instance attribute called "value" that is shadowed by the class attribute "value", infinite recursion will occur for
          the same reasons as in swell_setter().
        """
        print("Inside nice_getter")
        #return self.value # Infinite recursion
        #return self.__dict__["value"] # clumsy
        return self.__value

    def swell_setter(self, data):
        """
        - If I try to assign an instance attribute called "value" that is shadowed by the class attribute "value", infinite recursion will occur with
          dot access because 1) Python looks up the attribute "value" 2) it sees that it is a data descriptor and so it takes precedence over an
          identically named instance attribute 3) it recurses into the swell_setter method.
        - To avoid this, I must use an entirely separate instance attribute name, or use __dict__ lookup which is clumsy. One convention is to use
          underscores.
        """
        print("Inside swell_setter")
        if data < 1:
            #self.value = 1 # Infinte recursion
            #self.__dict__["value"] = 1 # clumsy
            self.__value = 1
        elif data > 100:
            #self.value = 100 # Infinite recursion
            #self.__dict__["value"] = 100 # clumsy
            self.__value = 100
        else:
            #self.value = data # Infinite recursion
            #self.__dict__["value"] = data # clumsy
            self.__value = data

    # It's nice to put class attributes at the top, but I can't because the methods need to be defined first. Could put a deleter here to if I wanted
    value = property(nice_getter, swell_setter)


def examine_undecorated_property_example():
    obj = UndecoratedPropertyExample(-11)
    # accessing a property, but it looks like an instance attribute (because underneath it is using an instance attribute)
    print(obj.value) # 1
    obj2 = UndecoratedPropertyExample(99)
    print(obj2.value) # 99
    print(obj.value) # 1
    # The attribute cannot be deleted since it is a non-deletable property!
    #del obj.value


class DecoratedPropertyExample(object):
    """The importance of distinguishing the property name from the instance attribute name still holds when using decorators."""
    def __init__(self, data):
        #self.__thingy = data # This doesn't seem right. I'm ignoring the property entirely
        # Only raises an AttributeError if there IS no setter. Otherwise, this is correct
        self.zoowack = data

    @property
    def zoowack(self):
        """This IS the getter"""
        print("Hello from zoowack getter")
        return self.__thingy

    @zoowack.setter
    #def whatever(self, data): # this function name doesn't match the property so this won't work
    def zoowack(self, data):
        """When using the decorator, the function NAME must ALSO match the property exactly."""
        print("Hello from zoowack setter")
        if len(data) < 1:
            self.__thingy = "I"
        elif len(data) > 5:
            self.__thingy = "abcde"
        else:
            self.__thingy = data

    @zoowack.deleter
    #def however(self):
    def zoowack(self):
        """When using the decorator, the function name must also match the property exactly."""
        print("Hello from zoowack deleter")
        del self.__thingy
            

def examine_decorated_property_example():
    obj = DecoratedPropertyExample("wishes")
    print(obj.zoowack) # abcde
    obj.zoowack = "rice"
    print(obj.zoowack) # rice
    del obj.zoowack # Only throws AttributeError when there IS not deleter


class ReadOnlyAttribute(object):
    """There is an instance attribute "__my_atr". It is accessed through the property "my_atr". Since "my_atr" is read-only, so is "__my_atr."""
    def __init__(self, data):
        self.__my_atr = data

    @property
    def my_atr(self):
        return self.__my_atr


def examine_readonly_attribute():
    obj = ReadOnlyAttribute("Permanent")
    print(obj.my_atr) # Permanent
    #obj.my_atr = "something else" # AttributeError


if __name__ == "__main__":
    #examine_undecorated_property_example()
    #examine_decorated_property_example()
    examine_readonly_attribute()