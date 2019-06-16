import pandas as pd


def data_attribute():
    """ The "data" attribute of a Series is depreciated """
    s = pd.Series([1, 54, 34, 5, 26, 2456, 35, 67, 2, 345, 26])
    print(s)
    print(s.data)