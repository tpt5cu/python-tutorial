"""
https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#arrays-scalars-built-in - image of ALL 24 array scalar type objects
https://docs.scipy.org/doc/numpy/user/basics.types.html - list of built-in NUMERIC numpy types
https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#attributes - list of attributes on dtype objects
https://stackoverflow.com/questions/30086936/what-is-the-difference-between-the-types-type-numpy-string-and-type-str - string_ vs str
https://stackoverflow.com/questions/29877508/what-does-dtype-object-mean-while-creating-a-numpy-array - object type description
"""


import numpy as np


"""
There are 24 array scalar type objects in numpy:
- 5 exact signed numeric types (integers)
    - byte
    - short
    - intc
    - int_
    - longlong
- 5 exact unsigned numeric types
    - ubyte
    - ushort
    - uintc
    - uint_
    - ulonglong
- 4 inexact floating numeric types
    - half
    - single
    - float_
    - longfloat
- 3 inexact complexfloating numeric types
    - csingle
    - complex_
    - clongfloat
- 2 flexible character types
    - str_
    - unicode_
- 1 flexible type
    - void
- 2 generic types
    - bool_
    - object_
- 2 integer types which are just pointers to other types that hold a pointer for the platform
    - intp
    - uintp
    - object_

The basic numeric types are all platform-dependent in size. To mitigate this, numpy provides a set of aliases that refer to types of fixed size. These
aliases do NOT map exactly to any of the 24 types above. For example, "intc" matches the "int" C type while "int64" matches the "int64_t" C type
- int8
- int16
- int32
- int64
- uint8
- uint16
- uint32
- uint64
- intp
- uintp
- float32
- float64 (i.e. float_)
- complex64
- complex128 (i.e. complex_)
"""


def get_type():
    """
    My understanding is that a dtype object is really a complex object, and not a type in and of itself. Each dtype object has an underlying built-in
    numpy type. This underlying built-in type can be examined with the "type" attribute on a dtype object.
    """
    strings = np.array(["here", "are", "some", "strings"])
    numbers = np.array([1, 2, 3])
    floats = np.array([1.0, 2.45, 4.3456])
    print(strings.dtype.type) # numpy.string_
    print(numbers.dtype.type) # numpy.int64
    print(floats.dtype.type) # numpy.float64


def examine_string_type():
    """
    There are only 2 string types in numpy: a "string_" type and a "unicode_" type. The 'str' type is a native Python type and cannot be used in numpy arrays
    - string_:
        - There are aliases for the string_ type, including str_ and string0. I don't know why these aliases exist, maybe backwards compatability?
        - The numpy.string_ type is used for arrays that contain fixed-width byte strings
    - unicode_:
        - This type is used for string arrays in Python 3

    The bytes_ type maps directly to the string_ type.
    """
    print(np.string_) # numpy.string_
    print(np.str) # str (plain Python str)
    print(np.str_) # numpy.string_
    print(np.string0) # numpy.string_
    print(np.string_ is np.string0) # True
    print(np.string_ is np.str_) # True
    print(np.string_ is np.str) # False


def examine_object_type():
    """
    Normally, a numpy array is stored as a contiguous block of memory, with each item in the array having a fixed byte size. This is very efficient.
    However, sometimes numpy doesn't have a choice but to create an array with the "object_" type. If an array has this type, then it really is
    storing pointers to real Python objects that are NOT contiguous in memory.
    - When an object_ type array element is referenced, the actual Python object is returned
    """
    pass


if __name__ == "__main__":
    #get_type()
    examine_string_types()
    