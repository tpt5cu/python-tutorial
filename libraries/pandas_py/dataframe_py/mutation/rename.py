# http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html - rename
# https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas - rename


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