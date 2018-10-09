# https://stackoverflow.com/questions/207000/what-is-the-difference-between-class-and-instance-attributes
# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
# https://stackoverflow.com/questions/32720492/why-is-a-class-dict-a-mappingproxy

# TODO: look at his later

g_var = "Whoo!"


class CellPhone:
    """A class attribute is similar, but not identical, to a static member in Java."""

    os = "Android"
    brand = "Asus"
    stuff = [1, 2, 3]

    def __init__(self, os="IOS"):
        self.os = os


def view_shadowed_attribute():
    """When an instance attribute shadows a class attribute, the only way to access the class attribute is with the
    <class>.<attribute> syntax.
    """
    phone = CellPhone()
    print(phone.os)
    print(CellPhone.os)


def view_class_attribute():
    """If a class attribute is NOT shadowed, then it can be accessed just fine through an instance. Whenever an
    attribute is accessed on an object, first the instance's namespace is checked. If the attribute is not found
    in the instance's namespace, the class namespace is examined. If it isn't found there, an error is thrown.
    """
    phone = CellPhone()
    # check the namespace of the class. Didn't find it, so check the class
    print(phone.brand)
    # global variable, so it exists
    print(g_var)
    # g_var attribute doesn't exist in instance of class namespace, throw AttributeError
    # print(phone.g_var)


def turn_class_attribute_to_instance():
    """Reassigning a mutable or immutable class attribute through a particular instance will
    1) add an instance attribute to that instance with the same name as the class attribute
    2) change the new instance attribute.
    Other instances will still reference the class attribute.
    """
    my_phone = CellPhone()
    your_phone = CellPhone()
    print("my_phone.brand: " + my_phone.brand)
    print("your_phone.brand: " + your_phone.brand)
    my_phone.brand = "Windows"
    print("my_phone.brand: " + my_phone.brand)
    print("your_phone.brand: " + your_phone.brand)
    print("class attribute: " + CellPhone.brand)


def reassign_any_class_attribute_through_class():
    """ Reassigning a mutable OR immutable class attribute through the class WILL reassign the actual class attribute
    """
    phone = CellPhone()
    print("phone.brand: " + phone.brand)
    print("Cellphone.brand: " + CellPhone.brand)
    CellPhone.brand = "Samsung"
    print("phone.brand: " + phone.brand)
    print("Cellphone.brand: " + CellPhone.brand)
    """This throws a TypeError because mappingproxy doesn't support item assignment. I need to use setattr() instead.
    Using setattr() is equivalent to the code above.
    """
    # CellPhone.__dict__["brand"] = "Motorola"
    setattr(CellPhone, "brand", "Motorola")
    print("phone.brand: " + phone.brand)
    print("Cellphone.brand: " + CellPhone.brand)


def modify_mutable_class_attribute():
    """Modifying a mutable class attribute through an instance (or the class) WILL change that attribute for
    all other instances. That's because no new attribute in the instance's namespace is created.

    Modifying an immutable class attribute is impossible. Any time this happens, a new immutable object is created and
    the variable is reassigned to this new object.
    """
    phone1 = CellPhone()
    print(phone1.stuff)
    phone2 = CellPhone()
    print(phone2.stuff)
    phone1.stuff.append(99)
    CellPhone.stuff.append("More stuff")
    print(phone1.stuff)
    print(phone2.stuff)


if __name__ == "__main__":
    # view_shadowed_attribute()
    # view_class_attribute()
    turn_class_attribute_to_instance()
    reassign_any_class_attribute_through_class()
    modify_mutable_class_attribute()
