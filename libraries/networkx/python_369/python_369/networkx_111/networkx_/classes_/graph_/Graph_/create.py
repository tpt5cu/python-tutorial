# https://networkx.github.io/documentation/networkx-1.11/tutorial/tutorial.html


from networkx.classes.graph import Graph


def create_empty_graph():
    '''Create an empty graph with no nodes or edges'''
    g = Graph()
    print(type(g)) # <class 'networkx.classes.graph.Graph'>


def create_graph_with_edges():
    '''
    The data can be an edge list, or any NetworkX graph object, but not a list of nodes!
    - It can't be a list of nodes because a bunch of unconnected nodes don't compose a very interesting graph
    - Nodes can be any hashable object. Recall that immutable objects are implicitly hashable: int, string, tuple, etc.
    '''
    g = Graph([(1, 'foo'), (1, 3)])
    nodes = g.nodes()
    print(type(nodes)) # <class 'list'>
    print(nodes) # [1, 'foo', 3]
    g.nodes()[0] = 5
    print(g.nodes()) # [1, 'foo', 3]


if __name__ == '__main__':
    #empty_graph()
    create_graph_with_edges()
