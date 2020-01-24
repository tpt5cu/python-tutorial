# https://docs.python.org/3/library/functions.html#sorted


'''
Return a new sorted list from the items in iterable.
- <list>.sort() is in-place, not sorted()
'''


def sort_iterable():
    '''sorted() will consume a view object (which is iterable) just fine without creating a list from the view object'''
    inTree = {
        '1': 'foo',
        '2': 'bar',
        '3': 'baz'
    }
    list_ = sorted(inTree.keys(), key=int)
    print(list_) # ['1', '2', '3']


if __name__ == '__main__':
    sort_iterable()