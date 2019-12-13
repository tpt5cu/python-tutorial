# https://rszalski.github.io/magicmethods/
# https://docs.python.org/2.7/reference/datamodel.html#emulating-container-types
# https://portingguide.readthedocs.io/en/latest/core-obj-misc.html


import random


'''This class demonstrates that simple key access and slice access all filter through __getitem__, __setitem__, and __delitem__'''


class Pizza(object):

    def __init__(self, name, toppings, slice_count):
        self._name = name
        self._slices = [['{} * {}'.format(t, random.randint(0, 10)) for t in toppings] for i in range(slice_count)]

    def __len__(self):
        return len(self._slices)

    def __getitem__(self, key):
        '''Defines self[key]'''
        return self._slices[key]

    def __setitem__(self, key, value):
        self._slices[key] = value
    
    def __delitem__(self, key):
        del self._slices[key]

    def __repr__(self):
        return repr(self._slices)
    

def eat_pizza():
    '''
    As long as I'm using a built-in sequence type under the hood, implementing my own container is really easy. If I don't use a built-in sequence,
    then this would be much harder
    '''
    p = Pizza('Meat Lovers', ('pepperoni', 'sausage'), 16)
    print(p[10]) # ['pepperoni * 2', 'sausage * 4']
    print(p[13]) # ['pepperoni * 4', 'sausage * 10']
    print(p[0:3:2]) # [['pepperoni * 6', 'sausage * 10'], ['pepperoni * 2', 'sausage * 9']]
    del p[6:16]
    p[0] = ['pinapple * 100']
    print(len(p)) # 6
    print(p) # [['pinapple * 100'], ['pepperoni * 0', 'sausage * 3'], ['pepperoni * 2', 'sausage * 9'], ['pepperoni * 1', 'sausage * 10'], ['pepperoni * 7', 'sausage * 6'], ['pepperoni * 9', 'sausage * 4']]
    #print(p[7]) # IndexError: list index out of range


if __name__ == '__main__':
    eat_pizza()