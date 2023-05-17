from queue import PriorityQueue

def prim(G, s):
    n = len(G)
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    weight = [float('inf') for v in range(n)]
    Q = PriorityQueue()
    
    visited[s] = True
    Q.put((0, s))
    weight[s] = 0
   
    while not Q.empty():
        _, v = Q.get()
        visited[v] = True
        for (u, w) in G[v]:
            if weight[u] > w and not visited[u]:
                parent[u] = v
                weight[u] = w
                Q.put((weight[u], u))
    print(parent)
        


G = [[(1, 1), (3, 5), (5, 8)], [(0, 1), (2, 3)], [(1, 3), (3, 4), (4, 6)], [(0,5), (4, 2), (2, 4), (5, 7)], [(3, 2), (2, 6)], [(0, 8), (3, 7)]]
prim(G, 2)