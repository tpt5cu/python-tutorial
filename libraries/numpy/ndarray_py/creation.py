"""
https://docs.scipy.org/doc/numpy/user/quickstart.html#array-creation
https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html
https://stackoverflow.com/questions/15879315/what-is-the-difference-between-ndarray-and-array-in-numpy
"""


"""
numpy.array is not a real class. It is merely a convenience function for the numpy ndarray.
"""


import numpy as np


def array_convenience_function():
    """
    A numpy ndarray can be created with the array convenience function. The type of the numpy ndarray is inferred from the Python list contents, or it
    can be specified with the "dtype" parameter.
    """
    numbers = np.array([1, 2, 3, 4])
    print(type(numbers)) # <type 'numpy.ndarray'>
    print(numbers.dtype) # int64
    # The array constructor does not accept a list of arguments, only a single "object" argument (the data), along with some keyword arguments that
    # specify metadata
    #error = np.array(1, 2, 3, 4)
    # The array constructor will throw an error if I attempt to coerce the array to a type that doesn't make sense
    #error = np.array(['a', 'b', 'c'], dtype=np.float64)


def multidimensional_ndarray():
    ary = np.array([[1, 2, 3], [4, 5, 6]])
    print(ary)
    print(ary.shape) # (2, 3), meaning 2 rows and 3 column


def jagged_array():
    """
    If I attempt to create a multidimensional ndarray with different inner sequence lengths, I will create a jagged ndarray. numpy will create the
    jagged array, but many operations just won't work. I can tell that an ndarray is jagged by printing it. It will show list([...]) insted of the more
    compact notation.
    """
    ary = np.array([range(1, 10), range(10, 20)])
    print(ary)
    print(ary.shape) # (2,) # 2 elements in a 1-d ndarray
    reshaped = ary.reshape(4, 5)
    print(reshaped)


def fill_with_placeholders():
    """
    Creating an ndarray with placeholder values is more efficient than growing the ndarray later on.
    - ones() is just like zeros() except it fills with 1s
    - empty() is just like zeros() except it fills with whatever is in memory
    """
    # zeros() must be given a shape argument, which is an int or a tuple of ints
    one_d = np.zeros(5)
    print("1-dimensional:")
    print(one_d)
    two_d = np.zeros((5, 5))
    print("\n2-dimensional:")
    print(two_d)
    three_d = np.zeros((5, 5, 5))
    print("\n3-dimensional:")
    print(three_d)


def fill_with_range_of_values():
    """
    The arange ("a-range") function returns a 1-d ndarray that is filled with values in the range of [start, stop). It also accepts a "step" argument
    """
    ary = np.arange(10)
    print(ary) # [1 - 10]
    ary = np.arange(10, step=3) 
    print(ary) # [0, 3, 6, 9]
    ary = np.arange(start=5, stop=15, step=2)
    print(ary) # [5, 7, 9, 11, 13]
    ary = np.arange(start=0, stop=-10, step=-3)
    print(ary) # [0, -3, -6, -9]


def fill_with_single_value():
    """
    full() creates a NEW ndarray of the specified shape with the specified value. <ndarray>.fill() fills an existing ndarray with the
    specified value
    """
    ary = np.full((10,), 77.777) # 1-D array filled with a value
    print(ary)
    ary = np.full((1, 10), 77.777) # 1-D array containing another 1-D array that is filled with a value
    print(ary)



if __name__ == "__main__":
    #array_convenience_function()
    #multidimensional_ndarray()
    #jagged_array()
    #fill_with_placeholders()
    #fill_with_range_of_values()
    fill_with_single_value()