# https://docs.python.org/2.7/howto/descriptor.html


import datetime


'''
Put charitably, Python documentation is not great. There are subtleties to the descriptor protocol that are not reflected in the documentation.
- If a class does not implement __get__(), then it is not a descriptor at all
- A data descriptor implements __set__() and/or __delete__()
- If a descriptor implements __get__() and __delete__(), but not __set__(), then
    - It is a data descriptor
    - It is effectively a read-only data descriptor
        - The official way to implement a read-only data descriptor is to implement a __set__() that raises an AttributeError
'''


class ReadOnlyDataDescriptor(object):
    '''
    A read-only data descriptor cannot connect its data to any instance that uses it, because 1) __set__() isn't implemented and 2) the __init__() of
    a data descriptor never knows anything about any possible future instances that might use it
    '''
    def __init__(self):
        # Creation time of the data descriptor, not any class that uses it. Normally, I would never store data in a descriptor itself
        self._creation_time = datetime.datetime.now().strftime('%c')

    def __get__(self, instance, owner):
        return self._creation_time

    def __delete__(self, instance):
        '''
        This method SHOULD delete an attribute off of the instance, but it can do whatever I want. In this case, I remove the descriptor itself!
        - i.e. it should do: del instance.__dict__['_factory_creation_time]
        '''
        #del instance.__class__.__dict__['_factory_creation_time'] # TypeError: can't delete anything directly from a dictproxy
        del instance.__class__._factory_creation_time


class Product(object):
    '''Let's pretend that all products have a read-only timestamp that indicates when the factory started producing products.'''
    _factory_creation_time = ReadOnlyDataDescriptor()

    def __init__(self, name, price):
        self._name = name
        self._price = price


def examine_descriptor_deletion():
    p1 = Product('Suspenders', 15.99)
    print(p1._factory_creation_time) # Fri Nov 15 18:08:55 2019
    #p1._factory_creation_time = datetime.datetime.now() # AttributeError: __set__()
    p2 = Product('Cat_litter', 8.99)
    print(p2._factory_creation_time) # Fri Nov 15 18:08:55 2019
    del p1._factory_creation_time
    #print(p1._factory_creation_time) # AttributeError: missing '_factory_creation_time'


if __name__ == '__main__':
    examine_descriptor_deletion()