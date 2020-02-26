# https://numpy.org/doc/1.18/reference/generated/numpy.array.html


import numpy as np


'''np.array() can take pretty much any nested sequence to create an ndarray'''


def create_three_dimensional_array():
    '''
    In a 3-D array, there are one or more rows. In the first row, there will be one or more columns. Nothing new so far. What's interesting is that at
    an [r][c] index, instead of getting a number, I get another array! Think of this array as extending backwards in space away from me
    - Don't accidentally create jagged arrays because there is no error and it's just not good
    '''
    ary = np.array(
        [[
            [2, 3],
            [7, 8],
        ]]
    )
    # 1 row, 2 columns, 2 deep
    print(ary.shape) # (1, 2, 2)
    print(ary.dtype) # int64
    # Get the element (i.e. an array) at the first row, first column
    print(type(ary[0][0])) # <class 'numpy.ndarray'>
    print(ary[0][0]) # [2 3]
    # Get the element (i.e. a number) at the first row, first column, 2-deep
    print(type(ary[0][0][1])) # <class 'numpy.int64'>
    print(ary[0][0][1]) # 3
    # Make a jagged array
    ary = np.array(
        [[
            [2, 3],
            [7, 8],
            # This messes up the dimensions and makes an array with 1 row and 3 columns. Actually, it doesn't mess up the dimensions, but the
            # jaggedness of the 3-D array makes it so that NumPy can't report the exact shape. Instead of reporting the exact shape, NumPy just knows
            # that it has a single row with 3 columns, where each column contains some object. That object COULD be a list, or anything else
            [20, 21, 22]
        ]]
    )
    print(ary.shape) # (1, 3)
    print(ary.dtype) # object
    print(type(ary[0][0])) # <class 'list'>
    print(type(ary[0][0][1])) # <class 'int'> 
    print(ary[0][0][1]) # 3


if __name__ == '__main__':
    create_three_dimensional_array()
