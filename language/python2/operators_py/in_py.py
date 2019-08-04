"""
https://stackoverflow.com/questions/35302215/python-in-operator
"""


def sequence_membership():
    """
    The 'in' operator is used to check if a value exists in a sequence. It is actually a shortcut for calling an object's __contains__ method.
    Therefore, 'in' is equivalent to 'x is y or x == y'. This means that if the element is equal in memory to a sequence element or equal in value to a
    sequence element, the operator returns true.
    """
    my_list = [1, 2, 3, 4, 5]
    print("1" in my_list) # False because the byte string "1" is not contained in a list of integers
    print(1 in my_list) # True
    list_a = ["bye"]
    list_b = ["hi"]
    list_of_lists = [list_b]
    print(list_a in list_of_lists) # False
    list_a[0] = "hi"
    print(list_a in list_of_lists) # True due to value equality
    print(list_b in list_of_lists) # This is true due to identity (and value) equality


def in_none():
    """If a sequence could instead be None, I cannot use a naked 'in' operator"""
    if 1 in None: # TypeError: argument of type 'NoneType' is not iterable
        print("impossible")
    else:
        print("predictable")


if __name__ == "__main__":
    #sequence_membership()
    in_none()