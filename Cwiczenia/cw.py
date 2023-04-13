#1 sprawdzanie czy graf jestr dwudzielny BFS

def dwudzielny(G):
    colors = [-1] * len(G)
    Q = Queue()
    start_v = 0
    q.put(start_v)
    colors[start_v] = 1
    while not Q.empyt():
        v = Q.get()
        for n in G[v]:
            if colors[n] == -1:
                colors[n] = (colors[v] + 1)%2
                Q.put()
            else:
                if colors[n] == colors[v]:
                    return False
    return True
# lista spojnych skladowych w grafie DFS

def ccs(G):
    vis = [0]*len(G)
    def DFS(v):
            vis[v] = 1
            for x in G[v]:
                if vis[x]: continue
                DFS(x)
    i = 0
    for i in range(len(G)):
        if not vis[l]:
            l = 1
            DFS(i)
    return i

# stacje nadwacze odłączanie

#dany jest graf G jako macierz sąsiedztwa, czy w tym grafie istnieje cykl długosci 4, składajaący się dokładnie z 4 wierzchłów?

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
#graf skierowany
# znaleźć uniwersalne wyjścia t
# a dla kadego b 

# zdj

# szukamy najprostrzej siezki w grafie nieskierowanym bfs

def s(G, s, t):
    vis = [0]*len(G)
    par = [-1]*len(G)
    g = Queue()
    vis[]

# dana jest szachownica nxn
#kazde pole ma wart. = {1, 2, 3, 4, 5}
#chcemy w tajtańszy sposób przejsc z lewego gornego do prawego dolnego
# szukany: minimalny koszt

# zadanie 7
#malejące krawędzie
# G = (V,E)
# koszt {1, ..., |E|} kazda krawedz ma inny koszt
#chcemy przejsc z krawdzi od s -> t
# koszt jest malejący
# dfs