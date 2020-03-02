# https://networkx.github.io/documentation/networkx-1.11/reference/classes.graph.html


from networkx.classes.graph import Graph


def add_node():
    '''
    - Adding a duplicate node does not add another node to the graph
        - Nodes must be unique. I cannot add two different nodes with the same value
            - Use the ability to add arbitrary attributes to nodes in order to make multiple nodes have the same "value"
                - From a technical standpoint, there is no reason why I can't have two nodes that are identified by the number 5. However, from a
                    traveral perspective, it makes sense to require that nodes be unique. If I had two nodes whose primary identifier was 5, how would
                    the code know which node I was interested in when I looked up 5? 
                    - What's annoying about this is that since nodes must be unique, then there's no reason why I can't look them up by key!
                        - This restriction must be due to performance?
                            - But this can't be! There IS already a dictionary that contains a reference to every node! It's <Graph>.node! So it's
                              just poor design
    - Adding a duplicate node can update the aribtrary node attribute dict (see below)
    - A node can be added along with attributes
    '''
    g = Graph([(1, 5), (5, 5)])
    g.node[5]['foo'] = 'bar'
    # A duplicate node cannot remove existing arbitrary node attributes
    #g.add_node(5, {})
    #print(g.node[5]) # {'foo': 'bar'}
    # A duplicate node can overwrite existing arbitrary node attributes
    #g.add_node(5, foo='bleh')
    #print(g.node[5]) # {'foo': 'bleh'}
    # A duplicate node can add new arbitrary node attributes
    #g.add_node(5, bless='you')
    #print(g.node[5]) # {'foo': 'bar', 'bless': 'you'}
    print(g.nodes()) # [1, 5]
    g.add_node(6, size='big', sound='quack')
    print(g.node[6]) # {'size': 'big', 'sound': 'quack'}


def add_nodes():
    '''Multiple nodes can be added at the same time from any container'''
    g = Graph([(1, 5), (5, 5)])
    # If a kwarg is included, every added node will get the kwarg as an attribute
    g.add_nodes_from(['a', 'b'], price='$10')
    print(g.nodes()) # [1, 5, 'a', 'b']
    print(g.node['a']) # {'price': '$10'}
    print(g.node['b']) # {'price': '$10'}
    # A dictionary can be used as a source of nodes, but the dict values are not incorporated into the graph
    g.add_nodes_from({'greeting': 'aloha'}) 
    print(g.nodes()) # [1, 5, 'a', 'b', 'greeting']
    print(g.node['greeting']) # {}


def get_node():
    '''
    - Remember that in v1.11:
        - <Graph>.nodes is a function that returns a list
        - <Graph>.node returns a dict that contains <node key>-<dict> pairs
    '''
    g = Graph([(1, 5), (5, 5)])
    print(type(g.nodes.get(1))) # AttributeError: 'function' object has no attribute 'get'
    #print(g.nodes.get(1))
    #print(type(g.nodes.get(2)))
    #print(g.nodes.get(2))


def get_nodes():
    '''
    <Graph>.nodes() returns a new list that contains the unique identifiers that represent nodes in the graph
    - Modifying this list does nothing to the original graph
    - I can only access nodes by index, not key
    '''
    g = Graph([(1, 5), (5, 5)])
    g.add_node(5)
    print(type(g.nodes())) # <class 'list'>
    print(g.nodes()) # [1, 5]
    print(g.nodes()[0]) # 1
    g.nodes().append(6)
    print(g.nodes()) # [1, 5]


def add_edge():
    '''
    - Adding an edge with nonexistent nodes creates those nodes
    - Adding a duplicate edge can update the arbitrary attribute data for that edge (see below)
        - The rules for updating arbitrary attributes are the same as those for adding a duplicate node
    '''
    g = Graph([(1, 5), (5, 5)])
    g.edge[1][5]['foo'] = 'bar'
    # A duplciate edge cannot remove existing arbitrary edge attributes.
    # - Also, {} and attr_dict={} are equivalent
    #g.add_edge(1, 5, attr_dict={})
    #g.add_edge(1, 5, {})
    #print(g.edge[1][5]) # {'foo': 'bar'}
    # A duplicate edge can overwrite existing arbitrary edge attributes
    #g.add_edge(1, 5, attr_dict={'foo': 'fru'})
    g.add_edge(1, 5, foo='fru')
    print(g.edge[1][5]) # {'foo': 'fru'}
    # A duplicate edge can add new arbitrary edge attributes
    #g.add_edge(1, 5, new='whoo')
    #print(g.edge[1][5]) # {'foo': 'bar', 'new': 'whoo'}
    #g.add_edge(4, 6)
    #print(g.nodes()) # [1, 5, 4, 6]
    #print(g.edges()) # [(1, 5), (5, 5), (4, 6)]


def add_edges():
    '''Including an arbitrary attribute with newly added edges will add that attribute to all of the new edges'''
    g = Graph([(1, 5), (5, 5)])
    g.add_edges_from([[4, 6], (7, 8)], win='yes')
    print(g.nodes()) # [1, 5, 4, 6, 7, 8]
    print(g.edges()) # [(1, 5), (5, 5), (4, 6), (7, 8)]
    print(g.edge) # {1: {5: {}}, 5: {1: {}, 5: {}}, 4: {6: {'win': 'yes'}}, 6: {4: {'win': 'yes'}}, 7: {8: {'win': 'yes'}}, 8: {7: {'win': 'yes'}}}


def get_edges():
    '''<Graph>.edges() returns a Python list of tuples, where each 2-tuple represents an edge between two nodes'''
    g = Graph([(1, 5), (5, 5)])
    #print(type(g.edges())) # <class 'list'>
    #print(g.edges()) # [(1, 5), (5, 5)]
    # Iterate over 2-tuples
    for e in g.edges():
        print(e) # (1, 5)\n(5, 5)


def get_neighbors():
    '''Get a Python list of neighbors connected to <v> via <Graph>.neighbors(<v>)'''
    g = Graph([(1, 2), (2, 3)])
    n = g.neighbors(2)
    print(type(n)) # <class 'list'>
    print(n) # [1, 3]


if __name__ == '__main__':
    #add_node()
    #add_nodes()
    #get_node()
    #get_nodes()
    #add_edge()
    #add_edges()
    #get_edges()
    get_neighbors()
