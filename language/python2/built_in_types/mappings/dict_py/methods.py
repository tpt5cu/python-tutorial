# https://docs.python.org/2.7/library/stdtypes.html#mapping-types-dict


def check_length():
    """
    There are multiple ways to check the length of a dictionary:
    - Just use len(<dict>)
    - get a list of keys and check the length
    - get a view object of the dictionary's keys and check the length
    """
    my_dict = {'my_key': 10}
    print(len(my_dict)) # 1


def key_value_iteration():
    """
    - dict.items() returns a list of tuples, where each tuple contains a key and a value. Therefore, what this is doing is 1) getting a list from the
      dictionary, 2) getting an element from the list that is a tuple, and 3) inspecting the items in the element.
    - dict.iteritems() returns an iterator over the dictionary's (<key>, <value>) pairs. This is more efficient than generating an entirely new list
    """
    my_dict = {
        "prop1": "val1",
        "prop2": 5
    }
    # This is invalid syntax! 
    #for key, val in dictionary: print(val)
    #for key, val in my_dict.items():
    #    print(key)
    #    print(val)
    for k, v in my_dict.iteritems():
        print(str(k) + ': ' + str(v)) # prop1: val1 prop2: 5


def value_iteration():
    """
    - <dict>.values() returns a list of the values in a dictionary. Don't depend on any particular ordering of the list. The returned list is an
      entirely new list. It has no relationship to the original dictionary
    - <dict>.itervalues() returns an iterator over the dictionary's values. Do NOT add or delete dictionary entries while iterating over a dictionary.
      Modifying entries is fine. This is more efficient than generating an entirely new list!
    """
    my_dict = {
        'name': 'Maruy',
        'favorite': 'milk'
    }
    #values = my_dict.values()
    #print(type(values)) # <type 'list'>
    #for v in values:
    #    print(v) # milk Maury
    for v in my_dict.itervalues():
        print(v) # milk Maury


def key_iteration():
    """<dict>.keys() returns a list of the keys in a dictionary. Don't depend on any particular ordering of the list"""
    my_dict = {
        'name': 'Maruy',
        'favorite': 'milk'
    }
    keys = my_dict.keys()
    print(type(keys)) # <type 'list'>
    for k in keys:
        print(k) # favorite name


# Don't use
def conditionally_insert_value():
    """
    <dict>.setdefault() is a shortcut for checking whether or not a key exists in a dictionary and then inserting it
    - If the dictionary already contains the key, the return the value associated with the key
    - If the dictionary does not contain the key, insert the key value pair and return the value that was just inserted
    - Actually, I shouldn't use this function. Why? Because the return value is the same whether or not the key was already in the dictionary. I can't
      tell from the return value whether or not I inserted a new (key, value) or whether I accessed an existing (key, value)
    """
    my_dict = {
        '1': 1,
        '3': 3
    }
    print(my_dict.setdefault('2', 'cat')) # '2' is not in the dictionary, so insert 'cat' and return 'cat'
    print(my_dict.setdefault('2', 'dog')) # '2' is already in the dictionary, so return 'cat'


def dynamic_dictionary_view():
    """
    A dynamic view of a dictionary's contents is useful when... I honestly don't know when I'll need this.
    - A view object does not support item assignment. Therefore, a view object cannot be used to modify a dictionary. It's sole purpose it to
      dynamically track the state of the dictionary
    - A view object can view keys, values, or both
    """
    my_dict = {
        'random': 7,
        'key': 98,
        'hi': 11
    }
    my_view = my_dict.viewvalues()
    print(type(my_view)) # <type 'dict_values'>
    my_dict['random'] = 'hashflakjsdf'
    for k in my_dict.itervalues():
        print(k)
    print('')
    for k in my_view:
        print(k)


if __name__ == "__main__":
    #check_length()
    #key_value_iteration()
    #value_iteration()
    #key_iteration()
    #conditionally_insert_value()
    #dynamic_dictionary_view()
    pass