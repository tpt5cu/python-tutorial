# https://docs.python.org/2/library/functions.html#filter


'''filter() is shorthand for [item for item in iterable if <condition>]. There does not appear to be any reference to indexes. It is very versitile!'''


def filter_list():
    '''filtering any iterable (except a string or tuple) will return a list '''
    numbers = [1, 2, 3, 4, 5]
    less_than = filter(lambda x: x <=3, numbers)
    print(less_than) # [1, 2, 3]
    print(type(less_than)) # <type 'list'>


def filter_tuple():
    '''filtering a tuple always returns a tuple'''
    booleans = (True, False, False, False, True, -1, 0, 1, 2, '', 'yay')
    # filter() when function = None simply returns an element if it is True (i.e. also return non-zero numbers, non-empty strings)
    truthy = filter(None, booleans)
    print(truthy) # (True, True, -1, 1, 2, 'yay')
    print(type(truthy)) # <type 'tuple'>


def filter_string():
    '''filtering a string always returns a string'''
    sentence = 'The quick brown fox jumped over the lazy dog'
    # Captials come before lowercase
    new_sentence = filter(lambda c: c < 'm', sentence)
    print(new_sentence) # The ick b f jed e he la dg
    print(type(new_sentence)) # <type 'str'>


def filter_opposite():
    items = [5, 4, 3, 2, 1]
    filtered_items = filter(lambda e: not e < 3, items)
    print(filtered_items) # [5, 4, 3]


if __name__ == '__main__':
    #filter_list()
    #filter_tuple()
    filter_string()
    #filter_opposite()