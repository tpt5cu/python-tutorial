# https://docs.python.org/3/tutorial/classes.html - surprisingly unhelpful resource
# https://portingguide.readthedocs.io/en/latest/classes.html
# https://stackoverflow.com/questions/1123000/does-python-have-anonymous-classes


from collections import namedtuple as nt
from types import SimpleNamespace as sn


class Road:
    '''The "object" is the default superclass of all classes in Python 3'''

    def __init__(self, length, width, material):
        self.length = length
        self.width = width
        self.material = material


def examine_road():
    r = Road(10, 10, 'asphalt')
    print(dir(r)) # Has all of the attributes of the Python "object"
    print(isinstance(r, object)) # True


def anonymous_namedtuple_class():
    '''Instances of a namedtuple do not have an implicit __dict__'''
    anonymous_class = nt('MyClass', 'age')
    print(anonymous_class) # <class '__main__.MyClass'>
    o = anonymous_class(14)
    print(o) # MyClass(age=14)
    #o.name = 'Chuck' # AttributeError: 'MyClass' object has no attribute 'name'


def anonymous_simplenamespace_object():
    '''Instances of a SimpleNamespace class do have an implicit __dict__. Instances of SimpleNamespace are anonymous custom objects'''
    o = sn()
    o.name = 'Bill'
    print(o) # namespace(name='Bill')
    print(type(o)) # <class 'types.SimpleNamespace'>


if __name__ == '__main__':
    examine_road()
    #anonymous_namedtuple_class()
    #anonymous_simplenamespace_object()
