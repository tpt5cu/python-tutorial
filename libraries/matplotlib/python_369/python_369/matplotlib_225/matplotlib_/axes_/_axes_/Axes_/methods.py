import matplotlib
matplotlib.use('Tkagg')
from matplotlib import pyplot as plt


def plot_single_line():
    '''
    plot() returns a list of Line2D objects representing the plotted data
    - plot() can be styled with Line2D attributes as well as marker attributes
    '''
    fig, ax = plt.subplots()
    x = [0, 100, 50, 1]
    y = [10, 200, 20, 4]
    lines = ax.plot(x, y, linestyle='-.', color='r')
    print(type(lines)) # <class 'list'>
    print(len(lines)) # 1
    print(type(lines[0])) # <class 'matplotlib.lines.Line2D'>
    plt.show()


if __name__ == '__main__':
    plot_single_line()
