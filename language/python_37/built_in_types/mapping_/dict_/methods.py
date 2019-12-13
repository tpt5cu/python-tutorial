# https://stackoverflow.com/questions/13998492/when-should-iteritems-be-used-instead-of-items
# https://docs.python.org/3/library/stdtypes.html#dict-views


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


if __name__ == '__main__':
    key_iteration()