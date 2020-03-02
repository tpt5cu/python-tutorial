# https://networkx.github.io/documentation/networkx-1.11/tutorial/tutorial.html


from networkx.classes.graph import Graph


def create_empty_graph():
    '''Create an empty graph with no nodes or edges'''
    g = Graph()
    print(type(g)) # <class 'networkx.classes.graph.Graph'>


def create_graph_with_new_data():
    '''
    - Parallel edges are not allowed
    - The data can be:
        - An edge list
        - Any NetworkX graph object
    - The data cannot be a flat list of nodes!
        - It can't be a list of nodes because a bunch of unconnected nodes don't compose a very interesting graph
            - Nodes can be any hashable object. Recall that immutable objects are implicitly hashable: int, string, tuple, etc.
    '''
    # Create with edge list. Since this is an undirected graph, there is only one edge between 1 and 3
    g = Graph([(1, 'foo'), (1, 3), (3, 1)]) 
    g.add_node(6)
    # Create with another graph
    print(g.nodes()) # [1, 'foo', 3, 6]
    print(g.edges()) # [(1, 'foo'), (1, 3)]


def create_graph_from_graph():
    '''Passing another graph object appears to have the same net result as <Graph>.copy()'''
    g = Graph([(1, 5), (5, 5)])
    g.add_node(6)
    h = Graph(g) 
    print(h.nodes()) # [1, 5, 6]
    print(h.edges()) # [(1, 5), (5, 5)]
    g.node[1]['color'] = 'black'
    print(g.node[1]) # {'color': 'black'}
    print(h.node[1]) # {}


def bad_create_graph():
    '''NetworkX does not view a flat list as a list of edges'''
    g = Graph([1, 2]) # networkx.exception.NetworkXError: Input is not a valid edge list


def create_graph_from_nodes():
    '''
    - Don't use this strategy alone to copy a graph
    - None of the arbitrary attributes from nodes, edges, or the graph are copied
    - If the nodes of a graph object are used to create a new graph object:
        - No edges are created in the new graph.
    '''
    g = Graph([(1, 5), (5, 5)])
    g.graph['baz'] = 'boo'
    g.add_node(6)
    print(g.nodes()) # [1, 5, 6]
    print(g.edges()) # [(1, 5), (5, 5)]
    g.node[5]['foo'] = 'bar'
    print(g.node[5]) # {'foo': 'bar'}
    h = Graph()
    h.add_nodes_from(g)
    print(h.graph) # {}
    print(h.nodes()) # [1, 5, 6]
    print(h.edges()) # {}
    print(h.node[5]) # {}


def create_graph_from_edges():
    '''
    - Don't use this strategy alone to copy a graph
    - None of the arbitrary attributes from nodes, edges, or the graph are copied
    - When a new graph is created from the edges of an existing graph, the nodes that form each edge are also created
        - Thus, creating a copy from edges is almost a true copy
            - It is NOT a true copy because any nodes without edges are not copied!
    '''
    g = Graph([(1, 5), (5, 5)])
    g.add_node(6)
    g.edge[1][5]['foo'] = 'bar'
    print(g.edge[1][5]) # {'foo': 'bar'}
    print(g.nodes()) # [1, 5, 6]
    h = Graph()
    # Yes, this is the required syntax to do this
    h.add_edges_from(g.edges())
    print(h.edge[1][5]) # {}
    print(h.nodes()) # [1, 5]
    print(h.edges()) # [(1, 5), (5, 5)]


def create_true_graph_copy():
    '''
    - <Graph>.copy() returns a true copy of the original graph
        - == operator for graph objects is useless, or perhaps __eq__ isn't implemented so it falls back to "is" behavior
    - This is NOT what I want if I don't want to copy attributes
    '''
    g = Graph([(1, 5), (5, 5)])
    g.add_node(6)
    g.graph['pie'] = 'apple'
    g.node[1]['pet'] = 'fish'
    g.edge[5][5]['sound'] = 'clink'
    h = g.copy()
    print(h.nodes()) # [1, 5, 6]
    print(h.edges()) # [(1, 5), (5, 5)]
    print(h.graph) # {'pie': 'apple'}
    print(h.node) # {1: {'pet': 'fish'}, 5: {}, 6: {}}
    print(h.edge) # {1: {5: {}}, 5: {1: {}, 5: {'sound': 'clink'}}, 6: {}}
    print(h is g) # False
    print(h == g) # False


if __name__ == '__main__':
    #create_empty_graph()
    create_graph_with_new_data()
    create_graph_from_graph()
    #bad_create_graph()
    #create_graph_from_nodes()
    #create_graph_from_edges()
    #create_true_graph_copy()
