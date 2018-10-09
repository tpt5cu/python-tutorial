# https://stackoverflow.com/questions/4075190/what-is-getattr-exactly-and-how-do-i-use-it
# https://stackoverflow.com/questions/111234/what-is-a-callable-in-python

"""This method is very powerful and versatile"""


class Cat:

    def __init__(self, breed="Tabby", age=1, name="Amber", speed=4.7):
        self.breed = breed
        self.age = age
        self.name = name
        self.speed = speed

    def how_fast(self, accel):
        print("This cat is going " + str(self.speed) + " plus " + str(accel))


def get_attribute_value():
    """Let's say I have a variable 'external_data' that contains the name of an attribute. Now, I don't know the
    what attribute name will be contained in the variable at run-time, but I do know it will contain some attribute
    name. I can use getattr() to return the value of that attribute.
    """
    external_data = "age"
    brown_cat = Cat()
    print("brown_cat.age: " + str(brown_cat.age))
    white_cat = Cat()
    print("white_cat.age: " + str(getattr(white_cat, external_data)))
    """AttributeError is thrown if the object does not have the attribute AND no default argument is provided. If a
    default argument is provided, it is returned in the event that the attribute does not exist.
    """
    # getattr(white_cat, "Quack")
    print(getattr(white_cat, "Quack", "ha ha nothing here"))


def get_function():
    """getattr() will return any existing attribute, which includes functions! Once returned, a function can be
    invoked. Remember that functions are first class objects!"""
    purple_cat = Cat()
    getattr(purple_cat, "how_fast")(20.1)


def iterate_over_attributes():
    pretty_cat = Cat()
    for attr_name in dir(pretty_cat):
        attr_val = getattr(pretty_cat, attr_name)
        """callable() tells me if the object is 1) a class (all of which have the __call__ attribute) 2) a function"""
        print(attr_name, attr_val, callable(attr_val))


if __name__ == "__main__":
    # get_attribute_value()
    # get_function()
    iterate_over_attributes()
