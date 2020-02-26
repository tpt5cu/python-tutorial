# https://networkx.github.io/documentation/networkx-1.11/reference/classes.graph.html


from networkx.classes.graph import Graph


def examine_graph_attributes():
    '''A graph can contain arbitrary attributes in its "graph" attribute, which is a Python dict'''
    g = Graph()
    print(type(g.graph)) # <class 'dict'>
    print(g.graph) # {}
    g.graph['foo'] = 'bar'
    print(g.graph) # {'foo': 'bar'}


def examine_node_attributes():
    '''
    A node can contain arbitrary attributes
    - The <Graph>.node attribute is a regular Python dict whose key-value pairs are node identifiers and Python dicts
        - The documentation says that nodes cannot be added to the graph through <Graph>.node, but the code shows they can!
            - However, doing this can mess up the structure of the graph. The newly added node might not have its own Python dict if the update was
              done incorrectly
            - "Warning: adding a node to G.node does not add it to the graph." Listen to the documentation and never try to add nodes via <Graph>.node
    '''
    g = Graph([(1, 5), (5, 5)])
    print(g.nodes()) # [1, 5]
    print(g.edges()) # [(1, 5), (5, 5)]
    print(type(g.node)) # <class 'dict'>
    # Get the dict of an arbitrary node, but not the node itself (annoying)
    print(type(g.node[5])) # <class 'dict'>
    print(g.node[5]) # {}
    g.node[5]['pet'] = 'cat'
    print(g.node[5]) # {'pet': 'cat'}
    ## NEVER DO THIS
    # This is how to mess up the graph
    g.node[6] = 'psych'
    # The node exists, but are there underlying problems I'm not aware of?
    print(g.nodes()) # [1, 5, 6]
    # Here's the first problem. This should be a dict, but it's a str
    print(type(g.node[6])) # <class 'str'>
    # This error occurs because of the abuse of the API
    #g.add_node(6) # AttributeError: 'str' object has no attribute 'update'
    # This is how to "correctly" add a node via <Graph>.node, but never do this
    g.node[6] = {'psych': 'psych'}
    g.add_node(6)
    print(g.nodes()) # [1, 5, 6]


def examine_edge_attributes():
    '''
    <Graph>.edge[<n>] is a Python dict
    - This dict has keys that represent every other node that <n> is connected to
    - The values in the dict are themselves dicts. Each dict is associated with a node, but each dict is NOT the same dict that would be found via
      <Graph>.node
      - Thus, to look up an attribute of the edge between 5 and 5 (self loop), I would use <Graph>.edge[5][5], which is quite natural syntax actually
        - Don't worry. Every edge, regardless of how it was accessed, has exactly one Python dict for attributes
    '''
    g = Graph([(1, 5), (5, 5)])
    print(type(g.edge)) # <class 'dict'>
    print(type(g.edge[5])) # # <class 'dict'>
    g.node[5]['foo'] = 'bar'
    print(g.node[5]) # {'foo': 'bar'}
    # If the node dicts and edge dicts were the same, foo and bar would be shown below
    print(g.edge[5]) # {1: {}, 5: {}}
    g.edge[5][5]['friend'] = 'homie'
    print(g.node[5]) # {'foo': 'bar'}
    print(g.edge[5]) # {1: {}, 5: {'friend': 'homie'}}
    print(g.edge[1][5] is g.edge[5][1]) # True


if __name__ == '__main__':
    #examine_graph_attributes()
    #examine_node_attributes()
    examine_edge_attributes()
