# "Algorithms" 4th edition, Robert Sedgewick, page 526


import os


class Graph(object):

    def __init__(self, v=None, filepath=None):
        # type (int, str) -> None
        self.e = 0 # Number of edges
        if filepath is not None:
            with open(filepath) as f:
                self.v = int(f.readline())
                self.adjacent = [[] for _ in range(self.v)] # Main adjacency list
                for line in f:
                    a, b = [int(x) for x in line.split()]
                    self.add_edge(a, b)
        else:
            self.v = int(v) # Number of vertices
            self.adjacent = [[] for _ in range(self.v)] # Main adjacency list

    def add_edge(self, v, w):
        # type (int, int) -> None
        self.adjacent[v].append(w)
        self.adjacent[w].append(v)
        self.e += 1

    def get_adjacent(self, v):
        # type (int) -> list
        return self.adjacent[v]

    def __repr__(self):
        return ''.join(['{vertex}: {connected}\n'.format(vertex=i, connected=self.adjacent[i]) for i in range(len(self.adjacent))])


def get_simple_graph():
    return Graph(filepath=os.path.join(os.path.dirname(__file__), 'simple_graph.txt'))


if __name__ == '__main__':
    g = Graph(v=10)
    g.add_edge(0, 9)
    print(g)
    g = Graph(filepath=os.path.join(os.path.dirname(__file__), 'simple_graph.txt'))
    print(g)