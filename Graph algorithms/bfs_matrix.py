from collections import deque

def bfs(G, s):
    n = len(G)
    visited = [False for v in range(n)]
    time_arr = [0 for v in range(n)]
    parent = [None for v in range(n)]

    Q = deque() 
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for i in range(n):
            if G[u][i] == 1 and visited[i] == False:
                visited[i] = True
                parent[i] = u
                time_arr[i] = time_arr[parent[i]] + 1
                Q.append(i)
    print(visited)
    print(time_arr)
    print(parent)




    


G = [[0, 1, 1, 1, 0], 
     [1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 1], 
     [0, 0, 0, 1, 0]]
bfs(G, 0)