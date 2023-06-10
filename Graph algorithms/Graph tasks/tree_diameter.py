
def DFS(G, s):
    n = len(G)
    visited = [False for v in range(n)]
    time_arr = [0 for v in range(n)]

    def DFSVisit(G, u):
        visited[u] = True

        for v in G[u]: 
            if not visited[v]:
                time_arr[v] = time_arr[u] + 1
                DFSVisit(G, v)

    DFSVisit(G, s)
    return time_arr

def make_adjacency_list(E):
    max_index = 0
    for u, v in E:
        max_index = max(max_index, u, v)
    G = [[] for _ in range(max_index + 1)]

    for u, v in E:
        G[u].append(v)
        G[v].append(u)

    return G

def diamter(E):
    G = make_adjacency_list(E)
    max_time = 0
    time_arr = DFS(G, 0)
    for i in range(len(time_arr)):
        if time_arr[max_time] < time_arr[i]:
            max_time = i
    
    time_arr = DFS(G, max_time)

    for i in range(len(time_arr)):
        if time_arr[max_time] < time_arr[i]:
            max_time = i

    return time_arr[max_time]


E = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [5, 10], [7, 11],
         [7, 12], [7, 13], [8, 14], [8, 15], [11, 16], [11, 17], [13, 18], [16, 19], [19, 20]]

print(diamter(E))