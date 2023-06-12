from kol2testy import runtests
# Kamil Kawula
# Algorytm szukający MST to algorytm Kruskala
# Algorytm znajduje kolejne najmniejsze drzewa i sprawdza czy jest piękne, w rzeczywistości szuka tylko pięknych drzew,
# aby drzewo było piękne czyli aby zachodził warunek z m i M, krawędzie tworzące piękne drzewo muszą być swoimi sąsiadami w tablicy,
# wszystkie krawędzie muszą lezec obok siebie, wtedy zostaje spelniony warunek, aby drzewo bylo piekne
# , algorytm przestaje szukac drzewa, gdy kolejna krawedz nie bedzie tworzyla drzewa. I zaczyna szukanie od kolejnej najmniejszej krawedzi
#  O(VElog*E)

def edges(G):
    E = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                E.append((i, G[i][j][0] ,G[i][j][1]))
    return E

def dfs(G):
    n = len(G)
    visited = [False for _ in range(n)]
    time = 0
    def DFSVisit(G, u):
        nonlocal time
        time += 1

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                DFSVisit(G, v)

    visited[0] = True
    DFSVisit(G, 0)

    return True if time == n else False


def beautree(G):
    n = len(G)
    E = edges(G)
    E = sorted(E, key= lambda x : x[2])
    GG = [[] for _ in range(n)]
    weight = 0
    # fast but slow
    # for j in range(len(E) - n + 1):
    #     for i in range(j, j + n - 1):
    #         u, v, w = E[i]
    #         weight += w
    #         GG[u].append(v)
    #         GG[v].append(u)
    #     if dfs(GG):
    #         return weight
    #     GG.clear()
    #     GG = [[] for _ in range(n)]
    #     weight = 0


    # fast fast 
    for i in range(n - 1):
        u, v, w = E[i]
        weight += w
        GG[u].append(v)
        GG[v].append(u)


    for i in range(n - 1, len(E)):
        if dfs(GG):
            return weight
        u, v, w = E[i - n + 1]
        weight -= w
        GG[u].remove(v)
        GG[v].remove(u)

        u, v, w = E[i]
        weight += w
        GG[u].append(v)
        GG[v].append(u)

    if dfs(GG):
        return weight
    
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )