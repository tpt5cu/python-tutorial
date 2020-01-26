import pandas as pd


'''
I don't know when I would prefer a PandasArray to an actual numpy ndarray. Actually, it is useful in these cases:
- numpy cannot represent time zone aware datetimes, while Pandas can
'''


def list_to_pandas_array():
    a = pd.array((1, 2, 3)) 
    print(type(a)) # <class 'pandas.core.arrays.numpy_.PandasArray'>
    print(a) # <PandasArray>\n[1, 2, 3]\nLength: 3, dtype: int64 


def create_timestamp_array():
    '''
    The Pandas Timestamp is mostly interchangable with Python's datetime.datetime
    - Timestamp is a subclass of datetime.datetime
    '''

    t1 = pd.Timestamp(2019, 1, 20, 12, 30, 5)
    print(type(t1)) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    print(t1) # 2019-01-20 12:30:05
    t2 = pd.Timestamp(2018, 5, 5, 5, 5, 5)
    print(t2) # 2018-05-05 05:05:05
    a = pd.array((t1, t2))
    print(a) # <DatetimeArray>\n['2019-01-20 12:30:05', '2018-05-05 05:05:05']\nLength: 2, dtype: datetime64[ns]


if __name__ == '__main__':
    #list_to_pandas_array()
    create_timestamp_array()
