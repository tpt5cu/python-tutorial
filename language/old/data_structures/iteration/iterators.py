# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration


def get_an_iterator():
    """An iterator is merely an object with a __next__ method (or a next method in Python2)
    Whenever I use a for-loop, map, list comprehension, etc., the next method is called automatically to get each
    item from the iterator.
    """
    my_list = ['a', 'b', 'c', 'd']
    iterator = iter(my_list)
    print(type(iterator))
    print(dir(iterator))


def use_manual_iterator():
    """Normally, iterators are used transparently in things like for-loops, but I can manually
    manipulate an iterator if I want.
    """
    my_list = ['a', 'b', 'c', 'd']
    iterator = iter(my_list)
    while True:
        try:
            """Get the next element with the built-in next() function. The built-in next() function just invokes the
            __next__ method of the iterator.
            """
            element = next(iterator)
            # element = iterator.next__()
            print("I got this element: " + str(element))
        except StopIteration:
            """If StopIteration is raised, break from loop. 
            This exception is raised when there are no more elements.
            """
            break


def reset_iterator():
    """Python does not have an explicit method to reset an iterator. Proper practice is to just create a new iterator.
    However, there are some workarounds:
    https://stackoverflow.com/questions/3266180/can-iterators-be-reset-in-python
    """


def modify_during_iteration():
    """A (mutable) collection is NOT supposed to have items removed or added to it during iteration.

    In this first example, the iterator returns the first element (0) and the if-statement confirms 0 < 10. Next, 0 is
    passed as an argument to remove(), which then scans the list and finds the first element with a value of 0 and
    removes it. Now, the element with a value of 1 is the first element in the list with an index of 0. But the iterator
    already examined the element at index 0, so it moves on to index 1. The element at index 1 is now 2, so 2 is removed, etc.
    """
    numbers = list(range(0, 20))
    for num in numbers:
        if num < 10:
            numbers.remove(num)
    print(numbers)
    """This works fine, but it's still bad practice"""
    numbers = list(range(0, 20))
    for num in numbers:
        if num < 10:
            numbers.append(77)
    print(numbers)


def infinite_loop():
    """This results in an infinite loop."""
    numbers = list(range(0, 20))
    for num in numbers:
        if num > 10:
            numbers.append(77)
    print(numbers)


if __name__ == "__main__":
    """I just noticed that indentation amount only depends on context. I could indent one function by 1 space and a separate
    function with 3 spaces as long as I'm consistent in each function.
    """
    # get_an_iterator()
    # use_manual_iterator()
    # modify_during_iteration()
    infinite_loop()
