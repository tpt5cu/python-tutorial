# https://networkx.github.io/documentation/stable/reference/classes/graph.html


from networkx.classes.graph import Graph


def add_node_():
    g = Graph()
    attributes = {'foo': 'bar'}
    # Wrong in v2.4
    #g.add_node('9', attr_dict=attributes)
    # Right in v2.4
    g.add_node('9', **attributes)
    print(g.nodes(data=True)) # [('9', {'foo': 'bar'})]


def get_nodes():
    '''
    <Graph>.nodes AND <Graph>.nodes() return the SAME NodeView of the nodes in the graph
    - A NodeView is read-only because 1) it does not support item assignment (no new items and no changing existing items) and 2) it does not support
      item deletion
    - A NodeView is a dict-like object that itself holds normal Python dicts
        - The normal Python dicts are mutable (of course)
    - I prefer <Graph>.nodes instead of <Graph>.nodes() because the NodeView object is an attribute of the Graph. Nothing is "happening," so it's not
      really a method. If the API were <Graph>.get_nodes(), the method syntax would be preferrable
    '''
    g = Graph([(1, 5), (5, 5)])
    # Approach 1
    print(type(g.nodes)) # <class 'networkx.classes.reportviews.NodeView'>
    print(type(g.nodes[5])) # <class 'dict'>
    g.nodes[5]['foo'] = 'bar'
    print(g.nodes[5]) # {'foo': 'bar'}
    # Approach 2
    print(type(g.nodes())) # <class 'networkx.classes.reportviews.NodeView'>
    g.nodes()[5]['baz'] = 'boo'
    print(g.nodes[5]) # {'foo': 'bar', 'baz': 'boo'}
    # NodeView itself is read-only
    #g.nodes[6] = 'foo' # TypeError: 'NodeView' object does not support item assignment
    #del g.nodes[5] # TypeError: 'NodeView' object doesn't support item deletion
    # NodeView contains regular Python dicts
    print(type(g.nodes[5])) # <class 'dict'>


def get_nodes_and_data():
    '''
    <Graph>.nodes() is completely different in v2.4
    - The "data" kwarg can do three things:
        - If data==True, return all node keys and all their data
        - If data==False, return just a list of node keys
        - If data==<attribute key>, return all node keys with the attribute key, along with the value of the attribute
    - In combination with "data", the "default" kwarg will substitute <value> for every node that doesn't have the searched-for attribute key
    '''
    g = Graph()
    g.add_nodes_from(['a', 'b'], data='quack', size='tiny')
    g.add_node('c', data=False)
    g.add_node('d')
    print(g.nodes()) # ['a', 'b', 'c', 'd']
    # Get no node attribute values
    print(g.nodes(data=False)) # ['a', 'b', 'c', 'd']
    # Get all node attribute key-value pairs
    print(g.nodes(data=True)) # [('a', {'data': 'quack', 'size': 'tiny'}), ('b', {'data': 'quack', 'size': 'tiny'}), ('c', {'data': False}), ('d', {})]
    # Get all node keys and attribute values for the given attribute key
    print(g.nodes(data='size')) # [('a', 'tiny'), ('b', 'tiny'), ('c', None), ('d', None)]
    # Substitute a value for nodes that don't have the key
    print(g.nodes(data='size', default='purple')) # [('a', 'tiny'), ('b', 'tiny'), ('c', 'purple'), ('d', 'purple')]
    # It does not appear possible to search for multiple keys at the same time. I should get all data (data==True), then filter somehow
    #print(g.nodes(data=('size', 'data')))
    

def add_edge_():
    '''
    - <Graph>.edge[<u>][<v>] no longer exists, so use <Graph>.edges[<u>, <v>]
    - Unlike v1.11 which accepted a dict as a third argument, only additionals kwargs are accepted after <u> and <v>
    - The rules for arbitrary attributes are the same as v1.11 (see notes below)
    '''
    g = Graph([(1, 5), (5, 5)])
    g.edges[1, 5]['foo'] = 'bar'
    #g.add_edge(1, 5, {}) # TypeError
    # This is wrong. Don't do this!
    #g.add_edge(1, 5, attr_dict={})
    #print(g.edges[1, 5]) # {'foo': 'bar', 'attr_dict': {}}
    # A duplciate edge cannot remove existing arbitrary edge attributes
    g.add_edge(1, 5)
    print(g.edges[1, 5]) # {'foo': 'bar'}
    # A duplicate edge can overwrite existing arbitrary edge attributes
    #g.add_edge(1, 5, foo='fru')
    #print(g.edges[1, 5]) # {'foo': 'fru'}
    # A duplicate edge can add new arbitrary edge attributes
    #g.add_edge(1, 5, new='whoo')
    #print(g.edges[1, 5]) # {'foo': 'bar', 'new': 'whoo'}
    #g.add_edge(4, 6)
    #print(g.nodes) # [1, 5, 4, 6]
    #print(g.edges) # [(1, 5), (5, 5), (4, 6)]


def get_edges():
    '''
    <Graph>.edges AND <Graph>.edges() return the SAME EdgeView of the edges in the graph
    - An EdgeView is a strange data structure
        - It require a tuple index to access
            - What's really going on? Just look at the library code. It's simple really
        - At each tuple index, it stores a Python dict
        - This syntax makes more sense than the v1.11 syntax
    - Edges are stored as 2-tuples (which are immutable)
    - 
    '''
    g = Graph([(1, 5), [5, 5]])
    print(type(g.edges)) # <class 'networkx.classes.reportviews.EdgeView'>
    print(type(g.edges())) # <class 'networkx.classes.reportviews.EdgeView'>
    print(g.edges()) # [(1, 5), (5, 5)]
    # Invalid syntax
    #print(g.edges[1]) # TypeError: 'int' object is not iterable
    # Missing keys
    #print(g.edges[0, 1]) # KeyError: 1
    #print(g.edges[1, 2]) # KeyError: 2
    # Correct syntax
    print(type(g.edges[1, 5])) # <class 'dict'>
    print(g.edges[1, 5]) # {}
    # I can view the 2-tuples but can't modify them
    for e in g.edges():
        pass


def get_neighbors():
    '''
    Unlike v1.11, <Graph>.neighbors(<v>) returns an iterator over the keys of nodes that are neighbors of <v>, as opposed to a list
    - Iterating over the dict_keyiterators returns the keys of neighboring nodes
    '''
    g = Graph([(1, 2), (2, 3)])
    n = g.neighbors(2)
    print(type(n)) # <class 'dict_keyiterator'>
    print(n) # <dict_keyiterator object at 0x1030d9228>
    for x in n:
        print(x) # 1\n3



if __name__ == '__main__':
    add_node_()
    #get_nodes()
    #get_nodes_and_data()
    #add_edge_()
    #get_edges()
    #get_neighbors()
