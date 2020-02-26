# https://numpy.org/doc/1.18/reference/arrays.scalars.html#built-in-scalar-types


import numpy as np


def what_is_uint():
    '''
    - "np.uint" and "np.uintc" are aliases for real underlying NumPy scalar types
        - The values of those aliases depend on the operating system
            - On my system, "np.uint" creates an object whose class is "numpy.uint64"
                - "np.uint" has the same precision as ... ?
            - On my system, "np.uintc" creates an object whose class is "numpy.uint32"
                - "np.uintc" has the same precision as ... ?
        - If I want some size other than those specified by the aliases, I'll have to use a class with an explicit size, e.g. np.uint8
    '''
    print(np.uint is np.uint64) # True
    print(np.uintc is np.uint32) # True
    # No error because 1 certainly fits within the size of a C long
    ary = np.array(1, dtype=np.uint)
    print(ary.dtype) # uint64
    #print(int(10**50)) # 100000000000000000000000000000000000000000000000000
    #np.array(10**50, dtype=np.uint) # OverflowError: Python int too large to convert to C long
    print(type(np.uint)) # <class 'type'>
    scalar = np.uint(10)
    print(type(scalar)) # <class 'numpy.uint64'>
    scalar = np.uint32(10)
    print(type(scalar)) # <class 'numpy.uint32'>
    scalar = np.uintc(10)
    print(type(scalar)) # <class 'numpy.uint32'>
    scalar = np.uint8(4)
    print(type(scalar)) # <class 'numpy.uint8'>


if __name__ == '__main__':
    what_is_uint()
