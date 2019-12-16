# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/


from contextlib import contextmanager


"""It is possible to write a class that can be used as a decorator AND as a context manager. See the link"""


# Numbers are immutable, so think of a better example
@contextmanager
def prepend_element_to_list(my_list):
    """
    A generator function can be decorated to become a context manager. Everything before the "yield" statement is __enter__() and everything after the
    "yield" statement is __exit__. Super easy!
    """
    # __enter__()
    my_string = "Inside context manager"
    my_list.insert(0, my_string) # "as" expression value
    yield my_list
    # __exit__()
    my_list.remove(my_string)


def use_context_manager():
    my_list = ['a', 'b', 'c']
    with prepend_element_to_list(my_list) as modified_list:
        print(my_list is modified_list) # True
        print(modified_list)
    print(my_list)


if __name__ == "__main__":
    use_context_manager()