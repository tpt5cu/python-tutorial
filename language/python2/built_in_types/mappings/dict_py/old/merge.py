"""
https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
"""


def merge_in_place():
    """
    <dict>.update(<dict>) will update the calling dict in-place with the key-value pairs of the argument dict. This is good enough in most situations.
    """
    dict_1 = {
        "red": "a nice color",
        "blue": "also nice",
        "brown": "an ugly color"
    }
    dict_2 = {
        "yellow": "a vibrant color",
        "purple": "a complex color",
        "brown": "grossssss"
    }
    dict_1_copy = dict_1.copy()
    dict_1_copy.update(dict_2)
    # If the two dicts share keys, the argument dict will overwrite the calling dict
    print(dict_1_copy) # "grossssss"
    dict_2.update(dict_1)
    print(dict_2) # "an ugly color"


if __name__ == "__main__":
    merge_in_place()