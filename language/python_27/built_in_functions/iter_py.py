# https://docs.python.org/2/library/functions.html#iter


def iter_vs_iter():
    '''
    iter() and __iter__() both return an iterator object. Note however that calling these methods returns a different iterator. Calling either of
    these methods twice would also return a different iterator each time.
    '''
    my_list = ['a', 'b', 'c', 'd', 'e']
    syntactic_sugar_iterator = iter(my_list)
    print(type(syntactic_sugar_iterator)) # <type 'listiterator'>
    print(syntactic_sugar_iterator) # <listiterator object at ...>
    iterator = my_list.__iter__()
    print(type(iterator)) # <type 'listiterator'>
    print(iterator) # <listiterator object at ...>
    print(syntactic_sugar_iterator == iterator) # False
    iterator2 = my_list.__iter__()
    print(iterator == iterator2) # False


def repeated_iter():
    '''
    A new, different iterator object appears to be returned only when previous iterators still have a reference to them
    '''
    my_list = ['cat', 'dog', 'frog']
    # These are the same object. Python must just detect that the iterator was returned and thrown away, so it reuses it
    print(iter(my_list)) # <listiterator object at 1>
    print(iter(my_list)) # <listiterator object at 1>
    # Same object as above
    i1 = iter(my_list)
    #print(i1.next()) # cat
    print(i1) # <listiterator object at 1>
    i2 = iter(my_list) 
    print(i2) # <listiterator object at 2> 
    print(iter(my_list)) # <listiterator object at 3>
    print(iter(my_list)) # <listiterator object at 3>


if __name__ == "__main__":
    #iter_vs_iter()
    repeated_iter()