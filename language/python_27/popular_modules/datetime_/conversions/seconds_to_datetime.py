# https://stackoverflow.com/questions/3694487/in-python-how-do-you-convert-seconds-since-epoch-to-a-datetime-object


import datetime, os
from popular_modules.datetime_ import tzinfo_


def get_datetime_from_seconds(posix_timestamp, tz=None):
    '''
    datetime.fromtimestamp() accepts a POSIX timestamp (i.e. an integer).
    - If a tzinfo object is not provided, the returned datetime is naive, YET it will contain information corresponding to the platform's local time
    - If a tzinfo object is provided, the returned datetime is aware and will contain information corresponding to that timezone's local time
    '''
    dt = datetime.datetime.fromtimestamp(posix_timestamp, tz)
    print(dt)


def get_utc_datetime_from_seconds(seconds):
    dt = datetime.datetime.utcfromtimestamp(seconds)
    print(dt)


if __name__ == '__main__':
    #get_datetime_from_seconds(0) # 1969-12-31 19:00:00
    #get_datetime_from_seconds(0, tzinfo_.ET()) # 1969-12-31 19:00:00-05:00
    #get_datetime_from_seconds(0, tzinfo_.UTC()) # 1970-01-01 00:00:00+00:00
    #get_datetime_from_seconds(86400, tzinfo_.UTC()) # 1970-01-02 00:00:00+00:00
    #get_utc_datetime_from_seconds(86400) # 1970-01-02 00:00:00
    #get_datetime_from_seconds(os.path.getmtime('/Users/austinchang/Desktop/testfiles')) # 2019-07-14 16:18:14.867562
    get_utc_datetime_from_seconds(os.path.getmtime('/Users/austinchang/Desktop/testfiles')) # 2019-07-14 20:18:14.867562
