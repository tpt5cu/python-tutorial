import time


def get_local_time_string():
    t = time.time()
    print(t) # floating point number
    lt = time.localtime(t)
    print(lt) # struct_time
    #st = time.strftime("%a", t) # TypeError. strftime() needs a struc_time, not a floating point number
    # If a struct_time is not provided to strftime(), it uses the current local time
    st = time.strftime("%a", lt) # Day of week
    st = time.strftime("%d %H %M %S") # Day of month, hour (24 hr), minute, second
    st = time.strftime("%a %I:%M:%S") # Day of week, hour (12 hr), minute, second
    print(st)


def seconds_to_date_and_time():
    """
    Matthew Shawver's email was sent on Sep 4, 2019, 1:29 PM. That puts the milliseconds value in context. The %x and %X directives are concise ways
    of getting local date and local time, respectively
    """
    milliseconds = 1567615082000
    #seconds = milliseconds/1000.1
    seconds = 799693200.0
    lt = time.localtime(seconds)
    print(time.strftime("%x %X", lt)) # 09/04/19 12:38:02


def date_and_time_to_seconds():
    """
    - If a time is parsed according to a 24-hour clock, the hour range is [0, 23]. Therefore an hour of 12 would be equal to 1 pm
        - The %p option doesn't affect a 24-hour clock
    - If a time is parsed according to a 12-hour clock, the hour range is [1, 12]. Therefore an hour of 12 would equal 
        - The %p option does affect a 12-hour clock
    """
    date_string = "May 5 1995 12:00:00 AM UTC"

    st = time.strptime(date_string, "%B %d %Y %H:%M:%S %p %Z") # Get a struct_time from a string
    print(st) # time.struct_time(tm_year=1995, tm_mon=5, tm_mday=5, tm_hour=12, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=125, tm_isdst=0)
    seconds = time.mktime(st) # Get seconds from a struct_time
    print(seconds) # 799693200.0

    st = time.strptime(date_string, "%B %d %Y %I:%M:%S %p %Z") # Get a struct_time from a string
    print(st) # time.struct_time(tm_year=1995, tm_mon=5, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=125, tm_isdst=0)
    seconds = time.mktime(st) # Get seconds from a struct_time
    print(seconds) # 799650000.0


if __name__ == "__main__":
    #get_local_time_string()
    #seconds_to_date_and_time() 
    date_and_time_to_seconds()