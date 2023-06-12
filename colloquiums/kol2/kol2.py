from kol2testy import runtests
# Kamil Kawula
# Algorytm szukający MST to algorytm Kruskala
# Algorytm znajduje kolejne najmniejsze drzewa i sprawdza czy jest piękne, w rzeczywistości szuka tylko pięknych drzew,
# aby drzewo było piękne czyli aby zachodził warunek z m i M, krawędzie tworzące piękne drzewo muszą być swoimi sąsiadami w tablicy,
# wszystkie krawędzie muszą lezec obok siebie, wtedy zostaje spelniony warunek, aby drzewo bylo piekne
# , algorytm przestaje szukac drzewa, gdy kolejna krawedz nie bedzie tworzyla drzewa. I zaczyna szukanie od kolejnej najmniejszej krawedzi
#  O(VElog*E)

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
                E.append((i, G[i][j][0] ,G[i][j][1]))
    return E

def beautree(G):
    n = len(G)
    E = edges(G)
    E = sorted(E, key= lambda x : x[2])
    V = []
    weight = 0
    length = 0
    for i in range(n):
        V.append(Node(i))

    i = 0
    start = 0
    while i < len(E):
        if length == n - 1:
            return weight
        
        u, v, w = E[i]
        if find(V[v]) != find(V[u]):
            weight += w
            length += 1
            union(V[u], V[v])
            i += 1
        else:
            if start > len(E) - n + 1:
                return None
            weight = 0
            length = 0
            i = start + 1
            start += 1
            V.clear()
            for j in range(len(G)):
                V.append(Node(j))

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )