

def compare_objects():
    '''
    - There is no __cmp__() in Python 3, hence there is no simple comparison
    - In Python 3, objects cannot be compared using <, <=, >, >= by default. Thus, the special comparison operators only work if the relevant rich
      comparison methods have been defined for an object
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