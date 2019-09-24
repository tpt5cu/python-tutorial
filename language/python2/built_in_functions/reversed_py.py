

def iterate_with_reverse_iterator():
    """reversed() is not an in-place operation. It returns a new sequence"""
    my_list = [1, 2, 3, 4, 5]
    new_list = reversed(my_list)
    for e in new_list:
        print(e)
    for e in my_list:
        print(e)


if __name__ == "__main__":
    iterate_with_reverse_iterator()