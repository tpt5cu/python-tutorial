

def list_access():
    """Lists are accessed just like strings."""
    my_list = [10, 20, 30, 40, 50]
    print('The 3rd element is: ' + str(my_list[2]))
    print('This list has ' + str(len(my_list)) + ' elements.')


def list_concatenation():
    """The + operator concatenates two lists, just like strings!"""
    list_a = ['cat', 'dog']
    list_b = ['man', 'frog']
    list_a += list_b
    print(list_a)


def list_purpose():
    """Lists are typically used to store homogeneous collections of items. However, they are appropriate whenever
    a mutable, ordered sequence is needed.
    """
    # a homogeneous collection of ints
    my_list = [4, 5, 1, 4, 55, 6, 0]
    # lists are mutable (their contents can be changed)
    my_list[5] = 100000
    print(my_list)


def list_traversal_1():
    """List traversal can be tricky sometimes."""
    my_list = [3.0, 5.44, 99.9, 2]
    for elm in my_list:
        """In this example, the list contains immutable objects. Therefore, __add__ is being called for each object.
        Therefore, the 'elm' variable is being made to point at a NEW object that is returned from the operation. Hence,
        the original elements of the list aren't being modified in place at all.
        """
        elm += 5
        print(elm)
    print(my_list)


def list_traversal_2():
    """If I want to change immutable objects in a list (which is possible because a list itself is a mutable object),
    I have to access the indexes of the list. A regular for-in loop won't work because the resulting iterator will
    be giving me a reference directly to each (immutable) element.
    """
    my_list = [4, 3, 5, 77, 9, 1]
    """This is bad practice even though it works. Use enumerate() instead."""
    # for idx in range(0, len(my_list)):
    #     my_list[idx] = my_list[idx] + 5
    # print(my_list)
    """Actually this is bad practice too. I should use a list comprehension."""
    for idx, elm in enumerate(my_list):
        my_list[idx] = elm + 5
    print(my_list)


if __name__ == "__main__":
    # list_access()
    # list_concatenation()
    # list_purpose()
    # list_traversal_1()
    list_traversal_2()