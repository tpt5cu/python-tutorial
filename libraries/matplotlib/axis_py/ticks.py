# https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.xticks.html - xticks on the pyplot object. Not object-oriented so not what I want
# https://matplotlib.org/3.1.0/gallery/text_labels_and_annotations/date.html - good example
# https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior - format strings for Formatter objects
# https://stackoverflow.com/questions/1574088/plotting-time-in-python-with-matplotlib - how to plot time, NOT datetime, with matplotlib


import datetime, random
import matplotlib
from matplotlib import pyplot as plt


"""
Modify the "Locator" of an Axis to control the location of ticks. Modify the "Formatter" of an Axis to control the text on the ticks. It appears that
all locators have a "MAXTICKS" property of 1000. If I have 910 or more points that need to be plotted on the x-axis, doing:
- hours = matplotlib.dates.HourLocator()
- ax.get_xaxis().set_major_locator(hours)
will throw a RuntimeError. This is because matplotlib assumes that every piece of data to be plotted on the x-axis represents an hour.
"""


def create_hourly_timeseries(start_dt, hours):
    """
    It appears that matplotlib will NOT plot regular Python datetime.time objects, only datetime.datetime objects. matplotlib represents dates as
    floats, where each float represents the number of days since 0001-01-01. Therefore, matplotlib has no concept of a "time of day" without an
    associated day.

    Also, I'm supposed to convert regular datetimes to matplotlib datetimes with matplotlib.dates.date2num(), but pandas apparently does this for me.
    """
    time = []
    data = []
    td = datetime.timedelta(hours=1)
    for i in range(hours):
        cur_time = start_dt + td * i
        #cur_time = cur_time.time()
        time.append(cur_time)
        data.append(random.random())
    return (time, data)


def set_major_tick_and_minor_ticks():
    start = datetime.datetime(2000, 1, 1)
    fig = plt.figure() # Move this outside the for-loop because I want all Axes stacked on top of 1 figure
    """
    Even with 100 different time series, the tick marks appear just fine
    """
    for i in range(5):
        time, data = create_hourly_timeseries(start, 100)
        data = [x * i for x in data] # add some variation to the data
        ax = fig.add_subplot()
        #ax.plot(time, data)
        ax.plot_date(time, data)
        """
        Tell matplotlib that every piece of x-axis data is an hourly measurement and that it should mark the 23rd hour of every day with a tick
        - The "byhour" parameter of HourLocator() is restricted to be in the range of [0, 23]
        - The "byminute" parameter of MinuteLocator() is restricted to be in the range of [0, 59]
        - I cannot use the "interval" and "by<whatever>" arguments together. It seems like I should be able to, but I can't.
        - 1000/23 = about 43 major ticks
        """
        #hours = matplotlib.dates.HourLocator() # too many ticks
        #hours = matplotlib.dates.HourLocator(byhour=[23]) # tick on the last hour of every day
        hours = matplotlib.dates.HourLocator(byhour=[0]) # tick on the first hour of every day
        ax.get_xaxis().set_major_locator(hours)
        """
        Tick on the 0th minute of every hour. Therefore, every 23rd-hour-major-tick gets 23 0th-minute-minor-ticks after it. Since there are 1000 hours,
        there will be 1000/23 * 23 = 1000 minor ticks created, which is too many!
        """
        #minutes = matplotlib.dates.MinuteLocator(byminute=[0]) # too many ticks
        #minutes = matplotlib.dates.MinuteLocator(interval=100) # tick on every 100th minute. Looks ugly
        minutes = matplotlib.dates.MinuteLocator(interval=120) # mark every 120th minute, for a minor tick every 2 hours
        ax.get_xaxis().set_minor_locator(minutes)
        """
        Restrict the range of the graph so there is less whitespace on either side of the data. This makes the graph look squashed if I limit the graph to
        the first and last datetime
        """
        one_hour = datetime.timedelta(hours=1)
        datemin = time[0] - one_hour
        datemax = time[-1] + one_hour
        ax.set_xlim(datemin, datemax)
        """
        By default, matplotlib will represent a datetime with hourly detail as "mm-dd hh" I can specify an alternative format with a Formatter object.
        Formatter objects are smart. No matter what format I choose, the real data measurements are still apparent.
        - If I specify a year with %Y, then all ticks are marked with 2000 (since that is indeed the year of all of the datetimes) except for
        the very first tick, which is marked with 1999
        - If I specify a minute with %M, then all ticks are marked with 0 since every tick is an hourly measurement exactly
        """
        str_format = "%Y-%H-%M" # 2000-23-00, 2000-23-00 representing the year, hour, and minute of every tick (they are the same)
        str_format = "%j" # 001, 002, 003 representing days of th year
        hours_fmt = matplotlib.dates.DateFormatter(str_format)
        #ax.xaxis.set_major_formatter(hours_fmt)
    plt.show()


if __name__ == "__main__":
    set_major_tick_and_minor_ticks()
    