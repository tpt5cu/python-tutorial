# https://matplotlib.org/2.2.5/gallery/shapes_and_collections/line_collection.html?highlight=linecollection


import numpy as np
from matplotlib.collections import LineCollection
from matplotlib import pyplot as plt


def test():
    x = np.arange(100)
    # Here are many sets of y to plot vs x
    ys = x[:50, np.newaxis] + x[np.newaxis, :]
    print(ys)
    segs = np.zeros((50, 100, 2), float)
    segs[:, :, 1] = ys
    segs[:, :, 0] = x
    print(segs)


def create_line_collection():
    '''
    I GIVE UP
    '''
    segs = np.array([
        [[0, 1]],
        [[1, 2]],
        [[2, 3]]
    ])
    # 2 rows, 1 column, 2 deep
    print(segs.shape) # (2, 1, 2)
    print(segs)
    #lc = LineCollection(( # ValueError: 'vertices' must be a 2D list or array with shape Nx2
    #    (0, 0),
    #    (10, 10)
    #))
    #lc = LineCollection([ # ValueError: 'vertices' must be a 2D list or array with shape Nx2
    #    [0, 0],
    #    [10, 10]
    #])
    # I don't understand why this doesn't work. Perhaps the array must be 2 deep?
    #segs = np.zeros((10, 2)) # ValueError: 'vertices' must be a 2D list or array with shape Nx2
    # This works. <insert explanation once I can actually see the graph>
    #segs = np.zeros((10, 1, 2))
    #segs = np.zeros((50, 100, 2), float)
    colors = [
        (0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 1.0),
        (1.0, 0.4980392156862745, 0.054901960784313725, 1.0),
        (0.17254901960784313, 0.6274509803921569, 0.17254901960784313, 1.0)
    ]
    lc = LineCollection(segs, linewidths=(1.0, 1.0, 1.0), colors=colors, linestyle='solid')
    # Graph it just to see
    fig, ax = plt.subplots()
    #ax.set_xlim(0, 5)
    #ax.set_ylim(0, 5)
    ax.add_collection(lc)
    ax.autoscale()
    plt.show()


if __name__ == '__main__':
    #test()
    create_line_collection()
