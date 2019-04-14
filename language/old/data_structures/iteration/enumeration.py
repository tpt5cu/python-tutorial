# https://www.programiz.com/python-programming/methods/built-in/enumerate


def get_enumerate_object():
    """The enumerate function expects an iterable object and returns an enumerate object (i.e. an enumerator). This
    enumerator is essentially a list [] that contains tuples (), where each tuple contains an int (that can be treated
    as an index) and an element from the original iterable collection. The enumerate class is NOT the same as any
    variety of iterator class.
    """
    names = ['austin', 'david', 'mary', 'louise']
    enumerate_names = enumerate(names)
    print(type(enumerate_names))
    print(list(enumerate_names))
    """The enumerator object can be made to start at a different number than 0."""
    enumerate_names_again = enumerate(names, 11)
    print(list(enumerate_names_again))


def use_enumerator():
    """An enumerator can be used to modify a collection that is also a mutable object
    (i.e. list, set, and dict but NOT tuple).

    In this example, I print the strings in the list, then modify the list itself to contain new strings.
    """
    names = ['chuck', 'joe', 'chang', 'dude']
    for idx, elm in enumerate(names):
        print(elm)
        names[idx] = 'Really???'
    print(names)


if __name__ == "__main__":
    #get_enumerate_object()
     use_enumerator()
