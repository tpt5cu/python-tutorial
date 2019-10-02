# https://stackoverflow.com/questions/3694487/in-python-how-do-you-convert-seconds-since-epoch-to-a-datetime-object


import datetime


def get_local_datetime_from_seconds(seconds):
    """EDT is 4 hours behind UTC"""
    dt = datetime.datetime.fromtimestamp(seconds)
    print(dt)


def get_utc_datetime_from_seconds(seconds):
    dt = datetime.datetime.utcfromtimestamp(seconds)
    print(dt)

if __name__ == '__main__':
    get_local_datetime_from_seconds(1563321600) # 2019-07-16 20:00:00
    get_utc_datetime_from_seconds(1563321600) # 2019-07-17 00:00:00
    get_utc_datetime_from_seconds(1560686400) # 2019-06-16 12:00:00