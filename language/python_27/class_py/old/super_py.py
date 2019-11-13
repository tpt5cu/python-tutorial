"""
https://realpython.com/python-super/
https://www.python.org/dev/peps/pep-3135/ - Python 2 super call
"""

"""
- The super() function allows Python to support inheritance.
- By itself, super() returns a temporary instance of the superclass
- In Python 2, super() MUST be called as super(<ThisClass>, self)
    - In Python 3, this is done implicitly with super() (no arguments)

This file is an example of single inheritance. Python also supports multiple inheritance.
"""


class SuperClass(object):


    def __init__(self, name):
        self.name = name

    
    def set_name(self, name):
        self.name = name


    """
    If I comment this out, the SubClass instance will no longer have this method
    """
    def print_name(self):
        print("My name is " + self.name)


class SubClass(SuperClass):


    def __init__(self, name, age):
        #super().__init__(name) # TypeError: super() takes at least 1 argument (0 given)
        #super(SuperClass, self).__init__(name) # Wrong class passed to super()
        """
        This call is valid. However, the "age" attribute will NOT be assigned to an instance of SubClass with this call. Also, super() DOES return an
        instance of the superclass, but __init__() doesn't return anything. That's why the return value of the below statement is None.
        """
        super(SubClass, self).__init__(name) # This works
        """
        Even though it doesn't look like the above call and this call are related they are. Actually, since "self" is passed to super(), that's
        proof that the super() line and this line are connected
        """
        self.age = age


    """ 
    There is no need to redefine this method, unless I'm changing it or adding functionality to it.
    """
    #def set_name(self, name):
    #    self.name = name


    def set_age(self, age):
        self.age = age


    """ 
    There is no need to redefine this method (aka perform method overriding), unless I'm changing it or adding functionality to it.
    """
    def print_name(self):
        print("My name is " + str(self.name) + " Chang")


    def print_age(self):
        print("My age is " + str(self.age))


def use_subclass():
    sub = SubClass("Austin", 24)
    sub.print_name() # Austin Chang
    sub.print_age() # 24
    sup = super(sub.__class__, sub) # get the superclass
    sup.print_name() # Austin


if __name__ == "__main__":
    use_subclass()