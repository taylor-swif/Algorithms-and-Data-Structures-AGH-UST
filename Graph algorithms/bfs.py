# Breadth-first search
# ith vertex = T[i] starting form 0
# adjacent nodes are stored in T[] list
from queue import Queue

G = [[1, 4], [0, 2], [1, 3, 5], [2, 4, 6], [0, 3, 5], [2, 4], [3, 7], [6]]

def BFS(G, s):
    n = len(G)
    Q = Queue(0)
    visited = [False for v in range(n)]
    d = [-1 for v in range(n)]
    parent = [None for v in range(n)]

    visited[s] = True
    parent[s] = None
    d[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                visited[v] = True
                Q.put(v)
    print(visited)
    print(parent)
    print(d)

BFS(G, 0)
