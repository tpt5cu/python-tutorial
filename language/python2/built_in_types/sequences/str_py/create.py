# https://docs.python.org/2/library/stdtypes.html#string-methods


def list_to_string():
    """
    - Do not use str() to create a string from a list. str() returns a nicely printable representation of an object. That's all.
    - Use the <str>.join(<iterable>) method to get a string from an iterable
    """
    ary = list("What a nice sentence")
    print(ary)
    print(str(ary)) # ['W', 'h', 'a', 't', ' ', 'a', ' ', 'n', 'i', 'c', 'e', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']
    print(''.join(ary)) # What a nice sentence
    #print(str.join(ary)) # TypeError


if __name__ == "__main__":
    list_to_string()