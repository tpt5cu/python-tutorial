import networkx as nx
from networkx.drawing import nx_agraph
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def get_matplotlib_object_that_represents_graph_edges():
    '''
    networkx.drawing.nx_pylab.draw_networkx_edges() returns a matplotlib.collection.LineCollection
    - A graph object and a dictionary of positions are both required arguments to draw_networkx_edges()
    - matplotlib v3.1.3 (Stable version) is incompatible with networkx v1.11
    - matplotlib v2.2.5 (LTS version) is compatible with networkx v1.11
    '''
    g = nx.bull_graph()
    pos = nx_agraph.graphviz_layout(g)
    lc = nx.drawing.nx_pylab.draw_networkx_edges(g, pos)
    lc.set_color(('r', 'g', 'b'))
    fig, ax = plt.subplots()
    #ax.add_collection(lc)
    #ax.autoscale()
    #plt.show()


if __name__ == '__main__':
    get_matplotlib_object_that_represents_graph_edges()
