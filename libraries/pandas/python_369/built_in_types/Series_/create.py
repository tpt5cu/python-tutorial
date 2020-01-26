# https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dsintro


import numpy as np
import pandas as pd


'''
A Series is a 1D heterogenous data structure that can be created from many other sequence types. Series are useful because each item in a series is
associated with a label (i.e. an index)
- A Series is capable of holding any data type
- The index can be implicitly or explicitly set
- A Series can be created from any iterable, including generators!
'''


def list_to_series():
    '''
    Creating a Series will use standard numeric indicies if no other indices are specified
    - A Series can be created with many things: a Python dict, list, or other iterable (except a set, which is unordered by definition), an ndarray, a
      scalar value, etc.
    '''
    s = pd.Series([1, 20, 300])
    print(s)


def specify_indicies():
    '''
    If an index is explicitly set, it must be set to some kind of iterable
    - The length of the iterable passed as the index must match the length of the input data, except for a few special cases
    '''
    s = pd.Series([1, 20, 300], index=["cat", "dog", "frog"])
    print(s, '\n')
    # I can explicitly set the index for a Series like so. pandas supports non-unique indexes. If an operation cannot occur later on, THEN pandas will
    # raise an exception due to the non-unique index
    s = pd.Series([21, 12, 34, 14], index=['a', 'b', 'c', 'a'])
    print(s)
    # If the index is explicitly passed, it must be the same length as the data
    s = pd.Series([1, 2, 3], index=["whoo"]) # ValueError


def dict_to_series():
    '''Instantiating with a dictionary will use the dictionary keys as indexes. The order of the Series matches the dict's insertion order'''
    s = pd.Series({"a": 1, "b": 2, "c": 3})
    print(s)


def generator_to_series():
    g = (x for x in [1, 2, 3])
    g2 = (y for y in ('foo', 'bar', 'baz'))
    print(type(g)) # <class 'generator'>
    s = pd.Series(g, index=g2)
    print(s)


if __name__ == "__main__":
    #list_to_series()
    #specify_indicies()
    #dict_to_series()
    generator_to_series()
