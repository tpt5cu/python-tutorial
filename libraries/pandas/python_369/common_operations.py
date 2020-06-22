import pandas as pd




#skip rows
"""
in read_csv, read_excel and other read functions, feed pandas a skiprows parameter
"""
df = pd.read_csv('xxx', skiprows=y)



#Filter based on column values
"""
When multiple columns are avaliable with the same name, the names change to name, name0.1, name 0.2.
To create a new df out of these column values, """

df = df.filter(like='column_name')

#Extract data based on column value
data = data.loc[data['column_name']] == value




#iloc vs loc
"""
loc gets rows (or columns) with particular labels from the index.
iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.
"""
#first row
df.iloc[0]

#last 5
df.iloc[-5:]

#You can also use it on the columns. This retrieves the 3rd column:
df.iloc[:, 2]    # the : in the first position indicates all rows

#You can combine them to get intersections of rows and columns:
df.iloc[:3, :3] # The upper-left 3 X 3 entries (assuming df has 3+ rows and columns)

#On the other hand, .loc use named indices. Let's set up a data frame with strings as row and column labels:
df = pd.DataFrame(index=['a', 'b', 'c'], columns=['time', 'date', 'name'])
df.loc['a']     # equivalent to df.iloc[0]
#and the second two rows of the 'date' column by
df.loc['b':, 'date']   # equivalent to df.iloc[1:, 1]


