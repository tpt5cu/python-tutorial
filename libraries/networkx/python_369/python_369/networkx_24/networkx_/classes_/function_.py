# https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0


from networkx.classes.graph import Graph
from networkx.classes import function


'''This module contains functions that provide a "functional" interface to graph methods and assorted utilities'''


def get_node_attributes_():
    '''Unchanged from v1.11'''
    g = Graph([(1, 5), (5, 5)])
    g.nodes[5]['foo'] = 'bar'
    g.nodes[1]['foo'] = 'boo'
    # Works as expected
    d = function.get_node_attributes(g, 'foo')
    print(type(d)) # <class 'dict'>
    print(len(d)) # 2
    print(d) # {1: 'boo', 5: 'bar'}
    # Does not work. There is no object with the literal attribute key ('foo', 'hi')
    #g.nodes[1]['hi'] = 'bye'
    #d = function.get_node_attributes(g, ('foo', 'hi'))
    #print(d) # {}
    #g.nodes[1][('foo', 'hi')] = 'lmao'
    #print(function.get_node_attributes(g, ('foo', 'hi'))) # {1: 'lmao'}


def get_edge_attributes_():
    '''Exactly the same as v1.11'''
    g = Graph([(1, 5), (5, 5)])
    g.edges[5, 1]['foo'] = 'bar'
    print(function.get_edge_attributes(g, 'foo')) # {(1, 5): 'bar'}


if __name__ == '__main__':
    #get_node_attributes_()
    get_edge_attributes_()
