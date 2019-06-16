"""
https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#conversion
https://docs.scipy.org/doc/numpy/user/basics.types.html - basic numpy dtypes
https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-dtypes - show the extensions that pandas makes to numpy dtypes
"""

import random
import numpy as np
import pandas as pd


"""
A dataframe is basically a 2D matrix, except that the rows and columns are labeled. The basic constructor takes 5 optional arguments:
    - data: the data
    - index: labels to use for rows
    - columns: labels to use for columns
    - dtype: the data type will be inferred if this argument is not passed.
    - copy: whether or not to copy the data from the data input. 
"""


def get_mixed_matrix():
    """ Return a 10 x 10 2d matrix that is a list of lists """
    words = ["Returns", "a", "new", "list", "containing", "elements", "from", "the", "population", "while", "leaving", "the", "original", "population", "unchanged.", "The", "resulting", "list", "is", "in", "selection", "order", "so", "that", "all", "sub-slices", "will", "also", "be", "valid", "random", "samples.", "This", "allows", "raffle", "winners", "(the", "sample)", "to", "be", "partitioned", "into", "grand", "prize", "and", "second", "place", "winners", "(the", "subslices)."]
    matrix = []
    for x in range(10):
        my_list = []
        if x % 2 == 0:
            for y in range(10):
                my_list.append(random.randint(0, 100))
        else:
            for y in range(10):
                my_list.append(random.choice(words))
        matrix.append(my_list)
    return matrix


def get_numeric_matrix():
    """ Return a 10 x 10 2d matrix that is a list of lists """
    matrix = []
    for x in range(10):
        my_list = []
        for y in range(10):
            my_list.append(random.randint(0, 100))
        matrix.append(my_list)
    return matrix


def empty_dataframe():
    """ I can create an empty DataFrame just fine. pandas will even tell me that it's empty when I print it """
    df = pd.DataFrame()
    print(df)


def unlabeled_dataframe():
    """
    If a dataframe is created with a list of lists and no explicit label argument, the DataFrame still will have explicit row labels and column
    labels. The labels appear to just be autogenerated integer values. The row labels and column labels are displayed when printing, but are not
    counted in the length of the data, nor as part of the data at all.
    """
    df = pd.DataFrame(get_mixed_matrix())
    print(df)


def labeled_dataframe():
    """
    Since the DataFrame constructor takes 5 arguments, I should always label my arguments so its clear if the passed labels should apply to the rows
    or columns
    """
    # "index" applies to rows, "columns" applies to columns
    df = pd.DataFrame(get_mixed_matrix(), index=["cat", "dog", "frog", "log", "zog", "butt", "goof", "night", "as", "we"])
    print(df)


def uneven_dataframe():
    pass


def no_coerce_type():
    """
    pandas will ATTEMPT to enforce a type constraint on all columns when the dtype argument is passed. If pandas can't coerce a value in a specific column (e.g. coerce a
    string to a numpy int64), the constraint doesn't affect that column.
    """
    # The constraint does nothing to all columns, because all columns have string values
    df = pd.DataFrame(get_mixed_matrix(), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], dtype=np.int64) 
    print(df)
    print("\n")
    # The dtypes attribute returns a Series with the data type of each COLUMN. If a COLUMN has mixed types, then the column has a dtype of "object".
    # Columns that store strings also have the "object" dtype
    print(df.dtypes)
    # Shows that there are 10 columns that have the dtype "object"
    print(df.get_dtype_counts()) 


def coerce_type():
    """
    In this example, the np.int8 has a range of [-127, 128], so the bytes of the integer 3000 get interpreted as -72 because that entire column can be
    coerced into an np.in8 type. 4000 is not coerced because the string "cat" prevents the column from being coerced.
    """
    df = pd.DataFrame([[1, 2], [4000, 4], [5, 6], [7, 8], [9, 3000], ["cat", 4]], columns=["bat", "squat"], dtype=np.int8)
    print(df)
    print("\n")
    print(df.dtypes)


def from_ndarray():
    pass


if __name__ == "__main__":
    #empty_dataframe()
    #unlabeled_dataframe()
    #labeled_dataframe()
    #uneven_dataframe()
    #no_coerce_type()
    coerce_type()