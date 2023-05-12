# bellman-ford algorithm

E = [(0, 1, 2), (0, 3, 8), (1, 3, 5), (1, 4, 6), (3, 4, 3), (3, 5, 2), (4, 5, 1), (2, 4, 9), (2, 5, 3)]


def bellman_ford(E, n, s):

    d = [float('inf') for v in range(n)]
    parent = [None for v in range(n)]
    d[s] = 0

    for i in range(n):
        for u, v, w in E:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parent[v] = u

    print(d)
bellman_ford(E, 6, 0)

