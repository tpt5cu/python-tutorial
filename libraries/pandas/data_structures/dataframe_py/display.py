"""
https://stackoverflow.com/questions/34347145/pandas-plot-doesnt-show
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
https://matplotlib.org/tutorials/introductory/usage.html#figure-parts - matplotlib overview
https://matplotlib.org/tutorials/introductory/pyplot.html - pyplot interface
"""


import matplotlib.pyplot as plt
import pandas as pd
import create


"""
matplotlib is required for drawing nice plots of pandas DataFrames. matplotlib is NOT the same as MATLAB, which is proprietary software. However,
matplotlib is modeled after MATLAB.

The pyplot interface preserves the state on the same "figure" across function calls. The term "figure" refers to the ENTIRE visualization including
the "axes", the title of the visualization, x-axis label, y-axis label, etc.
- Clear the current figure with pyplot.clf().
Plotting functions are directed towards the current "axes".  The term "axes" refers to the numerical plotting area of the figure. The "axes" contains
1 or more "axis" objects.
- Clear the current axes with pyplot.cla()

"""

def view_with_pyplot():
    """ If my data is not numeric (e.g. it contains random words), pandas will throw an error instead of trying to plot something """
    df = pd.DataFrame(create.get_numeric_matrix())
    #df.plot()
    #df.plot.area()
    #df.plot.bar()
    df.plot.barh()
    plt.show() 
    plt.close()


def view():
    pass


if __name__ == "__main__":
    view_with_pyplot()