# https://docs.python.org/2.7/reference/expressions.html#membership-test-details
# https://stackoverflow.com/questions/14247373/python-none-comparison-should-i-use-is-or
# https://stackoverflow.com/questions/27276610/boolean-identity-true-vs-is-true


def is_py():
    """ The 'is' operator checks if two objects are exactly the same object in memory. """
    list_a = ["hello there"]
    list_b = ["hello there"]
    # This is false because a and b are two completely different lists that happen to have identical contents
    print(list_a is list_b)
    # This is true since the lists have the same value
    print(list_a == list_b)


def equals_py():
    """ 
    The '==' operator checks if two objects have the same value. The objects need not have the same type. However, for many built-in types '=='
    comparison is false if the objects have different types.
    """
    list_a = ["what", "no"]
    list_b = ["no", "what"]
    list_c = ["what", "no"]
    tup = ("what", "no")
    # This is false because the lists aren't ordered the same
    print(list_a == list_b)
    # This is true
    print(list_a == list_c)


def equals


def equals_with_order():
    """
    - If two dictionaries have the same contents, but different "ordering", they are equivalent
    - If two lists have the same contents, but different ordering, they are NOT equivalent
        - Same for tuples
    - A set() does not have an ordering, therefore sets with equivalent contents are equivalent
    """
    d1 = {
        "foo": "bar",
        "Austin": "Chang"
    }
    d2 = {
        "Austin": "Chang",
        "foo": "bar"
    }
    print(d1 == d2)
    l1 = [1, 2]
    l2 = [2, 1]
    print(l1 == l2)
    t1 = ("yes", "no")
    t2 = ("no", "yes")
    print(t1 == t2)
    s1 = set([1, 2])
    s2 = set([2, 1])
    print(s1 == s2)


def none_py():
    """
    Always use 'is' to compare to None because it is possible to define '==' so that 'x == None' is true while 'x is None' is false (this would be
    confusing)
    """
    d = {}
    # Is true but this is bad
    print(d.get("thing") == None)
    print(d.get("thing") is None)


def check_boolean():
    """Use 'is' when comparing to the singletons True and False"""
    if 1 is True:
        print("1 is True")
    elif 1 == True: # Don't do this
        print("1 == True") # This is True!!!
    else:
        print("False)")


if __name__ == "__main__":
    #py_is()
    #py_equals()
    #equals_with_order()
    #none_py()
    check_boolean()