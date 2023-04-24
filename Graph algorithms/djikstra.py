import heapq
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
        
        for (v, weight) in G[u]:
            if(dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
        done[u] = True


    print(dist)
    print(prev)

Djikstra(E, 6, 0)
