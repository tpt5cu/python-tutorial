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


def examine_nonexistent_node_attributes():
    '''Results are identical to v1.11. There is no magical nonexistent item handling by a NodeView'''
    g = Graph([(1, 5), (5, 5)])
    g.nodes.get(6, {})['foo'] = 'bar'
    #print(g.nodes[6]) # KeyError
    print(g.nodes) # [1, 5]


def examine_edge_attributes():
    '''
    Although the tuple indexing syntax is new, what's unchanged from v1.11 is that every edge key stores a regular dict
    - As before, edge attributes are distinct from node attributes and undirected graphs can only have one edge between vertices
    '''
    g = Graph([(1, 5), (5, 5)])
    print(type(g.edges[1, 5])) # <class 'dict'>
    print(g.edges[1, 5]) # {}
    g.edges[5, 1]['foo'] = 'bar'
    print(g.nodes[1]) # {}
    print(g.nodes[5]) # {}
    print(g.edges[1, 5]) # {'foo': 'bar'}
    print(g.edges[1, 5] is g.edges[5, 1]) # True
    # The legacy edge attribute access via <Graph>[<u>][<v>] is (confusingly) preserved
    print(g[1][5]) # {'foo': 'bar'}
    #print(g.edges[1][5]) # TypeError
    print(g.edges[1, 5]) # {'foo': 'bar'}
    print(g[1][5] is g.edges[1, 5]) # True


if __name__ == '__main__':
    #examine_node_attributes()
    #examine_nonexistent_node_attributes()
    examine_edge_attributes()
