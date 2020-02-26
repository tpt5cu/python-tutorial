# https://matplotlib.org/2.2.5/gallery/shapes_and_collections/line_collection.html?highlight=linecollection


import networkx as nx
from networkx.drawing import nx_agraph
import matplotlib.pyplot as plt



def get_matplotlib_object_that_represents_graph_edges():
    '''
    networkx.drawing.nx_pylab.draw_networkx_edges() returns a matplotlib.collection.LineCollection
    - A graph object and a dictionary of positions are both required arguments to draw_networkx_edges()
    - matplotlib v3.1.3 (Stable version) is incompatible with networkx v1.11
    - matplotlib v2.2.5 (LTS version) is compatible with networkx v1.11
    '''
    g = nx.bull_graph()
    pos = nx_agraph.graphviz_layout(g)
    mpl_lc = nx.drawing.nx_pylab.draw_networkx_edges(g, pos)
    # TODO: How do I plot a LineCollection?
    print(type(mpl_lc)) # <class 'matplotlib.collections.LineCollection'>

    # Doesn't work
    #fig = plt.figure()
    #ax = fig.add_subplot(1, 1, 1)
    #ax.add_collection(mpl_lc) # RuntimeError: Can not put single artist in more than one figure
    # Doesn't work
    #fig, ax = plt.subplots()
    #ax.add_collection(mpl_lc) # RuntimeError: Can not put single artist in more than one figure
    # Doesn't work
    #plt.plot(mpl_lc) # TypeError: float() argument must be a string or a number, not 'LineCollection'

    plt.show()


if __name__ == '__main__':
    get_matplotlib_object_that_represents_graph_edges()
