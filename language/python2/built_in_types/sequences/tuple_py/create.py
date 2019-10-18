# https://docs.python.org/2.7/tutorial/datastructures.html#tuples-and-sequences


"""
- A tuple is an immutable sequence data structure
- A tuple is often heterogenous (contains elements of different types), unlike a list which is usually homogenous (contains elements of the same type)
"""


def no_parentheses():
    """Tuples don't require parentheses to be declared. However, in certain contexts the parentheses are needed"""
    weird_tuple = 1, 2, 3
    print(weird_tuple) # (1, 2, 3)
    print(type(weird_tuple)) # <type 'tuple'>


def empty_tuple():
    """Empty parentheses create a tuple with 0 elements"""
    empty = ()
    print(type(empty)) # <type 'tuple'>


def single_element_tuple():
    """Creating a single element tuple has ugly syntax"""
    single = (1,)
    print(type(single)) # <type 'tuple'>


if __name__ == "__main__":
    #no_parentheses()
    #empty_tuple()
    single_element_tuple()