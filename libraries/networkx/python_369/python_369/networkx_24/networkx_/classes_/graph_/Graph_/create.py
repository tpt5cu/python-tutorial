# https://networkx.github.io/documentation/stable/


from networkx.classes.graph import Graph


def create_graph_from_nodes():
    '''
    The net result is the same as in v1.11: the new graph gets all new nodes that are copies of the original nodes
    - No edges are copied
    - No arbitrary attributes are copied
    '''
    g = Graph([(1, 5), (5, 5)])
    g.graph['baz'] = 'boo'
    g.add_node(6)
    print(g.nodes()) # [1, 5, 6]
    print(g.edges()) # [(1, 5), (5, 5)]
    g.nodes[5]['foo'] = 'bar'
    print(g.nodes[5]) # {'foo': 'bar'}
    h = Graph()
    h.add_nodes_from(g)
    print(h.graph) # {}
    print(h.nodes()) # [1, 5, 6]
    print(h.edges()) # {}
    print(h.nodes[5]) # {}


def create_graph_from_edgeview():
    '''
    Fortunately, creating a graph from the EdgeView of another graph does not perform a shallow copy of the original graph
    - The new graph gets entirely new edges
        - Arbitrary attributes of the old edges are not copied
    - This approach will miss copying nodes who had no edges
    '''
    g = Graph([(1, 'foo'), (1, 3)])
    g.add_node(4)
    h = Graph(g.edges)
    g.edges[1, 'foo']['key'] = 'value'
    print(h.nodes) # [1, 'foo', 3]
    print(h.edges) # [(1, 'foo'), (1, 3)]
    print(h.edges[1, 'foo']) # {}
    print(g.edges[1, 'foo']) # {'key': 'value'}


if __name__ == '__main__':
    create_graph_from_nodes()
    #create_graph_from_edgeview()
