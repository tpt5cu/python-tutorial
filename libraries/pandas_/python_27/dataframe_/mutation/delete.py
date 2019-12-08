# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html - quickstart
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html - delete


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