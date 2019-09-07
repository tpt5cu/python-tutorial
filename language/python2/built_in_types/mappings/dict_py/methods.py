# https://docs.python.org/2.7/library/stdtypes.html#mapping-types-dict


def check_length():
    """
    There are multiple ways to check the length of a dictionary:
    - get a list of keys and check the length
    - get a view object of the dictionary's keys and check the length
    """
    my_dict = {}
    keys = my_dict.keys()
    print(type(keys)) # <type 'list'>
    print(len(keys)) # 0
    # Does not work in Python 3 because keys() itself returns a <type 'dict_keys'>
    keys = my_dict.viewkeys()
    print(type(keys)) # <type 'dict_keys'>
    print(len(keys)) # 0


def key_value_iteration():
    """
    dict.items() returns a list of tuples, where each tuple contains a key and a value. Therefore, what this is doing is 1) getting a list from the
    dictionary, 2) getting an element from the list that is a tuple, and 3) inspecting the items in the element.
    """
    my_dict = {
        "prop1": "val1",
        "prop2": 5
    }
    for key, val in my_dict.items():
        print(key)
        print(val)
    # This is invalid syntax! 
    #for key, val in dictionary: print(val)


if __name__ == "__main__":
    #check_length()
    key_value_iteration()