# https://docs.python.org/3/whatsnew/3.0.html


'''
The built-in basestring abstract type was removed. Use str instead. The str and bytes types don’t have functionality enough in common to warrant a
shared base class. The 2to3 tool (see below) replaces every occurrence of basestring with str.
'''


def examine_subclasses():
    '''
    - str is of course a subclass of itself

    '''
    print(issubclass(str, str)) # True
    print(issubclass(bytes, str)) # False
    print(issubclass(str, bytes)) # False
    print(issubclass(bytearray, str)) # False
    print(issubclass(str, bytearray)) # False
    print(issubclass(bytes, bytearray)) # False
    print(issubclass(bytearray, bytes)) # False


def examine_baseclasses():
    '''
    The __base__ and __bases__ attributes are directy attributes of only class objects
    - The only base class of str is object
    '''
    print(str.__base__) # <class 'object'>
    print(str.__bases__) # (<class 'object'>,)
    print(str.__class__.__bases__) # (<class 'object'>,)


if __name__ == '__main__':
    #examine_subclasses()
    examine_baseclasses()
