# https://www.programiz.com/python-programming/nested-dictionary#iteration


def get_dictionary():
    # type: () -> dict
    my_dict = {
        "cat": {
            "red": 2342,
            "blue": 4859,
            "green": 990
        },
        "dog": {
            "yellow": 48523,
            "purple": 248234,
            "redish": 1
        },
        "ferret": {
            "red": 2405234,
            "green": 20452,
            "orange": 23043
        }
    }
    return my_dict


def parse_nested_dictionary():
    """<dictionary>.items() returns a LIST of TUPLES containing the key-value pairs of the dictionary. This is key."""
    my_dict = get_dictionary()
    count = 0
    """'key' accesses the first item in the tuple. It IS a string.
    'val' accesses the second item in the tuple. It IS a dictionary.
    """
    for key, val in my_dict.items():
        """<dictionary>.get() WON'T work because I'm searching for multiple values inside the dictionary. I need to
        iterate over all the values in the dictionary.
        """
        #if val.get("red") or val.get("green"):
        for sub_key, sub_val in val.items():
            if sub_key == "red" or sub_key == "green":
                count += 1
    if count == 0:
        print("No red or green!")
    else:
        print("count was : " + str(count))


def clean_parse_nested_dictionary():
    my_dict = get_dictionary()
    count = 0
    for key, val in my_dict.items():
        for sub_key, sub_val in val.items():
            if sub_key == "red" or sub_key == "green":
                count += 1
    if count == 0:
        print("No red or green!")
    else:
        print("count was : " + str(count))


if __name__ == "__main__":
    parse_nested_dictionary()
    clean_parse_nested_dictionary()
