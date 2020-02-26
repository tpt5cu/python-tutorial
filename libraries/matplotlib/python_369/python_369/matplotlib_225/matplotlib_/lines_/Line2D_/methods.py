import matplotlib
matplotlib.use('Tkagg')
from matplotlib import pyplot as plt


def set_linestyle_():
    '''
    - The linestyle is how the line itself is drawn. Nothing more, nothing less
        - It doesn't control whether or not individual points along the line are connected. That's drawstyle
    - Valid linestyle values:
        - "-" or "solid": solid line
        - "--" or  "dashed": dashed line
        - "-." or  "dashdot": dash-dotted line
        - ":" or "dotted": dotted line
        - "None": draw nothing
        - " ": draw nothing
        - '': draw nothing
    '''
    fig, ax = plt.subplots()
    x = [0, 100, 50, 1]
    y = [10, 200, 20, 4]
    lines = ax.plot(x, y)
    print(len(lines)) # 1
    #lines[0].set_linestyle('-.')
    lines[0].set_linestyle(':')
    #lines[0].set_linestyle('None')
    plt.show()


def set_drawstyle_():
    '''
    - The drawstyle is
    - Valid drawstyle values:
        - "default": connect each point along the line with a line that minimizes the distance between the points
        - "steps": connect each point along the line with a line that ascends/descends along the y-axis to the next point's y-value before traversing
          along the x-axis (it's weird)
        - "steps-pre": an alias for "steps"
        - "steps-mid": I can't describe
        - "steps-post": seems the same as "steps" except the y-axis ascent/descent happens at the midpoint of two adjacent x-values
    - There is not an option to not connect points with lines! 
        - Do that with linestyle
    '''
    fig, ax = plt.subplots()
    x = [0, 100, 50, 1]
    y = [10, 200, 20, 4]
    lines = ax.plot(x, y)
    #lines[0].set_drawstyle('steps-mid')
    lines[0].set_drawstyle('steps-post')
    plt.show()


def set_color_():
    '''set the color of the line with any matplotlib color'''
    pass


def set_marker_():
    '''Set the marker'''
    fig, ax = plt.subplots()
    x = [0, 100, 50, 1]
    y = [10, 200, 20, 4]
    lines = ax.plot(x, y)
    lines[0].set_linestyle('None') # No connecting lines
    lines[0].set_marker('o')
    lines[0].set_markeredgecolor('r')
    lines[0].set_markerfacecolor('g')
    plt.show()


if __name__ == '__main__':
    #set_linestyle_()
    #set_drawstyle_()
    set_marker_()
