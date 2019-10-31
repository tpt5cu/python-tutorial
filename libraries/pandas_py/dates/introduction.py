# https://stackoverflow.com/questions/22825349/converting-between-datetime-and-pandas-timestamp-objects
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html


import pandas as pd


def pandas_to_python():
    ts = pd.Timestamp('2014-01-23 00:00:00', tz=None)
    print(ts) # 2014-01-23 00:00:00
    print(type(ts)) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    dt = ts.to_pydatetime()
    print(dt) # 2014-01-23 00:00:00
    print(type(dt)) # <class 'datetime.datetime'>


if __name__ == "__main__":
    pandas_to_python()