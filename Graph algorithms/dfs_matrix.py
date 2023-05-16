# depth first search

def dfs(G, s):
    n = len(G)
    parent = [None for v in range(n)]
    visited = [False for v in range(n)]
    time_arr = [-1 for v in range(n)]
    time = 0

    def DFSVisit(G, s):
        nonlocal time
        visited[s] = True
        time_arr[s] = time
        time += 1

        for i in range(len(G)):
            if not visited[i] and G[s][i] == 1:
                parent[i] = s
                DFSVisit(G, i)

    DFSVisit(G, s)
    print(parent)
    print(visited)
    print(time_arr)


G = [[0, 1, 1, 1, 0], 
     [1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 1], 
     [0, 0, 0, 1, 0]]
dfs(G, 0)