

import pathlib
import matplotlib
matplotlib.use('Tkagg')
from matplotlib import pyplot as plt
from matplotlib.axes._base import _AxesBase
from python_369.matplotlib_225.matplotlib_.figure_.Figure_ import create


def set_savefig_values():
    '''
    There are two ways to modify the savefig() attributes: rcParams and kwargs
    - E.g. Use the "facecolor" argument to savefig() or modify rcParams['savefig.facecolor']
    - <Figure>.savefig() has SEPARATE entries in rcParams! That's why setting the facecolor of Figure object doesn't appear to work! Who designed this?! Awful!
    '''
    fig = create.get_blank_standard_figure()
    #fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve())) # facecolor of savefig is white by default
    #fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve()), facecolor=(1, 0, 0, .5)) # Red at 50% opacity
    matplotlib.rcParams['savefig.facecolor'] = 'm'
    fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve())) # Magenta


def savefig_without_pyplot():
    '''
    - These notes are about using savefig() without using pyplot.subplots() to create the underlying figure and axes
    - savefig() saves everything as expected, except for certain attributes of the figure which are overridden by values within the savefig() function
      itself
        - These attributes are controlled directly by savefig(), not the figure itself:
            - dpi, facecolor, edgecolor, frameon, orientation, jpeg_quality, format, bbox, pad_inches, directory, transparent
        - See the default_rcparams_copy.py notes for details
    '''
    # The pyplot interactive image shows I'm positioning and coloring the objects correctly. I don't need to give special consideration to certain
    # Figure attributes because I'm not using savefig()
    #fig, ax = plt.subplots()
    #fig.set_facecolor('b')
    #ax.set_position((0, 0, .5, .5))
    #ax.set_facecolor('y')
    #plt.show()
    # When savefig() is used, I have to treat certain Figure attributes specially
    fig = create.get_blank_standard_figure()
    ax = fig.add_axes((0, 0, .5, .5))
    fig.set_facecolor('b')
    ax.set_facecolor('y')
    # This does not save correctly because the Figure facecolor is ignored
    #fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve()))
    # This saves correctly
    fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve()), facecolor=fig.get_facecolor())


def savefig_with_pyplot():
    '''
    The axes that is returned by pyplot.subplots() has some initial configuration. Thus, using pyplot.subplots() and savefig() together yields a
    different result than the above function example merely because of the different axes object, not because savefig() itself behaves any differently
    '''
    fig, ax = plt.subplots()
    ax = fig.add_axes((0, 0, .5, .5))
    fig.set_facecolor('b')
    ax.set_facecolor('y')
    # This does not save correctly because the Figure facecolor is ignored
    #fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve()))
    # This saves correctly
    fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve()), facecolor=fig.get_facecolor())


def add_subplot():
    '''
    Add a subplot and return the Axes objects of the subplot
    - There are several valid invocations:
        - <Figure>.add_subplot(<row><column><position>)
        - <Figure>.add_subplot(<row>, <column>, <position>)
    '''
    ax = fig.add_subplot(1,1,1)


def add_axes_to_figure():
    '''
    - <Figure>.add_axes(rect, projection=None, polar=False, **kwargs)
        - <Figure>.add_axes() works like a charm. It returns the axes that was just added to the Figure
    - Alternatively, why doesn't creating an _AxesBase object add that object to the Figure?
        - I don't know, but don't do it
    '''
    # Works well
    fig, ax = plt.subplots()
    ax = fig.add_axes((0, 0, .5, .5))
    fig.set_facecolor('c')
    ax.set_facecolor('r')
    #plt.show()
    # Doesn't work
    #fig = create.get_blank_standard_figure()
    #pos = (0, 0, .5, .5)
    #ax = _AxesBase(fig, pos)
    #ax.set_facecolor('b')
    #print(ax.get_figure()) # Figure(640x480)
    #print(fig.axes) # []
    fig.savefig(str((pathlib.Path(__file__).parent / 'test-figure.png').resolve()), facecolor=fig.get_facecolor())


if __name__ == '__main__':
    #set_savefig_values()
    #savefig_without_pyplot()
    #savefig_with_pyplot()
    add_axes_to_figure()
