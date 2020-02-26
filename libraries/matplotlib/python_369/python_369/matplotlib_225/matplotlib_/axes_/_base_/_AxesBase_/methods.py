import matplotlib
matplotlib.use('Tkagg')
from matplotlib import pyplot as plt


'''Setting the xlim and ylim on the _AxesBase manually is nice, but autoscale() is nicer!'''


def set_xlim_():
    '''
    Set the leftmost and rightmost limits of the x-axis. Pretty simple
    - set_xlim(self, left=None, right=None, emit=True, auto=False, **kw)
    '''
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_facecolor('r')
    plt.show()


def set_ylim_():
    '''
    Set the lowest and highest limits of the y-axis. Pretty simple
    - set_ylim(self, bottom=None, top=None, emit=True, auto=False, **kw)
    '''
    fig, ax = plt.subplots()
    ax.set_ylim(-10, 10)
    ax.set_facecolor('g')
    plt.show()


def autoscale_():
    '''
    This is for automatically scaling the axes object, as set_xlim() and set_ylim() were being called
    - It appears to be enabled by default
    '''
    fig, ax = plt.subplots()
    ax.set_facecolor('g')
    x = [0, 100, 50, 1]
    y = [10, 200, 20, 4]
    print(ax.get_autoscale_on()) # True
    #ax.autoscale(False) # I can't see anything!
    ax.plot(x, y)
    plt.show()


def autoscale_view_():
    '''
    This is for ?
    '''
    pass

if __name__ == '__main__':
    #set_xlim_()
    #set_ylim_()
    autoscale_()
