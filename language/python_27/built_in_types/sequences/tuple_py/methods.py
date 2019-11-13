def get_element():
    """Tuples are accessed with brackets []. Using parentheses is always a function call and is thus incorrect."""
    t = ("Some", 4, True)
    print(t[1]) # 4


def slice_tuple():
    """
    A tuple is a sequence type, and so has access to that methods defined for sequences. Slicing appears to always return a data structure of the same
    type that was sliced.
    """
    t = ("Bird", 5, False, [])
    new_tup = t[1:3] # slicing indexe are [inclusive:exclusive]
    print(new_tup) # (5, False)
    print(type(new_tup)) # <type 'tuple'>


if __name__ == "__main__":
    #get_element()
    slice_tuple()