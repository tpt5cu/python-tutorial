# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html


import pandas as pd


"""
I was hoping that append() would just concatenate each Series as a new row in the DataFrame while ignoring all column indexes, but that's just not how
append() works. In order to do what I want, all the Series objects must have the default integer indexes.
- It's more efficient to perform a single append to the DataFrame than multiple appends().
    - Append to a list, then append the single list to the DataFrame
"""


def append_with_index():
    """
    When Series objects are appended to a DataFrame, the indexes of each Series will determine the column where the Series data is inserted. This is
    the default behavior for the method.
    """
    s1 = pd.Series(["A", "bunch", "of", "data"], index=['A', 'B', 'C', 'D'])
    s2 = pd.Series(["Some", "other", "rad", "stuff"], index=['D', 'B', 'A', 'C'])
    s3 = pd.Series(["Whoo", "hoo", "boy", "yea"]) 
    # <DataFrame>.append() does not have an "inplace" option, so it always returns a new DataFrame.
    df = pd.DataFrame()
    l = [s1, s2, s3]
    new_df = df.append(l)
    print(new_df)


# This does not do what I want
def append_without_index():
    """
    If I want to append a Series to a DataFrame, I MUST set (ignore_index=True). (ignore_index=False) only works if I'm appending a Python list,
    another DataFrame, or something else...
    """
    s1 = pd.Series(["A", "bunch", "of", "data"], index=['A', 'B', 'C', 'D'])
    s2 = pd.Series(["Some", "other", "rad", "stuff"], index=['D', 'B', 'A', 'C'])
    s3 = pd.Series(["Whoo", "hoo", "boy", "yea"]) 
    df = pd.DataFrame()
    # This looks exactly the same as append_with_index()
    #l = [s1, s2, s3]
    #new_df = df.append(l, ignore_index=True)
    # This looks exactly the same as append_with_index() too!
    #df_1 = df.append(s1, ignore_index=True)
    #df_2 = df_1.append(s2, ignore_index=True)
    #df_3 = df_2.append(s3, ignore_index=True)
    #print(df_3)
    # This appears to do what I want, but in reality it's still respecting the indexes of each Series. It just so happens that all of these Series
    # have the same default integer indexes
    s1 = pd.Series(["A", "bunch", "of", "data"])
    s2 = pd.Series(["Some", "other", "rad", "stuff"])
    s3 = pd.Series(["Whoo", "hoo", "boy", "yea"]) 
    l = [s1, s2, s3]
    new_df = df.append(l)
    print(new_df)


if __name__ == "__main__":
    #append_with_index()
    append_without_index()