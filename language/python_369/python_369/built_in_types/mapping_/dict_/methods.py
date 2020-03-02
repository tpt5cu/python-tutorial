# https://stackoverflow.com/questions/13998492/when-should-iteritems-be-used-instead-of-items
# https://docs.python.org/3.6/library/stdtypes.html#dict-views
# https://stackoverflow.com/questions/6777485/modifying-a-python-dict-while-iterating-over-it


'''
- As of 3.7, CPython dict iteration order is guaranteed to be the insertion order (but don't rely on this, just use an OrderedDict)
- In Python 3:
    - <dict>.keys(), <dict>.items(), and <dict>.values() all return a view object, which is also iterable
    - Thus, iterkeys(), iteritems(), itervalues(), viewkeys(), viewitems(), viewvalues() don't exist
'''


def key_iteration():
    '''
    Python 3 <dict>.keys() returns a view object instead of a list, specifically a <class 'dict_keys'>. What's important is that:
    - A view object always reflects (but doesn't contain) the current internal state of its dict
    - It must be iterated over
        - It cannot be indexed
    - It supports membership tests, including set membership tests, and length membership
    - A RuntimeError or undefined behavior can result if the dictionary is modified during iteration
    - It cannot directly modify the dictionary through assignment nor deletion

    A view object is not an iterator, but it is an iterable.
    '''
    my_dict = {
        'yarn': 'dollar',
        'thread': 'yen'
    }
    #print(my_dict.keys()[0]) # TypeError: 'dict_keys' object is not subscriptable
    print(len(my_dict.keys())) # 2
    print(type(my_dict.keys())) # <class 'dict_keys'>
    print(my_dict.keys().__iter__()) # <dict_keyiterator object at ...>
    for k in my_dict.keys():
        #del my_dict['yarn'] # RuntimeError
        print(k) # yarn\nthread
    # This is an example of a membership test
    print('ball' in my_dict.keys()) # False
    # I must use the explicit list() constructor if I want a separate list of keys
    print(list(my_dict.keys())) # ['yarn', 'thread']
    # There is no such thing as iterkeys() anymore
    #print(my_dict.iterkeys()) # AttributeError
    #print(my_dict.viewkeys()) # AttributeError


def modify_during_iteration():
    '''
    It is obvious that I should not delete or add items to a dictionary while iterating over it, but what about reassigning items?
    - Stack Overflow:
      (https://stackoverflow.com/questions/2315520/in-python-how-do-i-loop-through-the-dictionary-and-change-the-value-if-it-equal/2315529#2315529)
      says it is okay to modify existing entries of a dict while iterating over it
    - It's always fine to iterate over a list of the dict's keys and modify the dict that way, since I'm not iterating over the dict itself
    '''
    pass


def sort_dicts():
    '''
    Dicts can be sorted by converting their entire contents into strings and then comparing those strings lexicographically
    - I think it would be better to sort by a particular key, but this is allowed...
    '''
    d1 = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'name': 'One'
    }
    d2 = {
        '1': 'b',
        'c': 'c',
        'd': 'd',
        'name': 'Two'
    }
    d3 = {
        'a': '1',
        'c': 'c',
        'd': 'd',
        'name': 'Three'
    }
    unsorted_list = [d3, d1, d2]
    # [{'a': '1', 'c': 'c', 'd': 'd', 'name': 'Three'}, {'a': 'a', 'c': 'c', 'b': 'b', 'name': 'One'}, {'1': 'b', 'c': 'c', 'd': 'd', 'name': 'Two'}]
    print(unsorted_list) 
    sorted_ = sorted(unsorted_list, key=lambda d: str({val: d[val] for val in d if val != 'name'})) 
    # [{'1': 'b', 'c': 'c', 'd': 'd', 'name': 'Two'}, {'a': '1', 'c': 'c', 'd': 'd', 'name': 'Three'}, {'a': 'a', 'c': 'c', 'b': 'b', 'name': 'One'}]
    print(sorted_)
    #sorted_ = sorted([d1, d2], key=lambda d: {val: d[val] for val in d if val != 'name'}) # TypeError: '<' not supported between instances of 'dict'
    #and 'dict'
    

def update_():
    '''
    <dict>.update() accepts a variety of arguments to update the values in the dictionary
    - The original dictionary is updated in place
    - None is returned
    - key-values pairs are overwritten or not modified, but never removed
    '''
    original = {
        'foo': 'bar',
        'nice': 'job',
        3: 4
    }
    original.update({'foo': 'fru', 'nice': 'wow'})
    #print(original) # {'foo': 'fru', 'nice': 'wow', 3: 4}
    # Here we see the problem of using numbers as keys!
    #original.update(3='what?!', nice=no) # SyntaxError
    # A dict and kwargs can be used together
    original.update({3: 'what?!'}, nice='no')
    #print(original) # {'foo': 'bar', 'nice': 'no', 3: 'what?!'}
    # Only an ITERABLE of key-values pairs is allowed, not a plain tuple
    #original.update(('foo', 'boo')) # ValueError
    original.update((('foo', 'boo'),))
    #print(original) # {'foo': 'boo', 'nice': 'job', 3: 4}


if __name__ == '__main__':
    #key_iteration()
    #sort_dicts()
    update_()
