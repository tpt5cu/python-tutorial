"""
https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#indexing-selection
https://stackoverflow.com/questions/10665889/how-to-take-column-slices-of-dataframe-in-pandas
"""


import pandas as pd
import create


def get_mixed_matrix():
    return pd.DataFrame(create.get_mixed_matrix(), columns=["cat", "dog", "frog", "log", "zog", "butt", "goof", "night", "as", "we"])


def access_rows():
    """
    Each DataFrame has two special dictionary-like attributes: loc and iloc
    - loc stands for location. Use it to return a row/column based on label
    - iloc stands for integer location. Use it to return a row/column based on its index relative to other rows/columns in the DataFrame. Indexes start at 0.
    """
    df = pd.DataFrame(create.get_mixed_matrix(), index=["cat", "dog", "frog", "log", "zog", "butt", "goof", "night", "as", "we"])
    print(str(df) + "\n")
    # get the row at integer index 0. Rows can be printed veritcally, but they are still horizontal rows in the DataFrame.
    print(str(df.iloc[0]) + "\n")
    # get the row labeld "butt"
    print(str(df.loc["butt"]) + "\n")
    # get rows at indexes 0 and 5. Interestingly, now the rows are printed horizontally. Printing components of a DataFrame is tricky!
    print(str(df.iloc[[0, 5]]) + "\n")
    # get rows with labels "zog" and "night"
    print(str(df.loc[["zog", "night"]]) + "\n")
    # rows can be accessed directly on the DataFrame object with slicing notation. As with the normal slice operator, the lower bound is inclusive and
    # the upper bound is exclusive.
    print(str(df[3:6]) + "\n")


def access_columns():
    """ Access columns directly on the DatFrame object with brackets. """
    df = pd.DataFrame(create.get_mixed_matrix())
    print(df)
    # Use brackets to access a COLUMN by label of a dataframe. Brackets (aka square brackets) refers to "[]". Braces (aka curly brackets) refers to "{}".
    # This particular DataFrame happens to have integer columns labels.
    print(df[0]) 
    # There are 10 rows at the column labled 0 in the DataFrame
    print(len(df[0])) 
    # This throws an error because there is no column with the label "cat"
    #print(df["cat"])


def slice_columns_by_label():
    """ The loc dictionary object stores everything by label. Everything must be accessed by lable, NOT index! """
    df = get_mixed_matrix()
    print(str(df) + "\n")
    # Get all the rows of the "frog" column
    print(str(df.loc[:, "frog"]) + "\n")
    # Get all of the rows of the "frog" through "zog" columns
    print(str(df.loc[:, "frog":"zog"]))


def slice_columns_by_index():
    """ The iloc dictionary object stores evrything by index """
    df = get_mixed_matrix()
    print(str(df) + "\n")
    # Get all the rows of the 1st column
    print(str(df.iloc[:,0]) + "\n")
    # Get all of the rows of the 1st through 3rd columns
    print(str(df.iloc[:,0:3]))


def access_column_and_row():
    """ The syntax for accessing a particular row of a column is actually intuitive """
    df = pd.DataFrame(create.get_mixed_matrix())
    print(df)
    print(df[0][1])


if __name__ == "__main__":
    #access_rows()
    #access_columns()
    #slice_columns_by_label()
    slice_columns_by_index()
    #access_column_and_row()