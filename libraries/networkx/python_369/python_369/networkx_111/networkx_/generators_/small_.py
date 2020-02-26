import networkx as nx


'''NetworkX makes it easy to generate common graphs'''


def create_bull_graph():
    '''
    In the mathematical field of graph theory, the bull graph is a planar undirected graph with 5 vertices and 5 edges, in the form of a triangle with
    two disjoint pendant edges. It has chromatic number 3, chromatic index 3, radius 2, diameter 3 and girth 3.
    '''
    g = nx.generators.small.bull_graph()
    print(g) # Bull Graph
    print(g.graph) # {'name': 'Bull Graph'}
    print(g.nodes()) # [0, 1, 2, 3, 4]
    print(g.edges()) # [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4)]


if __name__ == '__main__':
    create_bull_graph()
