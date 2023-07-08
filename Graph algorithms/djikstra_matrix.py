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
            if G[u][i] != -1 and not visited[i]:
                if d[i] > d[u] + G[u][i]:
                    d[i] = d[u] + G[u][i]
                    heapq.heappush(heap, (d[i], i))
    return d

def djikstra_better(G, s):
    n = len(G)
    parent = [False for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    dist[s] = 0

    while True:
        min_dist = float('inf')
        min_u = -1

        for u in range(n):
            if not visited[u] and dist[u] < min_dist:
                min_u = u
                min_dist = dist[u]
        if min_u == -1:
            break
        visited[min_u] = True
        u = min_u

        for v in range(n):
            if not visited[v] and G[u][v] != -1 and dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
                parent[v] = u
    
    return dist


G = [[-1, 1, 5, -1, -1],
    [1, -1, 2, 8, 7],
    [5, 2, -1, 3, -1],
    [-1, 8, 3, -1, 1],
    [-1, 7, -1, 1, -1]]
print(djikstra(G, 0, 1))
print(djikstra_better(G, 0))