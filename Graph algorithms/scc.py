# strongly connected components for directed graph

from collections import deque

def reverse_edges(G, G_r):
    n = len(G)
    for i in range(n):
        for j in range(len(G[i])):
            G_r[G[i][j]].append(i)

def scc(G):
    n = len(G)
    visited = [False for v in range(n)]
    #making stack with the highest procesing time on the top
    Q = deque()
    def DFSVisit_Stack(G, s):
        for u in G[s]:
            # print(u)
            if not visited[u]:
                visited[u] = True
                DFSVisit_Stack(G, u)
        Q.append(s)
    
    visited[0] = True 
    DFSVisit_Stack(G, 0)#grap is connected
    
    # going backward
    G_r = [[] for _ in range(len(G))]
    reverse_edges(G, G_r)
    visited = [False for v in range(n)]
    time_arr = [-1 for v in range(n)]
    time = 0

    def DFSVisit(G, s):
        nonlocal time
        time_arr[s] = time
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                DFSVisit(G, u)

    while len(Q) > 0:
        u = Q.pop()
        if not visited[u]:
            DFSVisit(G_r, u)
            time += 1

    print(time_arr) 


# G = [[1, 3], [2], [0, 3], []]
G = [[1], [2], [0, 3, 8], [4, 6], [5], [3], [5], [8], [9], [5, 10], [3, 7]]
scc(G)