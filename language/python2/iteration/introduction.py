# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration


def examine_iterable():
    """
    An iterable has an __iter__ method that returns an iterator, OR it defined a __getitem__ method that can take sequential index values starting
    from 0.
    """
    my_list = ["a", "b", "c", "d"]
    iterator = my_list.__iter__
    print(type(iterator)) # <type 'method-wrapper'>
    iter(my_list)


if __name__ == "__main__":
    examine_iterable()