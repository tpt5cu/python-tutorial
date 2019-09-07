# https://docs.python.org/2.7/library/stdtypes.html#typeiter - official protocol definition
# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration


"""
An iterator is simply an object that implements 2 methods: __iter__() and next() (not __next__(), that's Python 3)
- __iter__(): return the iterator object itself
- next(): return the next item from the container, or else raise StopIteration if there are no more items

An iterable is simply an object that implements 1 method: __iter__(). __iter__() returns an iterator object
- An iterable object may support different kinds of iteration, and thus may return different corresponding iterator objects

Therefore, an iterator is ALSO an iterable, and can be used in places where an iterable is expected (e.g. for loops). An iterator and an iterable both
implement __iter__() so that both an iterator and an iterable can be used interchangeably in for-statements and in-statements.

So what about __getitem__()? I understand that implementing __getitem__() on a class makes it possible to use the nice syntax "[]" to access data in a
class instance like it's a container. See custom_iterable.py notes
"""

def next_method():
    """
    An iterator is an object that has a next() method (or __next__() method in Python 3). The next() method returns the next element in the
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
    """An iterator also has an __iter__() method, which simply returns itself"""
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