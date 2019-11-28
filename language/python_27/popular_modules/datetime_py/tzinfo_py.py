# https://docs.python.org/2/library/datetime.html#tzinfo-objects
# https://julien.danjou.info/python-and-timezones/
# https://codeofmatt.com/please-dont-call-it-epoch-time/
# https://stackoverflow.com/questions/16539436/unix-time-and-leap-seconds - Unix timestamps and leap seconds


import datetime


'''
The article suggests that I should never use naive timezone objects in Python and that I should treat them as a bug. After reading the article and
watching the video, I'm inclined to agree.
'''


class UTC(datetime.tzinfo):
    '''This is the most basic possible implementation of a UTC tzinfo class'''
    ZERO = datetime.timedelta(0)
    
    def utcoffset(self, dt):
        return self.__class__.ZERO

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return self.__class__.ZERO


class ET(datetime.tzinfo):
    '''
    This class should be called ET, not EST or EDT. Why? Because I want this timezone object to be DST aware.
    - If I named this class EST, then by defintion it should never include with DST
        - EST is five hours behind UTC
    - If I named this class EDT, then by definition it must include with DST
        - EDT is four hours behind UTC
    - There are other ways to implement a tzinfo object. See the docs.
    '''
    offset = datetime.timedelta(hours=-5)
    # These DST transition times are only valid for Virginia, USA on these years. The only way to get this information is to look it up. Any
    # country can transitions on and off DST whenever it wants. I now see why Python never tried to provide a concrete implementation. Arizona
    # ignores DST completely!
    dst_switch = {
        2018: { 'on': datetime.datetime(2018, 3, 11, 2), 'off': datetime.datetime(2018, 11, 4, 2) },
        2019: { 'on': datetime.datetime(2019, 3, 10, 2), 'off': datetime.datetime(2019, 11, 3, 2) },
        2020: { 'on': datetime.datetime(2020, 3, 8, 2), 'off': datetime.datetime(2020, 11, 1, 2) },
        2021: { 'on': datetime.datetime(2021, 3, 14, 2), 'off': datetime.datetime(2021, 11, 7, 2) },
        2022: { 'on': datetime.datetime(2022, 3, 13, 2), 'off': datetime.datetime(2022, 11, 6, 2) }
    }

    def __init__(self):
        '''Unfortunately, a tzinfo object is created independently of any datetime object, so "dt" can't be accessed here'''
        pass

    def utcoffset(self, dt):
        '''
        Returns the total offset from UTC.
        - If this tzinfo object is DST aware, then this method should invoke self.dst().
        - If this tzinfo object is not DST aware, then it should just return a constant.
        - The total offset can be five hours or four hours, depending on whether or not DST is active
         '''
         # self.dst(dt) will be 0 or 1 depending on whether or not DST is active
        return self.__class__.offset + self.dst(dt)

    def tzname(self, dt):
        td = self.dst(dt)
        if td.seconds == 3600:
            return 'EDT'
        else:
            return 'EST'

    def dst(self, dt):
        '''Return the DST adjustment from UTC'''
        year = self.__class__.dst_switch[dt.year]
        dston = year['on']
        dstoff = year['off']
        # I am comparing naive datetime objects. It actually makes sense to do this because I know that what the naive datetimes represent. This
        # implementation does not work datetimes that are ambiguous (i.e. they could be in EDT or EST)
        if dston <= dt.replace(tzinfo=None) < dstoff:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(0)


def perform_utc_conversion():
    '''The timetuple(), utctimetuple(), and utcoffset() instance methods show that the tzinfo class is implemented correctly'''
    # Technically, this could be a DST active time. It could be the 1:59:59 after the initial switch from 2:00 AM back to 1:00 AM. This is ambiguous,
    # so I shouldn't use this time, e.g.:
    # - 1:59:59 AM EST is a real time
    # - 1:59:59 AM EDT is a real time
    #dst_inactive_dt = datetime.datetime(2018, 3, 11, 1, 59, 59) # 1:59:59 AM, March 11th, 2018
    # This is unambiguously not within the DST period
    dst_inactive_dt = datetime.datetime(2018, 3, 11, 0, 59, 59, tzinfo=ET()) # 12:59:59 AM, March 11th, 2018
    print(dst_inactive_dt.tzname()) # EST
    print(dst_inactive_dt.timetuple()) # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=0, tm_min=59, tm_sec=59, tm_wday=6, tm_yday=70, tm_isdst=0)
    print(dst_inactive_dt.utctimetuple()) # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=5, tm_min=59, tm_sec=59, tm_wday=6, tm_yday=70, tm_isdst=0)
    print(dst_inactive_dt.utcoffset()) # -1 day, 19:00:00, or -24 + 19 = -5 hours
    dst_active_dt = datetime.datetime(2018, 3, 11, 2, tzinfo=ET()) # 2:00 AM, March 11th, 2018
    print(dst_active_dt.tzname()) # EDT
    print(dst_active_dt.timetuple()) # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=2, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=70, tm_isdst=1)
    print(dst_active_dt.utctimetuple()) # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=6, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=70, tm_isdst=0)
    print(dst_active_dt.utcoffset()) # -1 day, 20:00:00, or -24 + 20 = -4 hours


def what_is_local_time():
    '''The fact that these two class methods return the same timestamp shows I implemented the ET class correctly'''
    print(datetime.datetime.today()) # 2019-11-27 18:01:28.225653
    print(datetime.datetime.now(ET())) # 2019-11-27 18:01:28.225750-05:00

if __name__ == '__main__':
    #perform_utc_conversion()
    what_is_local_time()