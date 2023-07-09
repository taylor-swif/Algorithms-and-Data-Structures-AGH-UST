# bellman-ford algorithm

E = [(0, 1, 2), (0, 3, 8), (1, 3, 5), (1, 4, 6), (3, 4, 3), (3, 5, 2), (4, 5, 1), (2, 4, 9), (2, 5, 3)]

E=[(0, 1, 3),(0, 3, 3),(0, 4, 2), (1, 2, -7), (2, 3, 8), (3, 1, -1),(3, 4, -2)]
def bellman_ford(E, n, s): #edges

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

def bellman_ford_adjacency(G, s):
    n =len(G)
    dist = [float('inf') for _ in range(n)]
    dist[s] = 0

    for i in range(n):
        for v in range(n):
            for u, w in G[v]:
                if dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w

    for i in range(n):
        for v in range(n):
            for u, w in G[v]:
                if dist[u] > dist[v] + w:
                    dist[u] = float('-inf')

    return dist

E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
G = [[(1, 5)], [(0, 5), (6, 60), (5, 30), (2, 20)], [(1, 20), (3, 10), (3, -15), (4, 75)], [(2, 10), (2, -15)], [(2, 75), (9, 100), (5, 25)], [(6, 5), (1, 30), (8, 50), (4, 25)], [(1, 60), (7, -50), (5, 5)], [(6, -50), (8, -10)], [(7, -10), (5, 50)], [(4, 100)]]
    
# bellman_ford(E, 5, 0)
print(bellman_ford_adjacency(G, 0))
