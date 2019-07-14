"""
https://matplotlib.org/3.1.0/api/axes_api.html#matplotlib-axes - Axes doc
https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot - basic add
https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_axes - complex add
https://stackoverflow.com/questions/31726643/how-do-i-get-multiple-subplots-in-matplotlib
"""


import numpy as np
from matplotlib import pyplot as plt


"""
Axes is the most important Artist subclass. It has all of the juicy methods for plotting specific types of graphs
"""

def easy_way_to_add_axes():
    """
    Figure.add_subplot() with no arguments is the easiest way to add a single Axes to a figure. I can stack multiple Axes onto a figure with repeated
    calls of this method. Currently, calling this function with the same arguments will reuse the same Axes (to prevent accidentally creating 736
    different Axes! However, in the future this call will always return a new Axes object)
    - The index of a Subplot refers to its position within the specified grid. Indexes start at 1 (argh!). E.g. add_subplot(2, 2, 1) means add a Subplot with 2 rows and 2 columns
      and place the Subplot in the top left corner of the 2 x 2 square. The index cannot exceed the specified grid. E.g in the previous example, index
      >= 5 or index <= 0 would raise an Exception
    """
    my_figure = plt.figure()
    my_axes = my_figure.add_subplot() # equivalent to add_subplot(1, 1, 1): add a single axes with 1 row, 1 column, and an index of 1
    line = my_axes.plot(range(0, 10), range(10, 0, -1)) # create a Line2D instance and add it to <Axes>.lines. Also return a LIST of Line2D objects on the Axes
    print(line) # [<matplotlib.lines.Line2D object at 0x10dfe56a0>]
    print(line[0]) # Line2D(_line0)
    print(line[0] is my_axes.lines[0]) # True
    another_axes = my_figure.add_subplot()
    another_axes.plot(range(0, 10), np.full((10,), 5))
    plt.show()


def easy_way_with_grid_specification():
    fig = plt.figure()
    # This will make a tiny Axes in the top left corner of the Figure
    ax = fig.add_subplot(2, 2, 1)
    ax.plot(range(0, 10), range(10, 0, -1))
    ax = fig.add_subplot(2, 2, 2)
    ax.plot(range(0, 10), range(0, 10))
    ax = fig.add_subplot(3, 3, 1)
    ax.plot(range(0, 10), np.full((10,), 3))
    plt.show()



def complex_add_axes():
    """ <Figure>.add_axes() requires me to specify the exact location of the Axes in the Figure, or to pass an existing Axes object as an argument """
    fig = plt.figure()
    fig.add_axes()


if __name__ == "__main__":
    #easy_way_to_add_axes()
    easy_way_with_grid_specification()
    #complex_add_axes()