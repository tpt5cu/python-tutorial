# https://matplotlib.org/2.2.5/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def create_axes_and_figure():
    '''
    The simplest use case of pyplot.subplots() is to create a figure with a single axes
    - Recall that the Figure is the final image that contains one or more Axes objects
    - Each Axes object represents an entire plot
        - "Axis" objects are different and actually represent the x or y axis of an Axes plot
    '''
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 400)
    # 400 floating point numbers in a 1-D array
    #print(x.shape) # (400,)
    y = np.sin(x**2)
    # 400 floating point numbers in a 1-D array
    #print(y.shape) # (400,)
    ax.plot(x, y)
    ax.set_title('My cool plot')
    plt.show()


if __name__ == '__main__':
    create_axes_and_figure()
