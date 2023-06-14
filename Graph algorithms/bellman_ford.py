# bellman-ford algorithm

E = [(0, 1, 2), (0, 3, 8), (1, 3, 5), (1, 4, 6), (3, 4, 3), (3, 5, 2), (4, 5, 1), (2, 4, 9), (2, 5, 3)]

E=[(0, 1,3),(0, 3,3),(0, 4,2), (1, 2,-7), (2, 3,8), (3, 1,-1),(3, 4,-2)]
def bellman_ford(E, n, s):

    d = [float('inf') for v in range(n)]
    parent = [None for v in range(n)]
    d[s] = 0

    for i in range(n - 1):
        for u, v, w in E:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parent[v] = u
    for u, v, w in E:
        if d[v] > d[u] + w:
            return False
    print(d)
    return True

    
bellman_ford(E, 5, 0)

