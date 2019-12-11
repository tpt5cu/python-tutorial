# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#missing-data-handling
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate


import pandas as pd
from python_27.dataframe_.create import get_numeric_matrix


def linear_interpolation():
    m = get_numeric_matrix()
    df = pd.DataFrame(m)
    print(df)
    print('')
    m = [([0] * len(t[1]) if (t[0] > 0 and t[0] < len(m) - 1) else t[1]) for t in enumerate(m)]
    df = pd.DataFrame(m)
    print(df)


if __name__ == '__main__':
    linear_interpolation()