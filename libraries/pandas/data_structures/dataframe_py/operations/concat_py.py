# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html


import pandas as pd
import random


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


def horizontal_concat():
    """
    When column concatenation is performed, the concatenated dataframe keeps all of the original column labels even if there are duplicates. If the
    DataFrames have an uneven amount of rows, the shorter DataFrame will have NaN values append to it.
    """
    df_1 = pd.DataFrame(get_mixed_matrix())
    df_2 = pd.DataFrame(get_mixed_matrix())
    df_2.drop([9], inplace=True)
    print("df_1:")
    print(df_1)
    print("df_2:")
    print(df_2)
    # axis = 1 performs column concatenation (horizontal concatenation)
    concat = pd.concat([df_1, df_2], axis=1)
    print("concat:")
    print(concat.to_string())


if __name__ == "__main__":
    horizontal_concat()