"""
https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
https://stackoverflow.com/questions/35339139/where-is-the-documentation-on-pandas-freq-tags - what is that "Freq" thing?
"""


import pandas as pd
import create


def view_column_labels():
    """ Don't use <DataFrame>.keys(). It doesn't do what I want """
    df = pd.DataFrame(create.get_mixed_matrix())
    print(df)
    print(df.columns.tolist())


def view_row_labels():
    df = pd.DataFrame(create.get_mixed_matrix())
    print(df)
    print(df.index.tolist())
    #print(df.loc)


if __name__ == "__main__":
    #view_column_labels()
    view_row_labels()
