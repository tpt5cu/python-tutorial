# https://stackoverflow.com/questions/15376509/when-is-i-x-different-from-i-i-x-in-python


def regular_plus_with_immutable_object():
    """Whenever the + operator is used, it implicitly calls the __add__ or __radd__ method of the object being operated on.
    __add__ always returns a NEW instance of an object. It does not matter whether the object is immutable or mutable.
    """

    """This int has a unique id."""
    i = 1
    print(str(id(i)))
    """This int has a different id, because it is not the same int as above. This shows that a new object was indeed
    returned and assigned to the variable i.
    """
    i = i + 1
    print(str(id(i)))
    print(i)


def plus_equals_with_immutable_object():
    """Whenever the += operator is used, it implicitly calls the __iadd__ method of the object being operated on. If the
    object does not implement __iadd__, then the operator will fall back to using regular __add__.

    __iadd__ is only used to modify mutable objects in-place, so only mutable objects implement __iadd__. This means that
    when += is used with an immutable object, the result is the same as if + had been used. All built-in types
    (i.e. bool, int, float, str, complex) are immutable.
    """
    i = 5
    print(str(id(i)))
    i += 6
    print(str(id(i)))
    print(i)


def regular_plus_with_mutable_object():
    """In this example, __add__ is being used to return a new object as the result of adding two lists together.
    That's why my_list has two different ids. The variable points to a different object after the operation!
    """
    my_list = [5, 6, 7, 11, 4]
    print(str(id(my_list)))
    my_list = my_list + my_list
    print(str(id(my_list)))
    print(my_list)


def plus_equals_with_mutable_object():
    """This is the only special case. my_list is a list data structure, and therefore is a mutable object. When += is
    used, it calls __iadd__ instead of __add__. The mutable object gets updated in-place. That's why the ids of both
    variables are the same after the operation. They point to the same object.
    """
    my_list = [4, 1, 5, 77, 2]
    print(str(id(my_list)))
    my_list += my_list
    print(str(id(my_list)))
    print(my_list)


if __name__ == "__main__":
    # regular_plus_with_immutable_object()
    # plus_equals_with_immutable_object()
    # regular_plus_with_mutable_object()
    plus_equals_with_mutable_object()
