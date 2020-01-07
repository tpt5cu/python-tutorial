"""
https://www.jessicayung.com/numpy-views-vs-copies-avoiding-costly-mistakes/
https://scipy-cookbook.readthedocs.io/items/ViewsVsCopies.html
"""


import numpy as np


"""
A view of an array is a presentation of the original data. Hence, modifying a view WILL modify the original data. A view can be obtained by:
- Slicing an array
- Using the view() function - view the original data in a different way by retinterpreting the SAME bytes of data
    - view() can be specified with a dtype
        - If the original dtype is a different length from the specified dtype, be careful! Printing such a representation can be misleading
    - view() can be specified with an ndarray subclass
        -  While an ndarray subclass is returned, the new ndarray is still presenting the same bytes in memory 
- Using the ravel() function to return a contiguous 1D array (a copy is made "only if needed" whatever that means)
"""


"""
A copy of an array is a completely new array in memory. A copy can be obtained by:
- Using index arrays (i.e. "fancying indexing")
- Using the as_type() function
- Using the flatten() function
"""


def slice_view():
    """ Slicing can be used for modifying the original data, since the slice IS the original data """
    ary = np.arange(30).reshape(5,6) # 5 rows, 6 columns
    print(str(ary) + "\n")
    print(str(ary[2:4]) + "\n") # print the 3rd and 4th rows of the array
    # The result of assigning a scalar value to some slice of the data is fairly intuitive
    ary[2:4] = 5 # the 3rd and 4th rows become filled with 5s
    print(str(ary) + "\n")
    # Error
    #ary[2:4] = (5, 6)
    # Error
    #ary[2:4] = [1, 2, 1, 2, 0]


def index_array_copy():
    """
    If I index an array with an 'index array' (including boolean index arrays), then the returned value is a COPY of the original array
    """
    ary = np.arange(30).reshape(5,6) # 5 rows, 6 columns
    print(str(ary) + "\n")
    copy = ary[[1, 2, 3]]
    print(str(copy) + "\n")
    copy[:] = 2 # Modifying the copied array does not change the original array
    print(str(copy) + "\n")
    print(str(ary) + "\n")
    ary[1:4] = copy # ASSIGNING part of the original array to be the copied array of course DOES change the original array
    print(str(ary) + "\n")


def index_array_tricky():
    """
    When indices are placed on the left hand side of an assignment statement, neither a view nor a copy is created. The actual data is modified. This
    is because of a Python interpreter optimization. The interpreter asks itself "do I need to create a new object (either a view or a copy in this
    case) to complete this operation? If the answer is no, it won't do it.
    """
    a = np.arange(10)
    a[[1,2]] = 100
    print(a) # [0, 100, 100, 3, 4, 5, 6, 7, 8, 9]
    b = np.arange(10)
    c = b[[1,2]]
    c[:] = 100
    print(b) # [0 1 2 3 4 5 6 7 8 9]
    print(c)


def index_array_tricky_2():
    """
    I think these tricky examples can be summarized as:
    - assignment with an operation that creates a copy actually doesn't create the copy, so the data IS modified (i.e. the copy operation is the
      outermost operation). There is no need to create the copy because no operation works ON the copy itself.
    - assignment with an operation that operates on the COPY itself does create a copy. The second example operates on the copy itself, so the copy is
      created and the original data isn't modified
    """
    # This first example DOES modify the array for the same reasons as index_array_tricky() above 
    a = np.arange(12).reshape(3,4)
    ifancy = [0,2]
    islice = slice(0,3,2)
    a[islice, :][:, ifancy] = 100 # replace 0, 2, 8, and 10 with the value 100
    print(a)
    # This second example does NOT modify the array because I'm slicing a copy?
    a = np.arange(12).reshape(3,4)
    ifancy = [0,2]
    islice = slice(0,3,2)
    a[ifancy, :][:, islice] = 100  # 
    print(a)
    

if __name__ == "__main__":
    #slice_view()
    #index_array_copy()
    #index_array_tricky()
    index_array_tricky_2()