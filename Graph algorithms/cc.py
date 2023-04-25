#connected components

G = [[1, 4], [0, 2], [1, 3, 5], [2, 4, 6], [0, 3, 5], [2, 4], [3], []]
#G = [[3, 4, 5, 6], [3, 4, 5, 6], [4, 5, 6], [0, 1], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
G = [[], [], [], [], [], [], []]
def cc(G):
    n = len(G)
    component = [-1 for v in range(n)]
    curr_comp = 0

    def DFSVisit(G, v):
        nonlocal curr_comp
        component[v] = curr_comp
        
        for u in G[v]:
            if component[u] == -1:
                component[u] = curr_comp
                DFSVisit(G, u)
    
    for v in range(n):
        if component[v] == -1:
            curr_comp += 1
            DFSVisit(G, v)

    return curr_comp

print(cc(G))

