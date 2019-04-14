""" It appears that comprehensions are much more powerful than I thought. I can freely navigate between sets, lists, and dictionaries
however I want!
"""

def traverse_dictionary():
    dictionary = {
        "0": "2345q3",
        1: 4326423.45,
        "2": 1025.354
    }
    # This grabs the first 2 characters of every key
    my_dict = {key: str(dictionary.get(key))[0:2] for key in dictionary}
    print(my_dict)
    # This returns a set of the dictionary's keys
    my_dict = {key for key in dictionary}
    print(my_dict)

def list_to_dictionary():
    my_list = ["cat.omd", "person.omd", "class.omd"]
    # It seems that using this syntax always produces a set, regardless of whether the iterable is a list or a dictionary
    my_set = {item[0:-4] for item in my_list}
    print(my_set)
    # I am adding a useless "value" here, but I could do something else
    my_dict = {item[0:-4]: "value" for item in my_list}
    print(my_dict)

if __name__ == "__main__":
    #traverse_dictionary()
    list_to_dictionary()
