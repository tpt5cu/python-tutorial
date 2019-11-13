#https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/


"""Also see the functions/parameters/kwargs_py notes"""


def copy_dictionary():
    """The ** operator can be used inside of a dict() construction to copy one dict into the new dict"""
    animals = {
        # Using this ** operator to copy/merge dictionaries is only possible in Python 3
        #**my_dict,
        "cat": "Ralph",
        "dog": "Persimmon",
        "fish": "Joe",
    }
    copy = dict(**animals)
    print(copy)
    print(copy is animals)


if __name__ == "__main__":
    copy_dictionary()