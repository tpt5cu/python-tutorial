# https://networkx.github.io/documentation/networkx-1.11/reference/classes.graph.html


from networkx.classes.graph import Graph


def examine_node_attribute():
    '''
    <Graph> objects don't have a "node" attribute, so why do instances of <Graph> objects have such an attribute?
    '''
    g = Graph([(1, 'foo'), (1, 3)])
    # <Graph>.node is a Python dict
    n = g.node.get('foo')
    print(n)


if __name__ == '__main__':
    examine_node_attribute()