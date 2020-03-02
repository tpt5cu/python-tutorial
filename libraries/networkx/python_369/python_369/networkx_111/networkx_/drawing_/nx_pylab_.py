import networkx as nx
from networkx.drawing import nx_agraph
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


'''
SUPER DUPER IMPORTANT: Creating a figure (and probably an Axes) must happen BEFORE any networkx drawing code is called!
'''


def get_matplotlib_object_that_represents_graph_edges():
    '''
    networkx.drawing.nx_pylab.draw_networkx_edges() returns a matplotlib.collection.LineCollection
    - A graph object and a dictionary of positions are both required arguments to draw_networkx_edges()
    - Optionally, I can provide a list of edges in which case only the provided edges will be drawn
    - Version incompatibilities:
        - networkx==1.11 and matplotlib==2.2.5 draws fine
            - The LineCollection is sneakily autoscaled! This is not standard in matplotlib
        - networkx==1.11 and matplotlib==3.1.3 fails to run successfully
        - networkx==2.4 and matplotlib==2.2.5 draws fine
            - Need to invoke autoscale()
        - networkx==2.4 and matplotlib==3.1.3 draws fine
            - Need to invoke autoscale()
    '''
    fig, ax = plt.subplots() # Works fine
    g = nx.bull_graph()
    pos = nx_agraph.graphviz_layout(g)
    print(g.edges()) # [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4)]
    lc = nx.drawing.nx_pylab.draw_networkx_edges(g, pos)
    #lc = nx.drawing.nx_pylab.draw_networkx_edges(g, pos, edgelist=[(0, 1)])
    #fig, ax = plt.subplots() # Causes RuntimeError
    lc.set_color(('r', 'g', 'b', 'y', 'c', 'm', 'k'))
    ax.add_collection(lc)
    ax.autoscale()
    plt.show()


if __name__ == '__main__':
    get_matplotlib_object_that_represents_graph_edges()
