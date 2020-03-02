# https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0


from networkx.classes.graph import Graph
from networkx.classes import function


'''
This module contains functions that provide a "functional" interface to graph methods and assorted utilities
'''


def get_node_attributes_():
    '''
    get_node_attributes(<Graph>, <attribute key>) returns a dict 
    - The <attribute key> can be anything that could be a key (i.e. any immutable object), but in most cases it will be a string. Multiple keys cannot
      be specified
    - The returned dict's keys are node identifiers who have the desired attribute key
    '''
    g = Graph([(1, 5), (5, 5)])
    g.node[5]['foo'] = 'bar'
    g.node[1]['foo'] = 'boo'
    # Works as expected
    #d = function.get_node_attributes(g, 'foo')
    #print(type(d)) # <class 'dict'>
    #print(len(d)) # 2
    #print(d) # {1: 'boo', 5: 'bar'}
    # Does not work. There is no object with the literal attribute key ('foo', 'hi')
    g.node[1]['hi'] = 'bye'
    d = function.get_node_attributes(g, ('foo', 'hi'))
    print(d) # {}
    g.node[1][('foo', 'hi')] = 'lmao'
    print(function.get_node_attributes(g, ('foo', 'hi'))) # {1: 'lmao'}


def get_edge_attributes_():
    g = Graph([(1, 5), (5, 5)])
    g.edge[5][1]['foo'] = 'bar'
    print(function.get_edge_attributes(g, 'foo')) # {(1, 5): 'bar'}


def edges_():
    '''
    edges(<Graph>, [<nbunch>]) returns Python list of edges incident to nodes in nbunch
    - If <nbunch> is not provided or None, return all edges in <Graph>
    '''
    g = Graph([(1, 5), (5, 5)])
    g.add_edge(2, 4)
    g.add_edge(1, 2)
    # 2 is connected to 4 and 1, so return those edges
    print(function.edges(g, 2)) # [(2, 4), (2, 1)]
    # With no <nbunch>, return all edges
    print(function.edges(g)) # [(1, 5), (1, 2), (5, 5), (2, 4)]


def neighbors_():
    '''Functional equivalent to <Graph>.neighbors(<v>)'''
    g = Graph([(1, 2), (2, 3)])
    print(function.neighbors(g, 2)) # [1, 3]


if __name__ == '__main__':
    #get_node_attributes_()
    #get_edge_attributes_()
    #edges_()
    neighbors_()
