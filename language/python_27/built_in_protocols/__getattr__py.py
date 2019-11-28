# https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88


'''
__getattr__() is not part of the descriptor protocol, but it can have a fundamental impact on attribute lookup, so these notes are stored near the
descriptor protocol
'''


class Dummy(object):

    def __init__(self, weight):
        self._weight = weight

    def __getattr__(self, attr):
        '''This method is only invoked if a nonexistent attribute is accessed on a instance of this class'''
        return 'Not an attribute'


def reference_nonexistent_attribute():
    '''Deleting an attribute from an object does make it so that __getattr__() will be called'''
    d = Dummy(45)
    print(d.foobar) # Not an attribute
    print(d._weight) # 45
    del d._weight
    print(d._weight) # Not an attribute
 

if __name__ == '__main__':
    reference_nonexistent_attribute()