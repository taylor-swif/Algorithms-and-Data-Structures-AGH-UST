import heapq
from queue import PriorityQueue
# (v1, v2, weight) v1 < v2
E = [(0, 1, 2), (0, 3, 8), (1, 3, 5), (1, 4, 6), (3, 4, 3), (3, 5, 2), (4, 5, 1), (2, 4, 9), (2, 5, 3)]

def Djikstra(E, n, s):
    G =[[] for _ in range(n)]

    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
        
    dist = [float('inf') for v in range(n)]
    prev = [None for v in range(n)]
    dist[s] = 0

    pq = []
    heapq.heappush(pq, (0, s))

    done = [False for v in range(n)]
    done[s] = True

    while pq:
        weight_u, u = heapq.heappop(pq)
        
        for v, weight in G[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
        done[u] = True



    print(dist)
    print(prev)

def djiksstra(G, s, t):
    n = len(G)
    dist = [float('inf') for _ in range(n)]
    prev = [None for _ in range(n)]
    done = [False for _ in range(n)]
    dist[s] = 0
    done[s] = True
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        w, v = Q.get()

        for u, w_u in G[v]:
            if not done[u] and dist[u] > w_u + dist[v]:
                dist[u] = w_u + dist[v]
                prev[u] = v
                Q.put((dist[u], u))
        done[v] = True
        if done[t]:
            return dist[t]
    print(dist)
    return dist[t]

graph = [[(1, 1), (2, 12)],
         [(0, 1), (2, 7), (3, 5)],
         [(0, 12), (1, 2), (3, 6), (4, 2)],
         [(1, 5), (2, 6), (4, 4), (5, 100)],
         [(2, 2), (3, 4), (5, 9)],
         [(3, 100), (4, 9)]]
for i in range(len(graph)):
    print(djiksstra(graph, 0, i))
