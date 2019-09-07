# https://docs.python.org/2/library/functions.html#slice


def get_slice():
    """
    The slice() function takes start, stop, step arguments. That's all! However, since slice() is a function, the arguments must be passed in like any
    other function. start and stop are REQUIRED arguments
    """
    my_list = [1, 2, 3, 4, 5]
    # Wrong syntax for passing function arguments
    #my_slice = slice(1::2)
    # Wrong syntax again
    #my_slice = slice(1,,2)
    my_slice = slice(1, len(my_list), 2)
    print(my_list[my_slice]) # [2, 4]


if __name__ == "__main__":
    get_slice()