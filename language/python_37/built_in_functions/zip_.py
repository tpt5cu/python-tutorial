# https://docs.python.org/2/library/functions.html#zip


'''zip() now return an iterator'''


def combine_lists():
    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    c = zip(a, b)
    print(type(c)) # <class 'zip'>
    print(c) # <zip object at ...>
    print(list(c)) # [(1, 4), (2, 5), (3, 6)]


if __name__ == '__main__':
    combine_lists()