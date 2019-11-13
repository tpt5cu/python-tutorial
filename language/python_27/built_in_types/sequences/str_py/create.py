# https://docs.python.org/2/library/stdtypes.html#string-methods
# http://python3porting.com/problems.html#byte-literals


def str_object_is_list_of_characters():
    '''The str type is a list of 8-bit characters. Indexing one element of a str will return another str, not an int!'''
    string = 'Nice string'
    print(type(string[6])) # <type 'str'>
    print((string[6])) # t
    print(ord(string[6])) # 116


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
    str_object_is_list_of_characters()
    #list_to_string()