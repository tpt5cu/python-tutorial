# https://matplotlib.org/2.2.5/gallery/shapes_and_collections/line_collection.html?highlight=linecollection - LineCollection tutorial


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.collections import LineCollection
from matplotlib import pyplot as plt


'''Artist and ScalarMappable <- Collection <- LineCollection'''


def create_linecollection():
    '''
    According to the LineCollection tutorial: "We need to set the plot limits, they will not autoscale"
    - The autoscale() method works!
        - It is NOT implicitly invoked
    - LineCollection objects don't have a __len__() nor are they iterable
    '''
    segments = [
        [(0, 0), (5, 5)], # line_0 # 2 points
        [(1, 1.1), (6, 6)], # line_1 # 2 points
        [(2, 2), (4, 0), (10, 1)] # line_2: 3 points
    ]
    lc = LineCollection(segments)
    lc.set_color(('r', 'g', 'b'))
    fig, ax = plt.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    #ax.set_xlim(0, 10)
    #ax.set_ylim(0, 10)
    plt.show()


if __name__ == '__main__':
    create_linecollection()
