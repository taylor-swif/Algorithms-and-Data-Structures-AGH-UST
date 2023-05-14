# algorithm return logaical value, if grap has cycle returns true and false if hasn't

# the grap is given as an adjacency list

def find_cycle(G):
    n = len(G)
    low = [-1 for v in range(n)]
    time_arr = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
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
                DFSVisit(G,v)
                low[s] = min(low[s], low[v])
            elif v != parent[s]:
                low[s] = min(low[s], time_arr[v])
    DFSVisit(G, 0)
    
    print(low)

G = [[1, 2], [0, 4], [0, 3, 4], [2], [1, 2, 5], [4, 6, 7], [5, 7], [5, 6]]

find_cycle(G)

    
    

