# https://networkx.github.io/documentation/stable/reference/classes/digraph.html


from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph


def create_graph_with_new_data():
    '''
    A DiGraph object holds directed edges
    - Parallel edges still aren't allowed
        - For a Digraph, two edges are parallel if they connect the same ordered pair of vertices
            - Thus, two edges that connect the same vertices but go in different directions are not parallel
    '''
    # Create with edge list
    g = DiGraph([(1, 5), (5, 1)]) 
    #g = Graph([(1, 5), (5, 1)]) 
    g.add_node(6)
    print(g.nodes()) # [1, 5, 6]
    # These are two distinct edges
    print(g.edges()) # [(1, 5), (5, 1)]
    print(g.neighbors(1)) # [5]
    print(g.neighbors(5)) # [1]
    g.edge[1][5]['foo'] = 'bar'
    print(g.edge[1][5]) # {'foo': 'bar'}
    print(g.edge[5][1]) # {}


if __name__ == '__main__':
    create_graph_with_new_data()