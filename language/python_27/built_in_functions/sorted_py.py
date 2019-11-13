# https://docs.python.org/2/library/functions.html#sorted


'''The sorted() function returns a NEW sorted LIST from the items in the iterable. It is stable.'''


def sort_ints():
    my_set = set([6, 456, 234, 52475, 367, 234, 3542, 362, 5672, 6])
    print(sorted(my_set))


def sort_strings():
    """As expected, strings are sorted in ASCII order: capital letters come before lowercase, longer strings come after shorter strings."""
    strings = ["Austin", "apple", "ardvark", "Astronomy", "amazing", "add", "ankle", "Ankle", "anaconda", "ashes", "ash"]
    print(sorted(strings))


def sort_2d_list():
    """Sort by valid lines, then sort by name. Actually, I can't sort based on multiple criteria with just the "key" parameter."""
    data = [
        ["hourly", "2000", "Alaska", 8760, 5000, 3760],
        ["hourly", "2001", "Alabama", 8760, 4001, 4760],
        ["hourly", "2001", "Maine", 8760, 2999, 5760],
        ["hourly", "2000", "Maine", 8760, 3000, 5760],
        ["hourly", "2001", "Alaska", 8760, 5001, 3760],
        ["hourly", "2001", "Virginia", 8760, 4001, 4760],
        ["hourly", "2000", "Virginia", 8760, 4000, 4760],
        ["hourly", "2000", "Alabama", 8760, 4000, 4760]
    ]
    #sorted_by_valid_lines = sorted(data, key=lambda e: e[4])
    #sorted_by_name = sorted(sorted_by_valid_lines, key=lambda e: e[2])
    #print(sorted_by_name)
    sort_by_valid_and_name = sorted(data, cmp=custom_comp)
    print(sort_by_valid_and_name) # 2000 Alaska, 2000 Alabama, 2000 Virginia, 2000 Maine, 2001 Alaska, 2001 Alabama, 2001 Virginia, 2001 Maine


def custom_comp(e1, e2):
    # sort by year first
    if e1[1] == e2[1]: # years are equal
        if e1[4] == e2[4]: # valid counts are equal
            if e1[2] < e2[2]:
                return -1
            else:
                return 1
        elif e1[4] < e2[4]:
            return 1
        else:
            return -1
    elif e1[1] < e2[1]:
        return -1
    else:
        return 1


if __name__ == "__main__":
    #sort_ints()
    #sort_strings()
    sort_2d_list()