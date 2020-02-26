# https://numpy.org/doc/1.18/reference/arrays.dtypes.html#attributes


import numpy as np


def view_underlying_scalar_type():
    '''
    - Literally, <dtype>.type is "The type object used to instantiate a scalar of this data type."
        - If the dtype an underlying scalar type, then the underlying scalar type would be returned
        - If the dtype doesn't have an underlying scalar type (e.g. it's some weird composite type), then numpy.void would be returned since there is
          no underlying numpy scalar type that could be used to instantiate a scalar of this data type
    '''
    my_dtype = np.dtype(np.int64)
    print(type(my_dtype.type)) #<class 'type'> 
    print(my_dtype.type) # <class 'numpy.int64'>
    my_dtype = np.dtype([('foo', 'i8'), ('bar', 'M')])
    print(type(my_dtype.type)) # <class 'type'>
    print(my_dtype.type) # <class 'numpy.void'>


def view_other_attributes():
    '''I don't find the other attributes of dtype objects to be particularly useful right now'''
    my_dtype = np.array(1, str).dtype
    # __str__() representation, aka the array-protocol typestring
    print(my_dtype) # <U21
    # Character code identifying the general data type
    print(my_dtype.kind) # U
    # Unique character code for each of the 21 built-in types (yes 21, not 24?)
    print(my_dtype.char) # U
    # Unique number for each of the 21 built-in types
    print(my_dtype.num) # 19
    # Bit-width name
    print(my_dtype.name) # str672
    # Element size of the data-type object
    print(my_dtype.itemsize) # 84


if __name__ == '__main__':
    #view_underlying_scalar_type()
    view_other_attributes()
