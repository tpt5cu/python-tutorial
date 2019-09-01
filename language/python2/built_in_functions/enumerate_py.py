# https://docs.python.org/2/library/functions.html#enumerate



def iterate_with_index():
    """
    enumerate() returns an enumerate object. 
    """
    my_list = ['a', 'b', 'c', 'd', 'e']
    x = enumerate(my_list)
    print(x) # <enumerate object at ...>
    print(type(x)) # <type 'enumerate'>


if __name__ == "__main__":
    iterate_with_index()
