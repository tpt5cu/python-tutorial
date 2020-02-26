# https://numpy.org/doc/1.18/reference/generated/numpy.zeros.html


import numpy as np


'''
Get an ndarray of the specified shape filled with zeros
- The default dtype is np.float_
'''


def create_horizontal_array():
    # 10 columns
    ary = np.zeros(10)
    print(ary)
    print(ary.dtype) # float64


def create_vertical_array():
    # 10 rows, 1 column
    ary = np.zeros((10, 1))
    print(ary)
    # [[0.]
    # [0.]
    # [0.]
    # [0.]
    # [0.]
    # [0.]
    # [0.]
    # [0.]
    # [0.]
    # [0.]]


def create_three_dimensional_array():
    # 50 rows, 100 columns, 2 deep
    ary = np.zeros((50, 100, 2), float)
    print(dir(ary))
    print(ary.shape) # (50, 100, 2)
    print(ary.size) # (10000)
    #print(ary)



if __name__ == '__main__':
    #create_horizontal_array()
    #create_vertical_array()
    create_three_dimensional_array()
