# https://docs.python.org/2/library/functions.html#reversed
# https://stackoverflow.com/questions/3266180/can-iterators-be-reset-in-python


'''Iterators cannot be reset in Python. Once it has been consumed, it is gone'''


def inspect_reversed():
    '''reversed() does NOT return a usable reversed object. It returns a reverse iterator!'''
    sentence = 'Hello there General Kenobi!'
    ri = reversed(sentence)
    print(type(ri)) # <type 'reversed'>
    print(ri) # <reversed object at 0x...>
    

def get_reversed_object():
    '''Once an iterator is iterated over, it has been consumed. That's why I can't pass 'new' list to multiple factory functions'''
    my_list = [1, 2, 3, 4, 5]
    new_list = reversed(my_list)
    print(new_list) # <listreverseiterator object at 0x...>
    # This consumes the iterator entirely
    print(list(new_list)) # [5, 4, 3, 2, 1]
    # This will be an empty tuple because the iterator has been consumed
    print(tuple(new_list))


if __name__ == '__main__':
    #inspect_reversed()
    get_reversed_object()