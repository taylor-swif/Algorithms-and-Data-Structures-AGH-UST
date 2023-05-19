# The edmonds karp algorithm that computes maximum flow

from collections import deque

def bfs(G, s, t):
    n = len(G)
    parent = [None for v in range(n)]
    visited = [False for v in range(n)]
    
    Q = deque()

    Q.append(s)

    while Q:
        v = Q.popleft()

        for i in range(n):
            if G[v][i] != 0 and not visited[i]:
                parent[i] = v
                visited[i] = True
                Q.append(i)
    
    if parent[t] == None:
        return None
    return parent

def Ford(G, s, t):
    max_flow = 0
    parent = bfs(G, s, t)

    while parent:
        curr_flow = float('inf')
        v = t
        
        while v:
            curr_flow = min(curr_flow, G[parent[v]][v])
            v = parent[v]
        
        v = t

        while v:
            G[parent[v]][v] -= curr_flow
            G[v][parent[v]] += curr_flow
            v = parent[v]
        max_flow += curr_flow
        
        parent = bfs(G, s, t)
    
    return max_flow

graph = [[0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
         [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


print(Ford(graph, 0, 9))
# print(bfs(graph, 0, 9))