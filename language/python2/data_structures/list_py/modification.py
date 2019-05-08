"""
https://docs.python.org/2.7/tutorial/datastructures.html
"""

def append_py():
    """ list.append() adds an element to the end of the list in-place. """
    my_list = [1, 2, 3]
    my_list.append(4)
    # append() only accepts a single argument
    #my_list.append(5, 6)
    my_list.append([5, 6])
    print(my_list) #[1, 2, 3, 4, [5, 6]] This is not what I want


def extend_py():
    """ extend() only takes 1 argument, but the elements inside of that argument are appended to the list directly. """
    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    print(my_list) #[1, 2, 3, 4, 5] This is what I want

if __name__ == "__main__":
    append_py()
    #extend_py()