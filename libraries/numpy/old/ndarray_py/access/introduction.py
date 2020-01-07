"""
https://docs.scipy.org/doc/numpy/user/basics.indexing.html#indexing - there's more here that isn't covered in these notes (yet)
"""


import numpy as np


array_2d = np.array([[5,3,6], [10,15,5], [15,12,18], [24,10,11], [30,45,30], [85,70,27], [71,80,50], [60,78,99], [55,52,48], [80,91,88],])


def index_outermost_element():
    """ Accessing an element of the highest-level in an array of arbitrary dimensions works as expected """
    print(array_2d[0]) # [5, 3, 6]


def index_innermost_element():
    """ A multidimensional array can have 1 index per axis (i.e. dimension). Each index is separated by a comma. """
    print(array_2d[3, 1]) # 4th row, 2nd element (i.e. 10)


def slice_outermost_elements():
    """ Slicing an array works with [start:stop:step] syntax as with regular Python slicing. """
    print(str(array_2d[0:2]) + "\n") # prints the first two rows of the array, since each row is an item of the outermost array
    print(str(array_2d[::-1]) + "\n") # Reverses the ORDER of the elements in the array. It does not reverse the elements themselves


def slice_innermost_elements():
    """ This looks complicated, but all I'm doing is applying slicing to the outermost and innermost levels of the array """
    print(str(array_2d[5, 0:2]) + "\n") # 6th row, first 2 elements (i.e. [85, 70])
    print(str(array_2d[1:3, 1]) + "\n") # 2nd and 3rd rows, middle element of each row (i.e. [15, 12])
    print(str(array_2d[::-1, ::-1]) + "\n") # Reverse the order of the outermost elements AND reverse each element itself! Crazy!


def regular_index_arrays():
    """
    It turns out that arrays THEMSELVES can be used to index other arrays!
    - Think of each 'index' array as containing a list of partial indexes into the target array.
    - Think of each element in an 'index' array as being a partial index into the target array 
    """
    # I pass 2 index arrays, so I'm passing 2d indexes. Each index array contains 3 values, so I pass 3 2d indexes in total
    print(str(array_2d[[0, 9, 7], [2, 2, 0]]) + "\n") # Return the elements at [0, 2], [9, 2], and [7, 0] (i.e. [6, 88, 60])
    # numpy will try to be smart when I mix an index array and scalar value
    print(str(array_2d[[0, 4, 8], 1]) + "\n") # Examine the 1st, 5th, and 9th rows of the array, and give me the middle element of those row (i.e. [3, 45, 52])
    print(array_2d[[4, 5, 6]]) # Return a NEW array consisting of the 5th, 6th, and 7th rows of the target array


def boolean_index_arrays():
    """
    A boolean array evaluates a true/false expression for every element in an array, and returns an array of the same shape that stores the result of
    every expression.
    When a boolean array of the same shape is used to index another array, the result is ALWAYS a 1D array with indexed elements that matched with a True value. This 1D
    array is a copy of the original data.
    - However, if the boolean array has different dimensions from the array it is indexing, the result isn't always a 1D array
    """
    boolean_array = array_2d > 69
    print(str(boolean_array) + "\n")
    # A 1D array of all values in array_2d that are greater than 69
    print(str(array_2d[boolean_array]) + "\n") 
    # If I took the last column of the boolean_array and transposed it, it would look like what is printed here
    print(str(boolean_array[:, 2]) + "\n") 
    # Examine all rows of the boolean array. For each row, take the last element in that row and insert it into a 1D array. Then, use that 1D array to
    # index array_2d. Since array_2d has more dimensions than the 1D array, the result contains all rows of array_2d that were matched with a True value.
    print(array_2d[boolean_array[:, 2]]) 


if __name__ == "__main__":
    print(str(array_2d) + "\n")
    #index_outermost_element()
    #index_innermost_element()
    #slice_outermost_elements()
    #slice_innermost_elements()
    #regular_index_arrays()
    boolean_index_arrays()