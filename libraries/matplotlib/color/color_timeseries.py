"""
https://stackoverflow.com/questions/25408393/getting-individual-colors-from-a-color-map-in-matplotlib
"""


import datetime
import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


"""
1) Specify the color per line during the <Axes>.plot() call
"""


def create_hourly_timeseries(start_dt, hours):
    time = []
    data = []
    for i in range(hours):
        td = datetime.timedelta(hours=i)
        cur_time = start_dt + td
        time.append(cur_time)
        data.append(random.random())
    return (time, data)


def plot(timeseries, colors):
    """ This is how to 1) get a colormap from matploblib and 2) use floats to get values from the colormap """
    # type: (list) -> None
    cmap = matplotlib.cm.get_cmap('viridis')
    fig = plt.figure()
    idx = 0
    for t in timeseries:
        time, data = t
        ax = fig.add_subplot()
        ax.plot(time, data, color=cmap(colors[idx]))
        idx += 1
    plt.show()


def main():
    time_series = []
    colors = []
    start = datetime.datetime(2000, 1, 1)
    for x in range(100):
        ts = create_hourly_timeseries(start, 1000)
        #color = "#0000ff"
        color = 0.1
        if x % 7 == 0:
            new_data = sorted([x * 3 for x in ts[1]])
            ts = (ts[0], new_data)
            #color = "#ff00ff"
            color = 0.5
        time_series.append(ts) 
        colors.append(color)
    plot(time_series, colors)


if __name__ == "__main__":
    main()