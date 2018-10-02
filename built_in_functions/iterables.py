# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration


def use_an_iterable():
    """An iterable is an object that has 1) an __iter__ method which returns an iterator and/or 2) a __getitem__ method that
    takes indexes.
    A list is an iterable since it has both of these methods.
    """
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)
    print(dir(my_list))


if __name__ == "__main__":
    use_an_iterable()
