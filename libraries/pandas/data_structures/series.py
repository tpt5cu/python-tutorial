"""
https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dsintro
"""


import numpy as np
import pandas as pd


def create_series():
    """
    A Series is a one-dimensional array capable of holding any data type. Each element in the array has an index. The index can be implicitly or
    explicitly set.

    """
    # A Series can be created with many things: a Python dict, list, or other iterable (except a set, which is unordered by definition), an ndarray, a
    # scalar value, etc.
    s = pd.Series([1, 20, 300])
    print(s)
    # If an index is explicitly set, it must be set to some kind of collection. The length of the collection passed as the index must match the length
    # of the input data, except for a few special cases
    s = pd.Series([1, 20, 300], index=["cat", "dog", "frog"])
    print(s)
    # Instantiating with a dictionary will use the dictionary keys as indexes. The order of the Series matches the dict's insertion order
    s = pd.Series({"a": 1, "b": 2, "c": 3})
    print(s)


if __name__ == "__main__":
    create_series()