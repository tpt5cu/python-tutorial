# https://stackoverflow.com/questions/14324270/matplotlib-custom-marker-symbol - custom marker
# https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line - might be helpful


import matplotlib
matplotlib.use('Tkagg')
from matplotlib import pyplot as plt
from matplotlib import markers # markers is a module inside of matplotlib


'''
Valid marker values:
- '.': 'point',
- ',': 'pixel',
- 'o': 'circle',
- 'v': 'triangle_down',
- '^': 'triangle_up',
- '<': 'triangle_left',
- '>': 'triangle_right',
- '1': 'tri_down',
- '2': 'tri_up',
- '3': 'tri_left',
- '4': 'tri_right',
- '8': 'octagon',
- 's': 'square',
- 'p': 'pentagon',
- '*': 'star',
- 'h': 'hexagon1',
- 'H': 'hexagon2',
- '+': 'plus',
- 'x': 'x',
- 'D': 'diamond',
- 'd': 'thin_diamond',
- '|': 'vline',
- '_': 'hline',
- 'P': 'plus_filled',
- 'X': 'x_filled',
- TICKLEFT: 'tickleft',
- TICKRIGHT: 'tickright',
- TICKUP: 'tickup',
- TICKDOWN: 'tickdown',
- CARETLEFT: 'caretleft',
- CARETRIGHT: 'caretright',
- CARETUP: 'caretup',
- CARETDOWN: 'caretdown',
- CARETLEFTBASE: 'caretleftbase',
- CARETRIGHTBASE: 'caretrightbase',
- CARETUPBASE: 'caretupbase',
- CARETDOWNBASE: 'caretdownbase',
- "None": 'nothing',
- None: 'nothing',
- ' ': 'nothing',
- '': 'nothing'

Valid fillstyle values:
- "full"
- "left"
- "right"
- "bottom"
- "top"
- "none"
'''


def create_markerstyle():
    '''
    A MarkerStyle object encapsulates all of the information about the marker that is drawn at each point for <Axes>.plot() and <Axes>.scatter()
    - Are MarkerStyle objects used elsewhere? The documentation only specifies those two Axes functions
    - Actually it doesn't look like I can use MarketStyle objects directly. How very, very annoying!
    '''
    # __init__(self, marker=None, fillstyle=None)
    ms = markers.MarkerStyle('o', 'left')
    fig, ax = plt.subplots()
    x = [0, 100, 50, 1]
    y = [10, 200, 20, 4]
    lines = ax.plot(x, y)
    # These don't work
    #lines = ax.plot(x, y, marker=ms) # TypeError: float() argument must be a string or a number, not 'MarkerStyle'
    #lines[0].set_marker(ms) # TypeError: float() argument must be a string or a number, not 'MarkerStyle'
    # This works but is pretty informal!
    lines[0].set_marker('o')
    plt.show()


if __name__ == '__main__':
    create_markerstyle()
