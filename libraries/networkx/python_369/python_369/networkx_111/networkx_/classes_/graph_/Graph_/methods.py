# https://networkx.github.io/documentation/networkx-1.11/reference/classes.graph.html


from networkx.classes.graph import Graph


def modify_nodes():
    '''
    The list returned by <Graph>.nodes() is an entirely new list, so modifying it has no effect on the Graph object
    '''
    g = Graph([(1, 'foo'), (1, 3)])
    nodes = g.nodes()
    g.nodes()[0] = 5
    print(g.nodes()) # [1, 'foo', 3]


def node():
    '''
    The <Graph>.node attribute ...
    '''
    g = Graph([(1, 'foo'), (1, 3)])
    n = g.node.get('foo')
    print(type(n)) # <class 'dict'>
    print(n) # {}


if __name__ == '__main__':
    #modify_nodes()
    get_node()
