

def iterate_with_reverse_iterator():
    """ This works as expected """
    my_list = [1, 2, 3, 4, 5]
    my_list = reversed(my_list)
    for e in my_list:
        print(e)


if __name__ == "__main__":
    iterate_with_reverse_iterator()