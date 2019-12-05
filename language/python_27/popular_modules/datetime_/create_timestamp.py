# https://en.wikipedia.org/wiki/ISO_8601#General_principles
# http://jkorpela.fi/iso8601.html


import datetime as dt
from datetime import tzinfo, timedelta
from popular_modules.datetime_ import tzinfo_


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
    - <datetime>.isoformat() will only append a timezone in the (+|-)dd:dd format. It won't append a "Z"
    '''
    d_time = dt.datetime.utcnow()
    print(d_time.tzinfo) # None
    ts = d_time.strftime('%c')
    print(ts) # Mon Nov 25 21:18:48 2019
    ts = d_time.isoformat()
    print(ts) # 2019-11-25T21:18:48.311245
    d_time = dt.datetime.now(tz=tzinfo_.UTC())
    print(d_time.isoformat()) # 2019-11-25T22:45:16.164069+00:00


def get_pretty_isoformat_timestamp():
    '''Using rsplit() to get rid of microseconds works regardless of the value of the microseconds'''
    ts = dt.datetime.utcnow().isoformat().rsplit('.')[0] + 'Z'
    print(ts)
    ts = dt.datetime(2019, 11, 27).isoformat().rsplit('.')[0] + 'Z'
    print(ts)


def prove_that_datetimes_are_naive():
    '''
    "Subtraction of a datetime from a datetime is defined only if both operands are naive, or if both are aware. If one is aware and the other is
    naive, TypeError is raised."
    '''
    td = dt.datetime.now() - dt.datetime.utcnow()
    print(td.total_seconds() / 60 / 60) # -5.00000000111


if __name__ == '__main__':
    #view_current_local_timestamp()
    #view_current_utc_timestamp()
    get_pretty_isoformat_timestamp()
    #prove_that_datetimes_are_naive()