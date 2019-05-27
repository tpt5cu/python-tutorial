"""
https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#indexing-selection
"""


import pandas as pd
import create


def access_rows():
    """
    Each DataFrame has two special dictionary-like attributes: loc and iloc
        - loc stands for location. Use it to return a row based on the row's label
        - iloc stands for integer location. Use it to return a row based on its index relative to other rows in the DataFrame. Rows are indexed from 0.
    These objects are used to return 1 or more rows from a DataFrame.
    Rows can also be accessed with a slice operator directly on the DataFrame object
    """
    df = pd.DataFrame(create.get_mixed_matrix(), index=["cat", "dog", "frog", "log", "zog", "butt", "goof", "night", "as", "we"])
    print(df)
    # get the row at index 0. Rows can be printed veritcally, but they are still horizontal rows in the DataFrame.
    print(df.iloc[0]) 
    # get the row labeld "butt"
    print(df.loc["butt"]) 
    # get rows at indexes 0 and 5. Interestingly, now the rows are printed horizontally. Printing components of a DataFrame is tricky!
    print(df.iloc[[0, 5]]) 
    # get rows with labels "zog" and "night"
    print(df.loc[["zog", "night"]])
    # rows can be accessed directly on the DataFrame object with slicing notation. As with the normal slice operator, the lower bound is inclusive and
    # the upper bound is exclusive.
    print(df[3:6])


def access_columns():
    """
    Access columns directly on the DatFrame object with brackets.
    """
    df = pd.DataFrame(create.get_mixed_matrix())
    print(df)
    # Use brackets to access a COLUMN by label of a dataframe. Brackets (aka square brackets) refers to "[]". Braces (aka curly brackets) refers to "{}".
    # This particular DataFrame happens to have integer columns labels.
    print(df[0]) 
    # There are 10 rows at the column labled 0 in the DataFrame
    print(len(df[0])) 
    # This throws an error because there is no column with the label "cat"
    #print(df["cat"])


def access_column_and_row():
    """ The syntax for accessing a particular row of a column is actually intuitive """
    df = pd.DataFrame(create.get_mixed_matrix())
    print(df)
    print(df[0][1])


if __name__ == "__main__":
    #access_rows()
    #access_columns()
    access_column_and_row()