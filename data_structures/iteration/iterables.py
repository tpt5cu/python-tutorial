# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration

"""These are all iterable:
list
string
dict
tuple
set
anything else?
"""


def what_is_iterable():
    #it = (1, 2, 3)
    #it = [1 ,2, 3]
    #it = "123"
    #it = {1: "yay", 2: "boo", 3: "cool"}
    # This is a set
    it = {1, 2, 3}
    for x in it:
        print(x)


def use_an_iterable():
    """An iterable is an object that has 1) an __iter__ method which returns an iterator and/or 2) a __getitem__ method that
    takes indexes. You GET an iterator FROM an iterable.

    A list is an iterable since it has both of these methods.
    """
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)
    print(dir(my_list))


if __name__ == "__main__":
    what_is_iterable()
    #use_an_iterable()
