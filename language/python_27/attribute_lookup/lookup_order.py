# https://docs.python.org/2.7/howto/descriptor.html#definition-and-introduction - literal statement of attribute look-up order
# https://docs.python.org/2/reference/datamodel.html#special-method-lookup-for-old-style-classes - super-duper fine details not discussed in these
# notes 
# https://codesachin.wordpress.com/2016/06/09/the-magic-behind-attribute-access-in-python/ - somewhat useful summary
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute - __getattr__() and __getattribute__()


"""
From the docs: "For instance, a.x has a lookup chain starting with a.__dict__['x'], then type(a).__dict__['x'], and continuing through the base
classes of type(a) excluding metaclasses." See the dir_py.py notes for which attributes belong to the Python 'object'.
- So the default order of attribute look-up is:
    - __dict__ of the object instance
    - __dict__ of the class object
    - __dict__ of base classes according to __mro__
- If a descriptor is involved, the look-up process can change slightly:
    - data descriptors are referenced before instance attributes
    - instance attributes are referenced before non-data descriptors
    - non-data descriptors are referenced before class __dict__???. The link says that non-data descriptors come BEFORE regular old class attributes
- Additionally, certain methods CAN also change the attribute look-up process:
    - __getattribute__(): all new-style classes inherit from 'object'. Therefore, they all eventually call down to 'object.__getattribute__()' because
      I haven't figured out how to implement __getattribute__() without then calling down to 'object.__getattribute__()' eventually
    - __getattr__(): __getattribute__() will ALWAYS be called before this method. This method will be invoked ONLY if it is found in the inheritance
      hierarchy and the attribute that is being looked-up does not exist anywhere else (i.e. does not exist in the instance __dict__, the class
      __dict__, etc.)

In a nutshell here is the look-up order for an attribute:
1) Data-descriptors anywhere in the inheritance hierarchy
2) Instance attribute in the object itself
3) Non-data descriptors anywhere in the inheritance hierarchy
4) Regular class attributes in the inheritance hierarchy
"""


class OldClass():

    def __init__(self, name):
        self.name = name


class Bottom(object):

    class_prop = "Bottom class_prop"

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("Bottom: Hello my name is " + self.name)

    #def __getattr__(self, a):
    #    print("Hello from Bottom __getattr__()")
    #    return "Default value!"


class OtherBottom(object):

    class_prop = "OtherBottom class_prop"

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("OtherBottom: Hello my name is " + self.name)

    """
    If __getattribute__() is defined here, THIS function WILL be called for an attribute look-up on THIS class/a class instance.
    - THIS function MAY be called for attribute look-up on a subclass/subclass instance of THIS class. If Top invokes __getattribute__() on this base
      class (or a subclass of this base class), then THIS function will be invoked. However, if Top invokes the __getattribute__() defined on the
      'object', THIS function won't be called because it gets skipped in the inheritance hierarchy
    """
    def __getattribute__(self, a):
        print("Hello from OtherBottom __getattribute__()")
        return object.__getattribute__(self, a)
        #return getattr(self, a) # Infinite recursion
        #return getattr(self.__dict__, a) # Infintie recursion


class Top(OtherBottom, Bottom):

    class_prop = "Top class_prop"

    def __init__(self, name):
        super(Top, self).__init__(name)

    """
    Regardless of which way I choose to call __getattribute__, it always goes back to 'object' since 1) no other class implemented __getattribute__ or
    2) if they did implement it, they in turn call object.__getattribute__(). These all work fine. This is an example of how Python recursively searches
    the attributes of base classes during attribute look-up.
    """
    #def __getattribute__(self, a):
    #    print("Hello from Top __getattribute__()")
    #    #return OtherBottom.__getattribute__(self, a)
    #    #return Bottom.__getattribute__(self, a)
    #    #return super(Top, Top).__getattribute__(self, a)
    #    return super(Top, self).__getattribute__(a)
    #    #return object.__getattribute__(self, a)


def base_class_lookup():
    # __getattribute__() WILL be called from somewhere
    t = Top("Maggie")
    print(t.name)
    # __getattr__() will be called if it is defined, but only if it is defined, since 'object' does not implement it
    #print(t.age)


def instance_dict_lookup():
    """ '.' syntax and getattr() are equivalent """
    t = Top("Boyle")
    # __getattribute__() is STILL called because of t.__dict__ which is using "." syntax
    #print(t.__dict__["name"]) # Boyle
    # __getattr__() will never be called when an attribute is referenced this way
    #print(t.__dict__["age"]) # KeyError
    print(t.age)
    print(getattr(t, "age"))


if __name__ == "__main__":
    #base_class_lookup()
    instance_dict_lookup()