from collections import deque
def bfs(G, s, t, x1, x2):
    n = len(G)
    visited = [False for v in range(n)]
    d = [-1 for v in range(n)]
    Q = deque()

    visited[s] = True
    d[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v] and not (x1 == u and x2 == v) and not (x2 == u and x1 == v):
                visited[v] = True
                d[v] = d[u] + 1
                if(v == t):
                    return d[t]
                Q.append(v)
    return d[t]

def parent_tab(G, s, t):
    n = len(G)
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    d = [-1 for v in range(n)]
    Q = deque()

    visited[s] = True
    d[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                if(v == t):
                    return parent, d[t]
                Q.append(v)
    return parent, d[t]

def longer( G, s, t ):
    parent, dist = parent_tab(G, s, t)
    path =[]
    i = t
    while i != s:
        path.append(i)
        i = parent[i]
    path.append(s)

    if dist == -1:
        return None
    
    for i in range(len(path) - 1, 0, -1):
        curr_dist = bfs(G, s, t, path[i], path[i - 1])
        if curr_dist > dist or curr_dist == -1:
            return (path[i], path[i - 1])
        
    return None
# G =  [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
# print(longer(G, 0, 12))



# Dany jest graf nieskierowany G = (V,E) oraz dwa wierzchołki s,t ∈ V. Proszę zaproponować i zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algo- rytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego poprawność i oszacować złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję:
# def longer(G, s, t):
#    ...
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0. Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie nie było ścieżki z s do t to funkcja powinna zwrócić None.
# Przykład. Dla argumentów:
#     G = [ [1, 2], [0, 2], [0, 1] ]
#      s=0 t=2      

# wynikiem jest np. krotka: (0, 2)