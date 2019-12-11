# https://docs.python.org/2/library/stdtypes.html#set


def from_list():
    """I have to use the list() constructor to create a list from a set. Using the list literals won't work"""
    my_list = [1, 2, 3, 3, 3, 4]
    my_set = set(my_list)
    #new_list = [my_set] # [set([1, 2, 3, 4])]
    new_list = list(my_set) # [1, 2, 3, 4]
    print(new_list)


if __name__ == "__main__":
    from_list()