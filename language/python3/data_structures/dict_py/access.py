# https://stackoverflow.com/questions/31837161/python-difference-between-listdict-and-dict-keys/31837256
# https://docs.python.org/3.7/library/stdtypes.html#dict-views - dict_keys doc


def examine_dict_keys():
    """
    A dict_keys object is not the same as a list of keys. It is only a view of the keys in dict, not a separate list that happens to have the same
    values as the keys in the dict. I can iterate over a dict_keys object, but I cannot index it. I also cannot iterate over a dict_keys object and
    modify the dict at the same time.
    """
    my_dict = {
        1: 'a',
        2: 'b',
        3: 'c'
    }
    key_view = my_dict.keys()
    print(key_view) # dict_keys([1, 2, 3])
    print(type(key_view)) # <class 'dict_keys'>
    for k in key_view:
        print(k)
    #print(key_view[0]) # TypeError
    # Using the list() constructor on a dict will return a list of the dict's keys
    key_list = list(my_dict)
    print(key_list) # [1, 2, 3]
    print(type(key_list)) # <class 'list'>


if __name__ == "__main__":
    examine_dict_keys()