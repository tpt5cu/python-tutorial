# https://docs.python.org/2/reference/datamodel.html#slots
# https://stackoverflow.com/questions/472000/usage-of-slots - Insane answer. I don't even need to take notes


'''
__slots__ is an optional class attribute that is used to make code more efficient. It is not necessary to use at all.
- __slots__ declares a precise set of attributes that each instance allocates space for, as opposed to having an instance __dict__ that can store
  anything
- For every instance of the class, it replaces the large __dict__ with the smaller __slots__ attribute
    - Actually, a __dict__ is only created the first time an object is accessed for efficiency
- Slots use data descriptors like properties, called "members" (e.g. <class 'member_descriptor'>)
'''

class Aardvark(object):
    '''The __slots__ attribute can hold ANY sequence'''

    # Now an Aardvark instance has space for a 'tongue', but doesn't actually have a tongue
    __slots__ = 'tongue', 

    def __init__(self):
        self.tongue = '==>'


def create_aardvark():
    av = Aardvark()
    print(type(av.tongue)) # <type 'str'>
    print(type(Aardvark.tongue)) # <type 'member_descriptor'>
    print(type(Aardvark.__slots__)) # <type 'tuple'>
    # Cannot add arbitrary attributes, unless I included __dict__ in __slots__
    #av.feet = 'vv-vv' # AttributeError


if __name__ == '__main__':
    create_aardvark()
