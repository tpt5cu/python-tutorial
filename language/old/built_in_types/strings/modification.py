# https://stackoverflow.com/questions/1228299/change-one-character-in-a-string

import timeit

"""strings are immutable, along with every other built_in type in Python. The only things that are mutable are a 
subset of data structures, which includes lists, sets, and dictionaries. Tuples are an immutable data structure."""


def string_to_list():
    """Strings should NEVER be modified. Instead, convert the string to a list and work with it until I'm ready to
    turn it back into a string.
    """
    print(timeit.timeit(
        "text = 'abcdefg'; s = list(text); s[6] = 'W'; ''.join(s)",
        number=1000000)
    )


def create_new_string():
    """This way is consistently faster than converting to a list because..."""
    if False:
        text = 'abcdefg'
        # Gets character 0
        print(text[:1])
        # Gets characters 2 - len(string)
        print(text[2:])
        text = text[:1] + 'Z' + text[2:]
        print(text)
    print(timeit.timeit(
        "text = 'abcdefg'; text = text[:1] + 'Z' + text[2:]",
        number=1000000)
    )


if __name__ == "__main__":
    string_to_list()
    create_new_string()
