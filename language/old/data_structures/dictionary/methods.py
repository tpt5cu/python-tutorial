

def pop():
    """<dict>.pop() removes and returns the value associated with the given key (and removes the key).
    If the key didn't exist, a KeyError is raised.
    If the key didn't exist and a default value was provided, the default value is returned.
    """
    my_dict = {"prop1": 1, "prop2": 2}
    print(my_dict.pop("prop2"))
    #print(my_dict.pop("prop3"))
    print(my_dict.pop("prop3", "There was no value!"))


if __name__ == "__main__":
    pop()