# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior


import datetime


"""
strftime() and strptime() are NOT the same at all!
- <datetime>.strftime() creates a string representing a datetime.
- <datetime>.strptime() creates a datetime from a string.
"""


def get_day_of_week():
    """Use <datetime>.strftime() to get a string that represents the datetime in whatever format I want."""
    dt = datetime.datetime.today()
    #dt = datetime.datetime.today() - datetime.timedelta(hours=24)
    print(dt.strftime("%a")) # Whatever the day of the week it is


if __name__ == "__main__":
    get_day_of_week()