def sort_a_set():
    '''By definition, sets are unsorted. However, it is legal to pass a set to sorted() to get a sorted list'''
    set_ = {5, 1, 2, 3, 4, 4}
    print(set_) # {1, 2, 3, 4, 5}
    set_ = sorted(set_)
    print(set_) # [1, 2, 3, 4, 5]


if __name__ == '__main__':
    sort_a_set()