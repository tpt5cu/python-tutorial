'''There is no __cmp__() in Python 3, hence there is no simple comparison'''


def compare_objects():
    '''
    In Python 3, objects cannot be compared using <, <=, >, >= by default.
    - == and != work just fine and use an object's id() just like in Python 2. 
    '''
    o2 = object()
    print(type(o2)) # <class 'object'>
    print(id(o2))
    o1 = object()
    print(id(o1))
    #print(o1 < o2) # TypeError
    #print(o1 > o2) # TypeError
    print(o1 == o2) # False
    print(o1 != o2) # True


if __name__ == '__main__':
    compare_objects()