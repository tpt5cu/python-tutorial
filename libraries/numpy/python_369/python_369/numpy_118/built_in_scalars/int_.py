# https://stackoverflow.com/questions/21851985/difference-between-np-int-np-int-int-and-np-int-t-in-cython - what is int
# https://numpy.org/doc/1.18/reference/arrays.scalars.html#built-in-scalar-types


import numpy as np


def what_is_int():
    '''
    - Python's "int" type is of arbitrary precision
        - However, when "int" is used as an arg/kwarg for the "dtype" parameter, it is equivalent to "np.int_". Confusing!
    - "np.int_" and "np.intc" are aliases for real underlying NumPy scalar types
        - The values of those aliases depend on the operating system
            - On my system, "np.int_" creates an object whose class is "numpy.int64"
                - "np.int_" has the same precision as a C long
            - On my system, "np.intc" creates an object whose class is "numpy.int32"
                - "np.intc" has the same precision as a C int
        - If I want some size other than those specified by the aliases, I'll have to use a class with an explicit size, e.g. np.int32
    '''
    print(np.int_ is np.int64) # True
    print(np.intc is np.int32) # True
    # No error because 1 certainly fits within the size of a C long
    ary = np.array(1, dtype=int)
    print(type(ary.dtype))
    print(ary.dtype) # int64
    #print(int(10**50)) # 100000000000000000000000000000000000000000000000000
    #np.array(10**50, dtype=int) # OverflowError: Python int too large to convert to C long
    print(type(np.int_)) # <class 'type'>
    scalar = np.int_(10)
    print(type(scalar)) # <class 'numpy.int64'>
    scalar = np.int32(10)
    print(type(scalar)) # <class 'numpy.int32'>
    scalar = np.intc(10)
    print(type(scalar)) # <class 'numpy.int32'>


def test():
    ary = np.array(1, dtype=list)
    print(ary.dtype)
    print(ary.dtype is np.dtype(np.object_))


if __name__ == '__main__':
    #what_is_int()
    test()
