"""
https://realpython.com/python-dicts/
"""

"""
A dictionary is another mutable collection, like a list, except that data is stored and accessed in key-value pairs. Dictionaries do NOT keep order
(well, starting in Python 3.7 they do), so don't depend on the insertion order of a dictionary. I think that dictionary keys can be of any immutable
type
"""

def literal():

    foods = {
        'starch': 'bread',
        'protein': 'steak',
        'dairy': 'yogurt'
    }
    print(foods)
    # Dictionaries might look like JavaScript objects, but they are not. All keys must have a defined type. Keys are not automatically strings.
    #animals = {
    #    cat: "Molly",
    #    dog: "george"
    #}
    #print(animals)


def fill_with_keys():
    """Create a dict with specified keys, where each key holds a list."""
    keys = ['a', 'b', 'c']
    d = {key:[] for key in keys}
    print(d)


def constructor():
    pass

if __name__ == "__main__":
    #literal()
    fill_with_keys()
    #constructor()