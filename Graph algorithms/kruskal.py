class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value

def find(v):
    if v.parent != v:
        v.parent = find(v.parent)
    return v.parent
    
def union(u, v):
    u = find(u)
    v = find(v)

    if v.rank > u.rank:
        u.parent = v
    else:
        v.parent = u
        if v.rank == u.rank:
            v.rank += 1

def edges(G):
    E = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
            # if ((G[i][j][0], i ,G[i][j][2])) not in E:
                E.append(i, (G[i][j][0] ,G[i][j][2]))
    return E

def kruskal(G):
    E = edges(G)
    E = sorted(E,key= lambda x : x[2])
    V = []
    MST = []
    for i in range(len(G)):
        V.append(Node(i))

    for u, v, w in E:
        if find(V[v]) != find(V[u]):
            MST.append((u, v, w))
            union(V[u], V[v])

    return MST