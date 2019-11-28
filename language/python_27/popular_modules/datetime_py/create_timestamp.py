# https://en.wikipedia.org/wiki/ISO_8601#General_principles
# http://jkorpela.fi/iso8601.html


import datetime as dt
from datetime import tzinfo, timedelta
from tzinfo_py import MostBasicUTC


'''
- ISO 8601 is the standard for timestamp formatting. There are two formats: basic and extended
    - Basic format: YYYYMMDDThhmmss
        - The basic format should be avoided in plain text
    - Extended format: YYYY-MM-DDThh:mm:ss
        - The extended date format uses hyphens as separators
        - The extended time format uses colons as separators
    - For either format, the "T" separator between date and time is optional
- The highest resolution time unit in a timestamp may have an arbitrary decimal precision
    - The separator for the decimal numbers may be a comma or period
    - E.g. YYYY-MM-DDThh:mm:ss.ssssss
    - There is no limit on the number of allowed decimal places

- <datetime>.isoformat() will only append a timezone in the (+|-)dd:dd format. It won't append a "Z"
'''


def view_current_local_timestamp():
    '''
    - Recently, Eastern Daylight Time (EDT) ended, which is 4 hours behind UTC
        - Daylight savings time ran from March 10th 2019 to November 3rd 2019
    - It is currently Eastern Standard Time (EST) which is 5 hours behind UTC
        - This makes sense, because when EST starts, we "fall back" an hour
    - Even though the local datetime is accurate, this is still technically a naive datetime object
    '''
    d_time = dt.datetime.now()
    print(d_time.tzinfo) # None
    ts = d_time.strftime('%c') 
    print(ts) # Mon Nov 25 16:18:48 2019
    ts = d_time.isoformat()
    print(ts) # 2019-11-25T16:18:48.309482


def view_current_utc_timestamp():
    '''
    - utcnow() returns a naive datetime object
        - A datetime object is naive if <datetime>.tzinfo is None or <datetime>.tzinfo.utcoffset() is None
    - In order to get a timestamp that is aware that it is in UTC, I should use datetime.now(<tz>)
    '''
    d_time = dt.datetime.utcnow()
    print(d_time.tzinfo) # None
    ts = d_time.strftime('%c')
    print(ts) # Mon Nov 25 21:18:48 2019
    ts = d_time.isoformat()
    print(ts) # 2019-11-25T21:18:48.311245
    d_time = dt.datetime.now(tz=MostBasicUTC())
    print(d_time.isoformat()) # 2019-11-25T22:45:16.164069+00:00



def prove_that_datetimes_are_naive():
    '''
    "Subtraction of a datetime from a datetime is defined only if both operands are naive, or if both are aware. If one is aware and the other is
    naive, TypeError is raised."
    '''
    td = dt.datetime.now() - dt.datetime.utcnow()
    print(td.total_seconds() / 60 / 60) # -5.00000000111


if __name__ == '__main__':
    #view_current_local_timestamp()
    view_current_utc_timestamp()
    #prove_that_datetimes_are_naive()