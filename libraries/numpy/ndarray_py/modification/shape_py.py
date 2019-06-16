"""
https://docs.scipy.org/doc/numpy/user/quickstart.html#shape-manipulation
"""


import numpy as np


"""
These 3 shape functions all return a new array without modifying the original array
"""

def flatten_ndarray():
    """ An multidimensional ndarray can be flattened into a 1-d array with the ravel() function, which returns a new modified array """
    ary = np.array([range(0, 10), range(10, 20)])
    print(ary)
    print(ary.shape) # (2, 10)
    flat = ary.ravel()
    print(flat)
    print(flat.shape)
    print(flat is ary) # (20,)


def reshape_py():
    """
    As long as the source array has the right number of elements, it can be reshaped into any compatible dimension with the same number of elements.
    """
    ary = np.array([range(0, 12), range(13, 25)])
    print(ary)
    print(ary.shape) # (2, 12)
    reshaped = ary.reshape((6, 4))
    print(reshaped)
    print(reshaped.shape) # (6, 4)


def transpose():
    ary = np.array([range(0, 10), range(10, 20)])
    print(ary)
    print(ary.shape) # (2, 10)
    ary_t = ary.T
    print(ary_t)
    print(ary_t.shape) # (10, 2)
    print(ary is ary_t)


if __name__ == "__main__":
    #flatten_ndarray()
    #reshape_py()
    transpose()