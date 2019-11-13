# https://docs.python.org/2/reference/datamodel.html#object.__cmp__ - describes default comparison behavior


def compare_objects():
    '''
    If no __cmp__(), __eq__(), nor __ne__() operation is defined, class instances are compared using their object identities (i.e. id())
    - Since no comparison operation is defined for <type 'object'> instances, such instances must be compared based on their object identity, which is
      a number that is related to their memory address in C-Python
    - As a result, the output of the comparison expressions will change depending on the relative order of initialization of o1 vs. o2! It just
      happens to be an implementation detail (as far as I can tell) that an object created first will have a lesser id than an object created later 
    '''
    o2 = object()
    print(type(o2)) # <type 'object'>
    print(id(o2))
    o1 = object()
    print(id(o1))
    # The results of these expressions depend on the order of object initialization!
    print(o1 < o2) # True, False
    print(o1 > o2) # False, True
    print(o1 == o2) # False, False


class Laptop(object):

    def __init__(self, price, color):
        self.price = price
        self.color = color

    def __cmp__(self, other):
        '''__cmp__() is only invoked if a relevant rich comparison operator isn't defined.'''
        print('Invoked __cmp__()')
        return self.price - other.price

    def __eq__(self, other):
        return self.price != other.price


def compare_laptops():
    acer = Laptop(700, 'orange')
    toshiba = Laptop(800, 'purple')
    # __cmp__() was invoked because no __lt__() method is defined for Laptop instances
    print(toshiba < acer) # False
    print(toshiba == acer) # True
    # __cmp__() was invoked
    print(toshiba > acer) # True


if __name__ == '__main__':
    #compare_objects()
    compare_laptops()