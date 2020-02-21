from networkx.classes.graph import Graph


def modify_nodes():
    '''
    A NodeView (thankfully) cannot modify the underlying list of nodes
    - It's just like a dictview in that regard
    '''
    g = Graph([(1, 'foo'), (1, 3)])
    nodes = g.nodes()
    #g.nodes()[0] = 5 # TypeError: 'NodeView' does not support item assignment


if __name__ == '__main__':
    modify_nodes()