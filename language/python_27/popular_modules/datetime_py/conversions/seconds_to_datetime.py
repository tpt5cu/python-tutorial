# https://stackoverflow.com/questions/3694487/in-python-how-do-you-convert-seconds-since-epoch-to-a-datetime-object


import datetime
import tzinfo_py


def get_datetime_from_seconds(posix_timestamp):
    '''
    datetime.fromtimestamp() accepts a POSIX timestamp (i.e. an integer).
    - If no tzinfo object is provided, the returned datetime is naived YET is also will contain information corresponding to the platform's local time
    - If a tzinfo object is provided, the returned datetime is aware and will contain information corresponding to that timezone's local time
    '''
    dt = datetime.datetime.fromtimestamp(posix_timestamp)
    print(dt)


def get_utc_datetime_from_seconds(seconds):
    dt = datetime.datetime.utcfromtimestamp(seconds)
    print(dt)


if __name__ == '__main__':
    # 1970 is 0, so 1971 should be 86400
    get_datetime_from_seconds(0) # 1969-12-31 19:00:00
    get_datetime_from_seconds(0, tzinfo_py.UTC()) # 1969-12-31 19:00:00
    get_datetime_from_seconds(86400)

    #get_utc_datetime_from_seconds(1560686400) # 2019-06-16 12:00:00
    #get_utc_datetime_from_seconds(1564365600) # 2019-07-29 02:00:00