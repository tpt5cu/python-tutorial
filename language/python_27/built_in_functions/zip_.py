# https://docs.python.org/2/library/functions.html#zip


'''
zip() merges two sequences/iterables into a single list, where each element of the list is a tuple contains two elements that were at identical
indexes in the sequences
- A longer sequence won't have its extra elements included
'''


def combine_lists():
    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    c = zip(a, b)
    print(type(c)) # <type 'list'>
    print(c) # [(1, 4), (2, 5), (3, 6)]


if __name__ == '__main__':
    combine_lists()