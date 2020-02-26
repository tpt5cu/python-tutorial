# https://markhneedham.com/blog/2018/05/04/python-runtime-error-osx-matplotlib-not-installed-as-framework-mac/ - avoid RuntimeError
# https://stackoverflow.com/questions/17538235/unable-to-save-matplotlib-figure-figure-canvas-is-none - avoid AttributeError
# https://stackoverflow.com/questions/47226172/matplotlib-inline-facecolor-not-working-on-savefig - savefig() has separate rcParams


import pathlib
import matplotlib
matplotlib.use('TkAgg') # Avoid the RuntimeError
from matplotlib import figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas # Avoid AttributeError


'''The figure module contains several classes, one of which is the almighty Figure'''


def create_nonviewable_figure():
    '''
    <Figure>.show() shows the Figure.
    - Figure objects can only be shown with a GUI backend provided by pyplot
        - To get around this, just save the Figure
    - In order to save the Figure without the RuntimeError, I need to switch the backend from "macosx" (defined in the matplotlibrc file) to something
      else like "TkAgg" (see link)
        - In order to get around the AttributeError, see the second link
            - TLDR: I need a Canvas object to tell the Artist object(s) (i.e. Figure objects) to draw themselves ON the canvas. A Canvas object is
              specific to a backend. pyplot handles all of this for me, but without pyplot I have to create a Canvas object myself
    '''
    # Create a massive 10" * 10" figure
    fig = figure.Figure((10, 10))
    canvas = FigureCanvas(fig)
    #fig.show() # AttributeError: 'NoneType' object has no attribute 'manager'
    path = (pathlib.Path(__file__).parent / 'test-figure.png').resolve()
    fig.savefig(str(path), facecolor='r') 
    # The canvas can ALSO save the image, but it's not necessary.
    # <Canvas>.print_figure(<filename>)
    #canvas.print_figure('test')


def create_viewable_figure():
    '''Need pyplot to show() a figure'''
    fig, ax = plt.subplots()
    fig.set_facecolor('y')
    ax.set_facecolor('b')
    plt.show()


def get_blank_standard_figure():
    fig = figure.Figure()
    canvas = FigureCanvas(fig)
    return fig


if __name__ == '__main__':
    create_nonviewable_figure()
    #create_viewable_figure()
