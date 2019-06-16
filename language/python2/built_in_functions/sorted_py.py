"""
https://docs.python.org/2/library/functions.html#sorted
"""


"""
The sorted() function returns a NEW sorted LIST from the items in the iterable. It is stable.
"""

def sort_ints():
    my_set = set([6, 456, 234, 52475, 367, 234, 3542, 362, 5672, 6 ])
    print(sorted(my_set))


def sort_strings():
    """ As expected, strings are sorted in ASCII order: capital letters come before lowercase, longer strings come after shorter strings """
    strings = ["Austin", "apple", "ardvark", "Astronomy", "amazing", "add", "ankle", "Ankle", "anaconda", "ashes", "ash"]
    print(sorted(strings))


if __name__ == "__main__":
    #sort_ints()
    sort_strings()