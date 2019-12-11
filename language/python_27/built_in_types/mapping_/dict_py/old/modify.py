# https://docs.python.org/2.7/library/stdtypes.html#mapping-types-dict


def delete_element():
    """The del statement is not a built-in function, but a statement that can be used with lists, tuples, dictionaries"""
    my_dict = {
        "cat": "Amber",
        "dog": "Max"
    }
    print(my_dict)
    del my_dict["dog"]
    #del my_dict.get("dog") Throws SyntaxError because can't delete a function call
    print(my_dict)
    #del my_dict["foo"] # Throws KeyError, but not because of del statement


def delete_during_iteration():
    """If I want to modify a dictionary during iteration, I have to iterate over a list/tuple/sequence of keys that doesn't change during iteration."""
    my_dict = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e"
    }
    # This code throws a RuntimeError because the dictionary's size changes during iteration
    #for key in my_dict:
    #    if key % 2 == 0:
    #        del my_dict[key]
    # This code does NOT throw a RuntimeError because my_dict.keys() returns a list of the dict's keys. I'm iterating over a list, not the actual
    # dictionary
    for key in my_dict.keys():
        if key % 2 == 0:
            del my_dict[key]
    print(my_dict)


def bonus_delete():
    my_list = [1, 2, 3]
    del my_list[1]
    print(my_list)
    my_tup = (4, 5, 6)
    my_tup = filter(lambda x: x != 5, my_tup)
    #del my_dup[2] # tuples are immutable
    print(my_tup)
    my_set = set([1, 2, 3]) # a set() constructor requires a single iterable object
    #del my_set[0] I cannot delete items from a set
    my_set.remove(3)
    print(my_set)


if __name__ == "__main__":
    #delete_element()
    #bonus_delete()
    delete_during_iteration()