"""
https://stackoverflow.com/questions/35302215/python-in-operator
"""

def sequence_membership():
    """ The 'in' operator is used to check if a value exists in a sequence. It is actually a shortcut for calling an object's __contains__ method. 
    Therefore, 'in' is equivalent to 'x is y or x == y'. This means that if the element is equal in memory to a sequence member or equal in value to
    a sequence member, the operator returns true.
    """
    my_list = [1, 2, 3, 4, 5]
    # This is false because the byte string "1" is not contained in a list of integers
    print("1" in my_list)
    # This is true
    print(1 in my_list)
    list_a = ["hi"]
    list_b = ["hi"]
    list_of_lists = [list_b]
    # This is true due to value equality
    print(list_a in list_of_lists)
    # This is true due to identity (and value) equality
    print(list_b in list_of_lists)

if __name__ == "__main__":
    sequence_membership()