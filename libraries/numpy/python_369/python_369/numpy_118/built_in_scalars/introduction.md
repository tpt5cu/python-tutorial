- https://numpy.org/doc/1.18/reference/arrays.dtypes.html - a scalar is not a dtype object
- https://numpy.org/doc/1.18/reference/arrays.scalars.html#arrays-scalars-built-in - scalar introduction
- https://stackoverflow.com/questions/21968643/what-is-a-scalar-in-numpy - what is a scalar?
# What is a scalar ?
- Informally:
    - A scalar is an item that can be put into an array
    - It's a number. It's called a "scalar" because in this context it's a number that is used to scale a vector
- Formally:
    - A NumPy scalar is any object which is an instance of np.generic or whose type is in np.ScalarType
# What is a scalar type?
- All NumPy scalar types are merely Python types that each represent a scalar NumPy type
    - Literally, each scalar type is a class object
        - E.g. "numpy.int64" is a class object that can be used to create Python objects
## Scalar types are not dtype objects
- Scalar types are *not* dtype objects even though they can be used in place of a dtype object anywhere in the API
    - Strictly speaking, a data type object is an instance of numpy.dtype
- All 24 built-in array scalar type objects (and their sub-classes) all convert to an associated data-type object
# Scalar type hierarchy
- The default data type in NumPy is "numpy.float_"
- NumPy says there are 24 fundamental scalar types:
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
- These types are mostly based on the types available in C
- In reality, the number of actual scalar types available depends on the operating system. Here are is a subset of the scalar types that are available
  on my system:
    - numpy.int8
    - numpy.int16
    - numpy.int32
    - numpy.int64
    - numpy.uint8
    - numpy.uint16
    - numpy.uint32
    - numpy.uint64
    - numpy.float16
    - numpy.float32
    - numpy.float64
    - numpy.float128
    - numpy.complex64
    - numpy.complex128
    - numpy.complex256
## NumPy Python type aliases
- For some reason, NumPy has several objects that are merely aliases to real Python types
    ```
        print(np.int is int) # True
        print(np.bool is bool) # True
        print(np.float is float) # True
        print(np.complex is complex) # True
        print(np.str is str) # True
    ```
    - There is no "np.bytes" type
- These alias objects are confusing and annoying
## Python type conversions within a NumPy dtype context 
- When a dtype object is generated (e.g. when there is a "dtype" parameter in a function signature, or inside of a dtype constructor), several Python
  types are equivalent to a corresponding array scalar type: 
    ```
        ary = np.array(1, int)
        print(ary.dtype) # int64
        print(ary.dtype is np.dtype(np.int_)) # True
    ```
    - int is np.int_
    - float is np.float_
    - bool is np.bool_
    - complex is np.cfloat
    - 
    - Exceptions:
        - bytes is not np.bytes_
        - str is not np.unicode_
    - Anything that is not int, float, bool, complex, str, or bytes is "np.object_" (I think)
# Scalar attributes and methods
- Scalars have the same attributes and methods as ndarrays
    - I'll have to figure out exactly what is meant by this...