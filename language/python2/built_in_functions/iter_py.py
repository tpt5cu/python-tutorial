# https://docs.python.org/2/library/functions.html#iter


def get_iterator_object():
    """
    iter() and __iter__() both return an iterator object. Note however that calling these methods returns a different iterator. Calling either of
    these methods twice would also return a different iterator each time.
    """
    my_list = ['a', 'b', 'c', 'd', 'e']
    syntactic_sugar_iterator = iter(my_list)
    print(type(syntactic_sugar_iterator)) # <type 'listiterator'>
    iterator = my_list.__iter__()
    print(type(iterator)) # <type 'listiterator'>
    iterator2 = my_list.__iter__()
    print(syntactic_sugar_iterator == iterator) # False
    print(iterator == iterator2) # False


if __name__ == "__main__":
    get_iterator_object()