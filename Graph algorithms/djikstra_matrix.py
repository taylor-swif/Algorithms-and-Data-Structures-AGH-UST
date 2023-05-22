import heapq

def djikstra(G, s, t):
    n = len(G)
    d = [float('inf') for v in range(n)]
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]

    heap = []
    heapq.heappush(heap, (0, s))
    d[s] = 0
    visited[s] = True

    while heap:
        w_u, u = heapq.heappop(heap)

        for i in range(n):
            if G[u][i] != 0 and not visited[i]:
                if d[i] > d[u] + G[u][i]:
                    d[i] = d[u] + G[u][i]
                    heapq.heappush(heap, (d[i], i))
    return d

G = [[0, 1, 5, 0, 0],
         [1, 0, 2, 8, 7],
         [5, 2, 0, 3, 0],
         [0, 8, 3, 0, 1],
         [0, 7, 0, 1, 0]]
print(djikstra(G, 0, 1))