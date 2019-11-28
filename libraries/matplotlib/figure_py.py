# https://matplotlib.org/3.1.0/tutorials/intermediate/artists.html#sphx-glr-tutorials-intermediate-artists-py


import matplotlib.pyplot as plt

"""
Create a Figure to draw 1 or more Axes onto. Use matplotlib.pyplot.figure() instead of matplotlib.figure.Figure() because the former does some
behind-the-scenes work including connecting my figure to the matplotlib backend (I don't even want to know)
"""

def basic_figure():
    """
    Return a new figure and hook it to the backend automatically. Everytime this function is called a new figure is created. If it's called once, a
    single graph will appear once the script starts. If I call this function inside of a for-loop with 10 iterations, I'll get 10 different graph
    windows upon script invocation.
    """
    my_figure = plt.figure() 