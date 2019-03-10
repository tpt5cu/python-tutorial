# https://realpython.com/python-dicts/ (real python is the best)

"""A dictionary is another mutable collection, like a list, except that data is stored and accessed in key-value pairs.
Dictionaries do NOT keep order (well, starting in Python 3.7 they do), so don't depend on the insertion order of a
dictionary.
"""


def create_dictionary():
    """A dictionary can be created with literal syntax or with the dict() constructor."""
    # I'm using a list of tuples as input to the dict constructor
    people = dict([
        (33, 'George'),
        (22, 'Amanda'),
        (54, 'Gregory'),
        (2, 'Billy')
    ])
    print(people)
    """There is also a convenience syntax for when I am just using simple strings as keys. But this syntax is easy 
    to mess up, so don't use it.
    """
    soccer_team = dict(
        Forward='Matthew',
        Defense='Austin',
        Goalie='Jim'
    )
    print(soccer_team)


def access_dictionary():
    """Dictionaries are accessed by referencing them with a key in square brackets."""
    cars = dict(
        VTT458='Honda',
        B786QA='Toyota',
        # this key starts with a number, so Python doesn't understand that I want to use the entire key a string
        # 955TT5B='Ford'
        R55TT5='Ford'
    )
    print(cars)
    print(cars['B786QA'])


def modify_dictionary():
    """Setting a non-existent key to a value adds that value to the dictionary"""
    ids = {
        12: 'Austin',
        77: 'Mary',
        1: 'Timothy'
    }
    print(ids)
    ids[44] = 'Joseph'
    print(ids)
    """Setting an existing key to a value overwrites that value. No duplicate keys allowed!"""
    ids[1] = "this isn't a name!"
    print(ids)
    """Trying to reference a non-existent key throws a KeyError"""
    # var = ids[100]
    """Delete a key-value pair with the del operator"""
    del ids[77]
    print(ids)


def key_restrictions():
    """A dictionary key can be ANY immutable type, but NO mutable type. Dictionary values can be of ANY type"""
    weird_dict = {
        (1, 2, 3): 100,
        1: 200,
        True: 300,
        str: 400
    }
    print(weird_dict[(1, 2, 3)])
    print(weird_dict[1])
    print(weird_dict[True])
    print(weird_dict[str])
    """This throws a TypeError because 'list' is un-hashable"""
    weird_dict[[5, 6, 7]] = 5


if __name__ == "__main__":
    pass
    #create_dictionary()
    #access_dictionary()
    #modify_dictionary()
    #key_restrictions()
