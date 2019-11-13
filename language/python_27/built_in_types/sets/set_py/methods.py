# https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset


"""Sets are mutable while frozensets are immutable"""


def add_py():
    s = set((5, 4, 3, 2, 1))
    s.add("pie")
    print(s)
    print(type(s)) # <type 'set'>


def remove_with_error():
    """remove() will raise an Error if the targeted element does not exist in the set"""
    s = set((1, 2, 3, 4, 5))
    s.remove(88) # KeyError


def remove_without_error():
    """discard() won't raise an error if the item does not exist"""
    s = set((1, 2, 3, 4, 5))
    s.discard(99)


if __name__ == "__main__":
    #add_py()
    #remove_with_error()
    remove_without_error()