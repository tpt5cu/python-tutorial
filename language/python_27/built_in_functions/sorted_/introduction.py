# https://docs.python.org/2/library/functions.html#sorted
# https://docs.python.org/3/howto/sorting.html#sortinghowto



import operator


'''
The sorted() function returns a NEW sorted LIST from the items in the iterable and is guaranteed to be stable
- If it doesn't seem stable, it's because my code is multiple sorts going on that are influencing each other
'''


def get_data():
    data = [
        ['hourly', '2000', 'Alaska', 8760, 5000, 3760],
        ['hourly', '2001', 'Alabama', 8760, 4001, 4760],
        ['hourly', '2001', 'Maine', 8760, 2999, 5760],
        ['hourly', '2000', 'Maine', 8760, 3000, 5760],
        ['hourly', '2001', 'Alaska', 8760, 5001, 3760],
        ['hourly', '2001', 'Virginia', 8760, 4001, 4760],
        ['hourly', '2000', 'Virginia', 8760, 4000, 4760],
        ['hourly', '2000', 'Alabama', 8760, 4000, 4760]
    ]
    return data


def sort_ints():
    my_set = set([6, 456, 234, 52475, 367, 234, 3542, 362, 5672, 6])
    print(sorted(my_set)) # [6, 234, 362, 367, 456, 3542, 5672, 52475]


def sort_strings():
    '''As expected, strings are sorted in ASCII order: capital letters come before lowercase, longer strings come after shorter strings.'''
    strings = ['Austin', 'apple', 'ardvark', 'Astronomy', 'amazing', 'add', 'ankle', 'Ankle', 'anaconda', 'ashes', 'ash']
    print(sorted(strings)) # ['Ankle', 'Astronomy', 'Austin', 'add', 'amazing', 'anaconda', 'ankle', 'apple', 'ardvark', 'ash', 'ashes']


def custom_cmp_by_year(e1, e2):
    '''
    - This sorting function IS stable. I tested it by comparing "list objects" solely by year. When I did this, equal list objects preserved their
      input ordering
        - This is true!
    '''
    if e1[1] == e2[1]:
        return 0
    elif e1[1] < e2[1]:
        return -1
    else:
        return 1


def custom_cmp_by_year_validcount_name(e1, e2):
    '''
    - I'm not sorting "first" by anything, unlike the _index_multisort(). I'm comparing multiple "attributes" of each "list object" to determine if
      one is greater than the other
    '''
    # sort by year first
    if e1[1] == e2[1]: # years are equal
        if e1[4] == e2[4]: # valid counts are equal
            if e1[2] < e2[2]:
                return -1
            else:
                return 1
        elif e1[4] < e2[4]:
            return 1
        else:
            return -1
    elif e1[1] < e2[1]:
        return -1
    else:
        return 1


def index_multisort(xs, specs):
    '''
    This function is based on the documentation to allow for sorting lists, where each element of the list can have multiple keys and where each
    key can have a specific ordering
    '''
    # - This is a for-loop because each Timsort runs a single sorting pass for each key
    #   - <list>.sort() is in-place
    # - The specs are reversed because 1) the specs are assumed to be passed in order of decreasing importance and 2) the most important sorting
    #   key must be used last so that it trumps any ordering created by other keys
    for key_idx, reverse in reversed(specs):
        # reverse is a bool which if True indicates sorting should be done in descending order
        xs.sort(key=operator.itemgetter(key_idx), reverse=reverse)
    return xs


if __name__ == '__main__':
    #sort_ints()
    sort_strings()