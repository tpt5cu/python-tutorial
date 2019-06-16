"""
https://docs.python.org/2/tutorial/datastructures.html
"""


def delete_element():
    """
    The del statement is not a built-in function, but a statement that can be used with lists, tuples, dictionaries
    """
    my_dict = {
        "cat": "Amber",
        "dog": "Max"
    }
    print(my_dict)
    del my_dict["dog"]
    #del my_dict.get("dog") Throws SyntaxError because can't delete a function call
    print(my_dict)
    #del my_dict["foo"] # Throws KeyError, but not because of del statement


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
    bonus_delete()
