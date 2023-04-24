from queue import Queue

#1 sprawdzanie czy graf jestr dwudzielny BFS
def is_biparie(G, s):
    n = len(G)
    Q = Queue(0)
    color = [-1 for v in range(n)]

    Q.put(s)
    color[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if color[v] == -1:
                color[v] = (color[u] + 1)%2
                Q.put(v)
            else:
                if color[v] == color[u]:
                    return False
    return True
# 2 liczba spojnych skladowych w grafie DFS
# strongly connected components
def scc(G):
    vis = [0]*len(G)
    def DFS(v):
            vis[v] = 1
            for x in G[v]:
                if vis[x]: continue
                DFS(x)
    l = 0
    for i in range(len(G)):
        if not vis[i]:
            l += 1
            DFS(i)
    return l

# 3 stacje nadwacze odłączanie
#TODO
# 4 dany jest graf G jako macierz sąsiedztwa, czy w tym grafie istnieje cykl długosci 4, składajaący się dokładnie z 4 wierzchłów?

# O(n^4)
# O(n^3)
def cykl4(G):
    n = len(G)
    for i in range(n):
        for j in range(i + 1, n):
            counter = 0
            for k in range(n):
                if G[i][k] and G[j][k]:
                    counter += 1
            if counter >= 2:
                return True
            
    return False

# 5 Graf skierowany G, jako macierz sasiedztwa
# Znalezć uniwersalne ujście t
# a) dla kazdego v istnieje krawedz z v do t
# b) t nie posiada krawedzi wychodzacych
#TODO

G = [[0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [1, 0, 0, 1, 1], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 1, 0]]

def exit(G):
    n = len(G)
    i = 0
    j = 0

    while j < n and i < n:
        if G[i][j] == 0:
            j += 1
        elif G[i][j] == 1:
            i += 1
    for k in range(n):
        if G[k][i] == 0:
            if k != i:
                return None
    return i

print(exit(G))
# 6 zdj
# szukamy najprostrzej siezki w grafie nieskierowanym bfs
#TODO

def spath(G, s, t):
    vis = [0]*len(G)
    par = [-1]*len(G)
    g = Queue(0)
    # vis[]

# 7 dana jest szachownica nxn
#kazde pole ma wart. = {1, 2, 3, 4, 5}
#chcemy w tajtańszy sposób przejsc z lewego gornego do prawego dolnego
# szukany: minimalny koszt
#TODO

# zadanie 8
#malejące krawędzie
# G = (V,E)
# koszt {1, ..., |E|} kazda krawedz ma inny koszt
#chcemy przejsc z krawdzi od s -> t
# koszt jest malejący
# dfs
#TODO

#zadanie 9
# graf to jest mapa drogowa kraju i chcemy przejechac jak najtaniej, gdzie koszt przejazdu to moze byc 0 lub 1
#TODO