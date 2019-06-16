"""
https://matplotlib.org/3.1.0/tutorials/intermediate/artists.html#sphx-glr-tutorials-intermediate-artists-py
"""

import matplotlib.pyplot as plt

"""
 Create a Figure to draw 1 or more Axes onto. Use matplotlib.pyplot.figure() instead of matplotlib.figure.Figure() because the former does some
 behind-the-scenes work including connecting my figure to the matplotlib backend (I don't even want to know)
"""

def basic_figure():
    """ Return a new figure and hook it to the backend automatically """
    my_figure = plt.figure() 