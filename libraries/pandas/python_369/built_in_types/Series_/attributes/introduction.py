# https://medium.com/@ericvanrees/pandas-series-objects-and-numpy-arrays-15dfe05919d7


import numpy as np
import pandas as pd


def get_underlying_pandas_array():
    '''
    <Series>.array returns a PandasArray, not a numpy array
    - A PandasArray is
    '''
    s = pd.Series([2, 5, 7])
    a = s.array
    #print(type(a)) # <class 'pandas.core.arrays.numpy_.PandasArray'>
    #print(a.dtype) # int64
    print(a) # <PandasArray>\n[2, 5, 7]\nLength: 3, dtype: int64


if __name__ == '__main__':
    get_underlying_numpy_array()
