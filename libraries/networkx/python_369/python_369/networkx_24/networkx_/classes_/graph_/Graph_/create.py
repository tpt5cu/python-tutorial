# https://networkx.github.io/documentation/stable/


from networkx.classes.graph import Graph


def create_graph_from_graph():
    '''Are the results the same as before?'''
    pass


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
    create_graph_from_edgeview()
