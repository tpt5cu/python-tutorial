# https://docs.python.org/2/library/functions.html#filter

'''
filter() now returns an iterable (a filter object) instead of whatever type it used to return
- Like a map, a filter must be iterated over to get the filtered result
'''


def filter_list():
    numbers = [1, 2, 3, 4, 5]
    less_than = filter(lambda x: x <=3, numbers)
    print(less_than) # <filter object at ...>
    print(type(less_than)) # <class 'filter'>
    print(list(less_than)) # [1, 2, 3]


def filter_tuple():
    booleans = (True, False, False, False, True, -1, 0, 1, 2, '', 'yay')
    # filter() when function = None simply returns an element if it is True (i.e. also return non-zero numbers, non-empty strings)
    truthy = filter(None, booleans)
    print(truthy) # <filter object at ...>
    print(type(truthy)) # <class 'filter'>
    print(list(truthy)) # [True, True, -1, 1, 2, 'yay']


def filter_string():
    sentence = 'The quick brown fox jumped over the lazy dog'
    # Captials come before lowercase
    new_sentence = filter(lambda c: c < 'm', sentence)
    print(new_sentence) # <filter object at ...>
    print(type(new_sentence)) # <class 'filter'>
    print(''.join(new_sentence)) # The ick b f jed e he la dg


def filter_opposite():
    items = [5, 4, 3, 2, 1]
    filtered_items = filter(lambda e: not e < 3, items)
    print(filtered_items) # <filter object at ...>
    print(list(filtered_items)) # [5, 4, 3]


if __name__ == '__main__':
    #filter_list()
    #filter_tuple()
    #filter_string()
    filter_opposite()