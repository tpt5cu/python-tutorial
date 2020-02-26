# https://numpy.org/doc/1.18/reference/generated/numpy.arange.html


import numpy as np


'''numpy.arange() returns an ndarray of the given <start>, [stop], [step], and [dtype]'''

def get_ascending_ndarray():
    '''A single argument provides the exclusive max bound for a single-stepped ascending array'''
    a = np.arange(100)
    print(a) # [1, 2 ..., 99]


def get_ascending_stepped_ndarray():
    ascending = np.arange(0, 10, 2)
    print(type(ascending)) # <class 'numpy.ndarray'>
    print(ascending) # [0 2 4 6 8]


def get_descending_stepped_ndarray():
    descending = np.arange(10, 0, -2)
    print(descending) # [10  8  6  4  2]


if __name__ == '__main__':
    get_ascending_ndarray()
    #get_ascending_stepped_ndarray
    #get_descending_stepped_ndarray()
