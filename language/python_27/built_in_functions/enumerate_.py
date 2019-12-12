# https://docs.python.org/2/library/functions.html#enumerate
# https://www.programiz.com/python-programming/methods/built-in/enumerate


'''An enumerate object merely wraps another iterator with a convenience index'''


def examine_enumerate():
    '''
    enumerate() returns an enumerate object which is itself an iterator, so its values are returned on demand. An enumerate object returns an index
    along with a value from the original iterable. 
    '''
    my_list = ['a', 'b', 'c', 'd', 'e']
    x = enumerate(my_list)
    print(hasattr(x, 'next')) # True
    print(hasattr(x, '__iter__')) # True
    print(x.next()) # (0, 'a')
    print(x) # <enumerate object at ...>
    print(type(x)) # <type 'enumerate'>


def iterate_with_index():
    '''
    enumerate() can take a starting index that defaults to 0. The value of the starting index does NOT change the fact that enumerate will iterates
    over ALL of the items in the original iterable. 
    - The built-in list() function takes an iterable and returns a list. Presumably, it iterates over all of the items in the original iterable and
    puts them into a list!
    '''
    my_list = ['a', 'b', 'c', 'd', 'e']
    x = enumerate(my_list, 2) # the starting index does NOT directly affect iteration
    # x is an enumerate object, which is an iterator, and is therefore an iterable. I don't need to cast the enumerate object to a list in order to
    # iterate over it
    for idx, val in x:
        print(str(idx) + ' ' + str(val))


if __name__ == '__main__':
    #examine_enumerate()
    iterate_with_index()