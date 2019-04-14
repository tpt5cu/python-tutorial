"""
https://docs.python.org/2.7/reference/expressions.html#membership-test-details
https://stackoverflow.com/questions/14247373/python-none-comparison-should-i-use-is-or
"""

def py_is():
    """ The 'is' operator checks if two objects are exactly the same object in memory.
    """
    list_a = ["hello there"]
    list_b = ["hello there"]
    # This is false because a and b are two completely different lists that happen to have identical contents
    print(list_a is list_b)
    # This is true since the lists have the same value
    print(list_a == list_b)

def py_equals():
    """ The '==' operator checks if two objects have the same value. The objects need not have the same type. However, for many built-in types '==' comparison is false if the objects have different types.
    """
    list_a = ["what", "no"]
    list_b = ["no", "what"]
    list_c = ["what", "no"]
    tup = ("what", "no")
    # This is false because the lists aren't ordered the same
    print(list_a == list_b)
    # This is true
    print(list_a == list_c)

def py_none():
    """ Always use 'is' to compare to None because it is possible to define '==' so that 'x == None' is true while
    'x is None' is false (this would be confusing)
    """
    d = {}
    # Is true but this is bad
    print(d.get("thing") == None)
    print(d.get("thing") is None)

if __name__ == "__main__":
    #py_is()
    #py_equals()
    py_none()