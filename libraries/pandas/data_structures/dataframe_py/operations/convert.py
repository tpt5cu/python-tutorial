# https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array

# Import the operations module (and thus run everything in __init__.py)
from .. import operations
import numpy as nd
import pandas as pd


def dataframe_to_ndarray():
    """
    Use pandas <DataFrame or Series or Index>.to_numpy() to get an ndarray from a Pandas object if I don't need to preserve the dtypes. Do not use
    <pandas object>.values
    - <Object>.to_numpy() is available in Python 2 and Python 3
    """
    df = pd.DataFrame(operations.get_mixed_matrix())
    print(type(df)) # <class 'pandas.core.frame.DataFrame'>
    print(df)
    ary = df.to_numpy()
    print(type(ary)) # <class 'numpy.ndarray'>
    print(ary)
    print(ary.shape) # (10, 10)


if __name__ == "__main__":
    dataframe_to_ndarray()