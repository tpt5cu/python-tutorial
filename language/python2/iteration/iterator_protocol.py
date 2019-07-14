# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration


def next_method():
    """
    An iterator is an object that has a next() method (Python 2) or __next__() method (Python 3). The next() method returns the next element in the
    iterable, updates the iterator to point to the next value, and signals that iteration is complete by raising the StopIteration Exception.
    """
    #A list is an iterable, NOT an iterator.
    my_list = ["a", "b", "c", "d", "e"]
    iterator = my_list.__iter__()
    print(iterator.next()) # a
    print(iterator.next()) # b
    print(iterator.next()) # c
    print(iterator.next()) # d
    print(iterator.next()) # e
    try:
        print(iterator.next()) # StopIteration
    except Exception as e:
        print(type(e)) # <type 'exceptions.StopIteration'>


def __iter__method():
    """
    An iterator also has an __iter__() method, which simply returns itself.
    """
    my_list = [1, 2, 3]
    iterator = my_list.__iter__()
    print(type(iterator)) # <type 'listiterator'>
    print(iterator is iterator.__iter__()) # True


def bad_manual_iteration():
    """If I iterate using the value returned from next(), the iteration will stop when a falsy value is returned."""
    my_list = [(0,), (), (2)]
    iterator = iter(my_list)
    try:
        element = iterator.next()
        while element:
            print(element)
            element = iterator.next()
    except:
        pass


def good_manual_iteration():
    """This seems like the best way to perform iteration manually using an iterator."""
    my_list = ["foo", "bar", "baz", "faz"]
    iterator = iter(my_list)
    try:
        while True:
            element = iterator.next()
            print(element)
    except StopIteration:
        pass


def use_for_loop():
    """
    Apparently I can use an iterator inside of a for-loop just fine. Remember this. This is important because it means I never need to do manual
    iteration ever.
    """
    my_list = ['a', 'b', 'c', 'd', 'e']
    iterator = my_list.__iter__()
    for e in iterator:
        print(e)



if __name__ == "__main__":
    #next_method()
    #__iter__method()
    #bad_manual_iteration()
    #good_manual_iteration()
    use_for_loop()