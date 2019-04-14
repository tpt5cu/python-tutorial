def get_string():
    """Python is smart enough to print string representations of objects on their own. However, if I try to
    mix a string literal with a non-string type, I get a TypeError. To avoid this, I must use the str() built-in function
    to get a string representation of the object.
    """
    num = 5.0
    print(num)
    # print("The value is: " + num)
    print("The value is: " + str(num))


def get_int():
    """Giving the int() function an invalid literal (e.g. a word) will result in a ValueError. """
    # string = 'my string'
    # num = int(string)
    """Providing a float as an argument merely rounds the float down or up."""
    f = 3.4456
    num = int(f)
    print(num)
    """It appears that the string will not also be converted to a float, so this is invalid."""
    # string = "1.5"
    # num = int(string)
    """The proper string literal is converted to an int."""
    string = "5"
    num = 4.4 + int(string)
    print(num)


def get_float():
    """Passing an int or string int works fine."""
    string = "5"
    f = float(string)
    print(f)


if __name__ == "__main__":
    # get_string()
    # get_int()
    get_float()