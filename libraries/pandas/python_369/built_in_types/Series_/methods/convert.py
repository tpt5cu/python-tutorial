import numpy as np
import pandas as pd


'''I think best practice is to specify the dtype of the numpy array that I want'''


def series_to_inferred_numpy_array():
    '''<Series>.to_numpy() will infer the dtype of the ndarray if one is not specified'''
    s = pd.Series([1, 3, 5, 7])
    a = s.to_numpy()
    print(type(a)) # <class 'numpy.ndarray'>
    print(a.dtype) # int64
    # The correct dtype has been inferred
    print(type(a[0])) # <class 'numpy.int64>


def series_to_object_numpy_array():
    '''<Series>.to_numpy() will return an ndarray of the "object" type if a more suitable type cannot be inferred'''
    s = pd.Series([1, 3, '5', 7])
    a = s.to_numpy()
    print(type(a)) # <class 'numpy.ndarray'>
    print(a.dtype) # object
    print(type(a[0])) # <class 'int'>
    print(type(a[2])) # <class 'str'>


def series_to_specified_numpy_array():
    '''
    <Series>.to_numpy() can have an explicit dtype specified for the ndarray
    - If each element can be coerced to the specified dtype, then great
    - If not, a ValueError will be raised
    '''
    s = pd.Series([1, 3, '5', 7], dtype=np.int)
    a = s.to_numpy()
    print(type(a)) # <class 'numpy.ndarray'>
    print(a.dtype) # int64
    print(type(a[0])) # <class 'numpy.int64'>
    print(type(a[2])) # <class 'numpy.int64'>
    print(a) # [1 3 5 7]
    s = pd.Series([1, 3, 'foo', 7], dtype=np.int) # ValueError: invalid literal for int() with base 10: 'foo'


if __name__ == '__main__':
    #series_to_inferred_numpy_array()
    #series_to_object_numpy_array()
    series_to_specified_numpy_array()
