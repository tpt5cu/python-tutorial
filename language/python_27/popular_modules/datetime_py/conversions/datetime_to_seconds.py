# https://stackoverflow.com/questions/7852855/in-python-how-do-you-convert-a-datetime-object-to-seconds
# https://stackoverflow.com/questions/2331592/why-does-datetime-datetime-utcnow-not-contain-timezone-information/2331635#2331635 - create own tzinfo class


from datetime import datetime
from datetime import tzinfo
from datetime import timedelta


def subtract_naive_datetime_objects():
    """
    Subtracting 2 datetime objects results in a timedelta object, which can then be converted to seconds
    - If a datetime is not created with a tzinfo object, then it is a naive datetime, and %Z and %z will be empty strings
    """
    fin = datetime(2019, 7, 17)
    #print(fin.strftime('%Y %m %d %H:%M:%S %z')) # 2019 07 17 00:00:00 
    #print(fin.tzinfo) # None
    start = datetime(1970, 1, 1)
    td = fin - start
    seconds = td.total_seconds()
    # This is the the number of seconds between July 7th 2019 and January 1st 1970. 
    print(seconds) # 1563321600.0


def subtract_aware_datetime_objects():
    """
    The primary usage for subtracting aware datetime objects is to get the time difference between them, including timezone differences
    - An error is raised if naive and aware datetime objects are subtracted
    """
    #fin = datetime(2019, 7, 17, tzinfo=UtcTzinfo())
    #print(fin.strftime('%Y %m %d %H:%M:%S %z')) # 2019 07 17 00:00:00 +0000
    #print(fin.tzinfo) # <__main__.UtcTzinfo object at 0x104eb2490>
    fin = datetime(2019, 7, 17, tzinfo=EdtTzinfo())
    print(fin.strftime('%Y %m %d %H:%M:%S %z')) # 2019 07 17 00:00:00 -0400
    print(fin.tzinfo)
    start = datetime(1970, 1, 1, tzinfo=EdtTzinfo())
    td = fin - start
    seconds = td.total_seconds()
    # This is the the number of seconds between July 7th 2019 and January 1st 1970. The floating point number is the same as above because both
    # datetime happen to be in the same time zone
    print(seconds) # 1563321600.0


def datetime_to_seconds(dt):
    td = dt - datetime(1970, 1, 1)
    return td.total_seconds()


class UtcTzinfo(tzinfo):
    """Represents a tzinfo object for UTC"""

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)


class EdtTzinfo(tzinfo):
    """EDT already includes DST. EDT is 1 hour ahead of EST"""

    def utcoffset(self, dt):
        return timedelta(hours=-4)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)

def _tests():
    '''
    - I want 89 * 24 = 2136 samples
    - End date needs to be October 14th. Why? Because that's an actual 89 days!

    '''
    print(len([0] * 2136)) # 2136
    start_date = datetime(2019, 7, 17)
    #end_date = datetime(2019, 10, 13, 23)
    end_date = datetime(2019, 10, 14)
    sample_number = 2136
    td = timedelta(milliseconds=(end_date - start_date).total_seconds() / float(sample_number) * 1000)
    final_date = start_date + td * 2135
    print(final_date.strftime('%x %X')) # 10/13/19 22:00:01


if __name__ == '__main__':
    #subtract_naive_datetime_objects()
    #subtract_aware_datetime_objects()
    #_tests()
    #07/29/2019 02:00:00
    print(datetime_to_seconds(datetime(2019, 7, 29, 2))) # 1564365600.0