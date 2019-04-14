"""
https://realpython.com/python3-object-oriented-programming/
https://stackoverflow.com/questions/6578487/init-as-a-constructor
https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self
"""

#class Animal:
class Animal(object):
    """
    Python 2.x notation has different class definition syntax. 'object' represents the superclass of this class. In Python 3.x this is implicit.

    A 'constructor' does slightly different things depending on the language, so some don't like to call __init__() the constructor per se. __init__()
    is called after the instance has been created by __new__(). __init__() receives the arguments that were passed to the class constructor expression
    (i.e. Animal() in this case). __init__() actually creates AND initializes custom attributes on an object. Custom attributes are those that all
    objects DON'T already posses.

    Surprisingly, there are no 'real' methods in Python. ANY method (i.e. a function that belongs to class) is simply a regular function with special
    conditions. These special condition are that: 1) when a method is called, it is implicitly passed an object instance as its first parameter,
    conventionally called 'self'. 'self' IS an object that is an instance of the class to which the function ALSO belongs. 2) when any method is
    defined, it must explicitly have 1 parameter (conventionally called 'self') which represents that object instance that is implicitly passed to it.

    This is long-winded to say, so these kinds of functions are called methods in Python. 
    """
    def __init__(self, name="George", species="none", age=0):
        self.name = name
        self.species = species
        self.age = age

    def bad_method(name):
        """
        This method doesn't have the 'self' parameter as the first parameter. As a result, 'name' is treated as 'self'. When this method is called, no
        arguments can be passed to it because 'name' is already occupied by an object instance that is implicitly passed. Furthermore, calling this
        method without arguments will actually change the instance's name property to Austin. Confusing!
        """
        name.name = "Austin"


def create_instances():
    """ These objects have identical data inside of them, but they are indeed different objects. """
    i1 = Animal()
    i2 = Animal()
    print(i1.name + " " + str(id(i1)))
    print(i2.name + " " + str(id(i2)))


def bad_method_test():
    """Isn't this confusing?"""
    creature = Animal()
    # creature.rename("Joe")
    creature.bad_method()
    print(creature.name)


if __name__ == "__main__":
    # create_instances()
    bad_method_test()
