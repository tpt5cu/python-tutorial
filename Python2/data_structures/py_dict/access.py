"""
https://realpython.com/python-dicts/#accessing-dictionary-values
"""

def py_get():
    """ Using brackets to access a value of a dictionary is great, except that a KeyError is thrown if the key doesn't exist.
    Use the get() method which is identical except it will return None if the key doesn't exist. I can set a default value instead of None if I want.
    """
    dictionary = {
        "name": "Austin",
        "age": 23
    }
    # Throws KeyError
    #print(dictionary["occupation"])
    # Returns None
    print(type(dictionary.get("madeUpVaLuE")))
    print(dictionary.get("occupation", "SuperHERo default value"))

def parse_dictionary():
    dictionary = {
        0: "first item",
        "1": "second item",
        2: "third item"
    }
    """ With just a single iteration parameter, that parameter always represents a key in the dictionary. """
    for key in dictionary:
        print(type(key))
        print(key)
    """ This is invalid syntax! """
    #for key, val in dictionary:
    #    print(val)
    """ dict.items() returns a list of tuples, where each tuple contains a key and a value. Therefore, what this is doing is
    1) getting a list from the dictionary 2) getting an element from the list 3) inspecting the items in the element.
    """
    for key, val in dictionary.items():
        print(val)
        
def parse_nested_dictionary():
    dictionary = {
        0: {
            "a": 23451543,
            "b": 4609,
            "c": 90345
        },
        1: {
            "a": 428.5342,
            "b": 82354.145,
            "f": "845"
        },
        "2": {
            45: "dfasfd",
            514: "fsdfasd3",
            "111": "11"
        }
    }
    """ dict.values() returns a list of values in the dictionary. Much more expressive then getting the key just to get the value. """
    for val in dictionary.values():
        for sub_key, val in val.items():
            print(val)

if __name__ == "__main__":
    #py_get()
    #parse_dictionary()
    parse_nested_dictionary()
