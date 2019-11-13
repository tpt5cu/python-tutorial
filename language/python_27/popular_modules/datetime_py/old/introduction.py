# https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64
# https://docs.python.org/2/library/datetime.html
# https://stackoverflow.com/questions/656297/python-time-timedelta-equivalent - time + timedelta?


import datetime


"""
If I ever see a datetime object like '2017-06-01 00:00:00-05:00', then:
- '2017-06-01' is year-month-day
- '00:00:00' is hrs-mins-secs
- '-05:00' is 5 hours subtracted from UTC, which represents EST (Eastern Standard Time), which starts in November and ends in March
    - '-04:00' is 4 hours subtracted from UTC, which represents EDT (Eastern Daylight Time), which starts in March and ends in November
- If I see "Z" at the end of a datetime format, that stands for the UTC timezone 1994-11-05T13:15:30Z

There are "naive" and "aware" objects for working with dates and times. A naive object cannot locate itself relative to other date/time objects. An
aware object can locate itself relative to other date/time objects.
- "time" and "datetime" objects are naive by default, and must be supplied a "tzinfo" instance in order to be aware. 
- The "tzinfo" class is abstract. Therefore, to pass a tzinfo object I must implement a concrete subclass of tzinfo and use it.
"""


def create_naive_datetime():
    """
    The constructor isn't capitalized for some reason. All instance attributes are ints, except for tzinfo. year, month and day are required.
    """
    # datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
    dt = datetime.datetime(2017, 1, 1, 0, 0, 0)
    print("year: " + str(dt.year))
    print("second: " + str(dt.second))


def create_timedelta():
    """
    All arguments are optional and default to 0. Make sure to use kwargs! A timedelta object only stores days, seconds, and microseconds, and hence
    only has those attributes. micro means 10^-6, not 10^-2 (that's centi)
    """
    # timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
    td = datetime.timedelta(microseconds=-1)
    # Why is this (-1, 86399, 999999)?
    # Because -1 days + (86,400 - 1) seconds = -1 second, and -1,000,000 microseconds + 999,999 microseconds = -1 microsecond
    print(td.days, td.seconds, td.microseconds) # (-1, 86399, 999999)


def add_timedelta_to_datetime():
    """datetime + timedelta = datetime"""
    dt = datetime.datetime(2000, 5, 5, 23, 59, 59)
    td = datetime.timedelta(seconds=1)
    new_dt = dt + td
    print(new_dt) # 2000-05-06 00:00:00
    td = datetime.timedelta(microseconds=1000001)
    new_dt = dt + td
    # The result is correct, but is it a real datetime? Yes!
    print(new_dt) # 2000-05-06 00:00:00.000001


def create_time():
    # time(hour, minute, second, microsecond, tzinfo)
    t = datetime.time(23, 59, 59)
    print(t)


def datetime_to_time():
    dt = datetime.datetime(2019, 6, 13, 2, 30, 2)
    t = dt.time()
    print(t)


def add_timedelta_to_time():
    """
    I cannot directly do operations with time objects and timedelta objects, so I have to convert the time into a datetime object!
    datetime.combine(<date>, <time>)
    """
    dt = datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30, 5)) + datetime.timedelta(hours=1)
    t = dt.time()
    print(t) # 13:30:05


if __name__ == "__main__":
    #create_naive_datetime()
    #create_timedelta()
    #add_timedelta_to_datetime()
    #create_time()
    #datetime_to_time()
    add_timedelta_to_time()