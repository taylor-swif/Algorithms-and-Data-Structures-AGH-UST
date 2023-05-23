# undirected connected graph
# bridge is defined as edge that when it is removed makes the graph unconnected 
# output: bridges 
# G = [
#     [0,1,1,0,0,0,0,0], 
#     [1,0,0,0,1,0,0,0], 
#     [1,0,0,1,1,0,0,0], 
#     [0,0,1,0,0,0,0,0], 
#     [0,1,1,0,0,1,0,0],
#     [0,0,0,0,1,0,1,1],
#     [0,0,0,0,0,1,0,1],
#     [0,0,0,0,0,1,1,0]]
# G = [[1, 2], [0, 4], [0, 3, 4], [2], [1, 2, 5], [4, 6, 7], [5, 7], [5, 6]]
# G =  [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
G = [[0,1,1,0,0,0],
     [1,0,1,0,0,0],
     [1,1,0,1,0,1],
     [0,0,1,0,1,0],
     [0,0,0,1,0,1],
     [0,0,1,0,1,0]]

def make_graph(G):
    new_graph = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 1:
                new_graph[i].append(j)
    return new_graph

def bridge(G):
    n = len(G)
    parent = [None for v in range(n)]
    time_arr = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    low = [-1 for v in range(n)]
    time = 0

    def DFSVisit(G, s):
        nonlocal time
        visited[s] = True
        time_arr[s] = time
        low[s] = time
        time += 1

        for v in G[s]:
            if not visited[v]:
                parent[v] = s
                DFSVisit(G, v)
                low[s] = min(low[s], low[v])
            elif v != parent[s]:
                low[s] = min(low[s], time_arr[v])

    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v)
    
    for i in range(n):
        if time_arr[i] == low[i] and parent[i] != None:
            print(parent[i], i)


print(make_graph(G))
# bridge(make_graph(G))
bridge([
    [1, 2],
    [0, 2],
    [0, 1, 6],
    [5, 4],
    [5, 3],
    [3,4,6],
    [2,7,5],
    [6]
    ])