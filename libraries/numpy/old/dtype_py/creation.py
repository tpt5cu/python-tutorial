"""
https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#arrays-dtypes - introduction
https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html - dtype constructor
"""


import numpy as np


def built_in_types():
    """
    Frequently, I don't need to use the dtype constructor because any of the built-in numpy type object can be used in place of a dtype object. I can
    use these built in type objects (which aren't technically dtype objects themselves) wherever a dtype object is needed.
    """
    # Here I am using a scalar type object in place of a "real" dtype object
    numbers = np.array([1, 2, 3, 4, 5], dtype=np.float_)
    print(numbers)
    print(numbers.dtype) # float64
    print(type(numbers[0])) # numpy.float64
    # I can force numpy to treat the array as an array of Python objects (which point to Python ints) instead of an array of numpy floats
    objects = np.array([1, 2, 3, 4, 5], dtype=np.object_)
    print(objects)
    print(objects.dtype) # object
    print(type(objects[0])) # int


if __name__ == "__main__":
    built_in_types()