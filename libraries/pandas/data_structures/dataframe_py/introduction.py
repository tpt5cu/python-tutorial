# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html - quickstart
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html - delete
# http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html - rename
# https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas - rename


import random
import pandas as pd


"""Many pandas operations have an "inplace" parameter that specifies whether to modify this DataFrame or return a new one."""


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


def delete_rows_and_columns():
    """
    <DataFrame>.drop() will delete either rows or columns according to their index or label respectively. The operation is not done in place unless
    specified. There does not appear to be slicing notation available.
    """
    df = pd.DataFrame(get_mixed_matrix())
    print("df:")
    print(df.to_string())
    df.drop([8, 9], inplace=True)
    print("df minus rows:")
    print(df.to_string())
    # Specify axis=1 to delete based on column labels
    df.drop([2, 3], axis=1, inplace=True)
    print("df minus columns:")
    print(df)


def rename_columns_and_indexes():
    df = pd.DataFrame(get_mixed_matrix())
    print("df:")
    print(df.to_string())
    #Rename specific rows or columns with <DataFrame>.rename()
    df.rename(columns={0: "aa", 3: "cc", 5: "ee", 9: "zz"}, inplace=True)
    df.rename(index={0: "blah", 1: "gruf", 9: "zooozoo"}, inplace=True)
    print("renamed df:")
    print(df.to_string())
    #Do wholesale modification
    df.columns = ["a" for x in df.columns.tolist()]
    df.index = ["z" for x in df.index.tolist()]
    print("renamed df:")
    print(df.to_string())


if __name__ == "__main__":
    delete_rows_and_columns()
    #rename_columns_and_indexes()