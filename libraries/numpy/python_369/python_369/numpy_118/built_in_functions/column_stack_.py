# https://numpy.org/doc/1.18/reference/generated/numpy.column_stack.html


import numpy as np


'''
np.column_stack() takes a sequence of 1-D arrays and combines each element at the same index from each array into a new array, and it does that for
all elements in every array
- Thus, all of the 1-D arrays must have the same dimensions
'''


def create_two_dimensional_array():
    '''3 arrays with 5 elements each create an array with 5 rows and 3 columns'''
    a = np.array((1, 2, 3, 4, 5))
    #b = np.array((400, 701, 343, 0)) # ValueError
    b = np.array((400, 701, 343, 0, 0))
    c = np.array((6, 7, 8, 9, 10))
    two_d = np.column_stack((a, b, c))
    print(type(two_d)) # <class 'numpy.ndarray'>
    print(two_d.shape) # (5, 3)
    print(two_d)
    # [[  1 400   6]
    # [  2 701   7]
    # [  3 343   8]
    # [  4   0   9]
    # [  5   0  10]]

    


if __name__ == '__main__':
    create_two_dimensional_array()
