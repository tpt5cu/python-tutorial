# https://stackoverflow.com/questions/18072759/list-comprehension-on-a-nested-list


def without_list_comprehension():
    """Let's say I have a nested list and I want to add 1 to every element in every list. Remember, it's poor form
    to modify a list during iteration. Additionally, trying to modify immutable elements WITHOUT using indexes is
    frustrating. Using indexes is frustrating too, so I'm appending to a new list.
    """
    new_list = []
    my_list = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    for sub_list in my_list:
        new_sub_list = []
        for e in sub_list:
            new_sub_list.append(e + 1)
        new_list.append(new_sub_list)
    print("old list: " + str(my_list))
    print("new list: " + str(new_list))


def with_list_comprehension():
    """Look at how I reduced code from 7 lines to 2 lines. Amazing! I kind of have to read from the outside-in to
    understand what is happening, but that's okay. This isn't the FASTEST way of doing this (using map is), but it's
    ideomatic.
    """
    my_list = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    new_list = [[e + 1 for e in sub_list] for sub_list in my_list]
    print("old list: " + str(my_list))
    print("new list: " + str(new_list))


if __name__ == "__main__":
    without_list_comprehension()
    with_list_comprehension()
