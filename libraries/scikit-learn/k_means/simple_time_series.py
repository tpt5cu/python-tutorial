"""
https://stackoverflow.com/questions/44945098/how-can-i-use-knn-k-means-to-clustering-time-series-in-a-dataframe
"""


# Copied from stackoverflow
import pandas as pd
import numpy as np
import random
from dtw import dtw
from matplotlib.pyplot import plot
from matplotlib.pyplot import imshow
from matplotlib.pyplot import cm
import matplotlib.pyplot as plt  

from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer 
#About classification, read the tutorial
#http://scikit-learn.org/stable/tutorial/basic/tutorial.html


def createTs(myStart, myLength):
    # Starting at a certain time, create "myLength" time measurements every hour
    index = pd.date_range(myStart, periods=myLength, freq='H'); 
    # Generate "myLength" number of floats, each in the range [0.0, 1.0)
    values = [random.random() for _ in range(myLength)]
    # Create a Series object that contains the random floats labeled by time
    series = pd.Series(values, index=index);  
    return(series)


# Time series of length 30, start from 1/1/2000 & 1/2/2000 so overlap
myStart='1/1/2000'
myLength=30
timeS1=createTs(myStart, myLength)
myStart='1/2/2000'
timeS2=createTs(myStart, myLength) 

# This could be your dataframe but unnecessary here
#myDF = pd.DataFrame([x for x in timeS1.data], [x for x in timeS2.data])#, columns=['data1', 'data2'])

# Take the values in the timeS1 Series and increase their magnitude by 100 so that timeS1 looks significantly different from timeS2. Also sort timeS1
# so it looks even more different from timeS2
x = [x * 100 for x in sorted(timeS1)]
y = [x for x in timeS2]


def view_timeseries():
    print(timeS1)
    print(timeS2)
    print(x)
    print(y)


def draw_timeseries():
    plot(x)
    plot(y)
    plt.show()


def show_dtw():
    # DTW with the 1st order norm
    myDiff = [xx - yy for xx, yy in zip(x,y)]
    dist, cost, acc, path = dtw(x, y, dist=lambda x, y: np.linalg.norm(myDiff, ord=1))
    imshow(acc.T, origin='lower', cmap=cm.gray, interpolation='nearest')
    plot(path[0], path[1], 'w')
    plt.show()


if __name__ == "__main__":
    #examine_timeseries()
    draw_timeseries()
    #show_dtw()