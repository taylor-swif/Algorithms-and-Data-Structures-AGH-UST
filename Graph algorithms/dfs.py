# Depth-first Search
# ith vertex = T[i] starting form 0
# adjacent nodes are stored in T[] list

G = [[1, 4], [0, 2], [1, 3, 5], [2, 4, 6], [0, 3, 5], [2, 4], [3, 7], [6]]

def DFS(G):
    n = len(G)
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    time_arr = [-1 for v in range(n)]


    def DFSVisit(G, u):
        nonlocal time 
        time += 1
        visited[u] = True
        time_arr[u] = time

        for v in G[u]: 
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)
        time += 1
    time = 0
    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v)
    print(visited)
    print(parent)
    print(time_arr)

DFS(G)