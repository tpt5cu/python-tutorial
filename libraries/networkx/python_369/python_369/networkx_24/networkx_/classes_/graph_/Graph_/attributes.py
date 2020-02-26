# https://networkx.github.io/documentation/stable/reference/classes/graph.html


from networkx.classes.graph import Graph


def examine_node_attributes():
    '''
    The v2.4 API is slightly different because it uses <Graph>.nodes (or <Graph>.nodes()) while <Graph>.node doesn't exist
    - Even though the NodeView is new, the underlying Python dicts that store attributes are the same as v1.11
    '''
    g = Graph([(1, 5), (5, 5)])
    g.add_node(5)
    print(g.nodes()) # [1, 5]
    print(g.edges()) # [(1, 5), (5, 5)]
    #print(g.node[5]) # AttributeError: 'Graph' object has no attribute 'node'
    print(g.nodes[5]) # {}
    g.nodes[5]['foo'] = 'bar'
    print(g.nodes[5]) # {'foo': 'bar'}


def examine_edge_attributes():
    pass


if __name__ == '__main__':
    examine_node_attributes()
