# https://docs.python.org/2/library/functions.html#setattr


def set_nonexistant_attribute():
    """
    Recall that an object must have a __dict__ property in order to have new/arbitrary attributes assigned to it. setattr() does not allow me to
    bypass this restriction, so attempting to change a nonexistent attribute on a built-in type will raise an AttributeError()
    """
    x = 5
    #print(dir(x))
    setattr(x, "foobar", 4) # AttributeError


def set_readonly_attribute():
    """
    Attempting to modify a read-only attribute will result in an AttributeError. I think it's using properties under the hood with custom error
    messages.
    """
    x = 5
    setattr(x, "__cmp__", None) # AttributeError


if __name__ == "__main__":
    #set_nonexistant_attribute()
    set_readonly_attribute()