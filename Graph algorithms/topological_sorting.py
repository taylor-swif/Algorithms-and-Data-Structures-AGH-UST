# Topological sorting, sorting for directed acyclic graph
# It is a linear ordering of its vertices that for every vertex you can only go right
# Based on DFS
G = [[1,2], [2, 3], [], [4, 5], [], [], [3]]

def top_sort(G):
    n = len(G)
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    sort = []
    
    def DFSVisit(G, u):

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)
        sort.append(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    print(sort[::-1])

top_sort(G)