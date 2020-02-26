'''An _AxesBase object is an Artist object'''


import pathlib
from python_369.matplotlib_225.matplotlib_.figure_.Figure_ import create
import matplotlib
from matplotlib.axes._base import _AxesBase


def create_axesbase():
    '''
    - TLDR: don't create these objects directly. Instead, just use the <Figure>.add_axes() function
    - __init__(self, fig, rect, facecolor=None, frameon=True, sharex=None, sharey=None, label='', xscale=None, yscale=None, **kwargs)
        - When an _AxesBase instance is created, it must be created on a Figure (fig) with coordinates (rect)
            - <rect> = a sequence of four floats: <left>, <bottom>, <width>, <height>
                - Each float is in fractions of figure width and height
    - The _AxesBase sees it has a Figure, but the Figure doesn't see that is has the _AxesBase
        - The only thing I can think of is that a Figure object needs its own pointer(s) to its Artists AND the artists need their own pointers to
          their Figure
            - The documentation says that is only possible to do <Figure>.add_axes(<axes object>) if there is "an Axes instance already created in the
              present figure but not in the figure's list of axes," but I can't get it to work
    '''
    # This does not work
    fig = create.get_blank_standard_figure()
    fig.set_facecolor((1, 0, 0, .5))
    ax = _AxesBase(fig, (0, 0, .5, .5), facecolor='g')
    print(ax.get_figure()) # Figure(640x480)
    print(fig.axes) # []
    #fig.add_axes(ax) # TypeError
    #fig.savefig(str(pathlib.Path(__file__).parent / 'axesbase-figure.png'), facecolor=fig.get_facecolor(), transparent=True)


if __name__ == '__main__':
    create_axesbase()
