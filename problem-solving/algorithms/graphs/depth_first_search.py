# "Algorithms" 4th edition, Robert Sedgewick, page 530


import graph


def recursive_dfs(g, start, visited=None):
    # type (Graph, int) -> None
    if visited is None:
        visited = []
    print('visited {}'.format(start))
    visited.append(start)
    for v in g.adjacent[start]:
        if v not in visited:
            recursive_dfs(g, v, visited)


def test_recursive_dfs():
    g = graph.get_simple_graph()
    print(g)
    recursive_dfs(g, 0, [])
    print('')
    recursive_dfs(g, 9, [])


if __name__ == '__main__':
    test_recursive_dfs()