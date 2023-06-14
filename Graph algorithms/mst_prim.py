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
        _, k = Q.get()
        visited[k] = True
        for v, w in G[k]:
            if weight[v] > w and not visited[v]:
                parent[v] = k
                weight[v] = w
                Q.put((weight[v], v))
    print(parent)
        


G = [[(1, 1), (3, 5), (5, 8)], [(0, 1), (2, 3)], [(1, 3), (3, 4), (4, 6)], [(0,5), (4, 2), (2, 4), (5, 7)], [(3, 2), (2, 6)], [(0, 8), (3, 7)]]

n = 6
B = [(0, 1, 1),
     (0, 3, 8),
     (0, 4, 5),
     (1, 2, 3),
     (2, 4, 4),
     (2, 5, 6),
     (3, 4, 7),
     (4, 5, 2)
     ]
def graph(B, n):
    G = [[] for _ in range(n)]

    for kraw in B:
        G[kraw[0]].append([kraw[1], kraw[2]])
        G[kraw[1]].append([kraw[0], kraw[2]])

    return G
G = graph(B, n)
prim(G, 0)