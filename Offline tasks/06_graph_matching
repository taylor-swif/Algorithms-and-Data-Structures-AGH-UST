from zad6testy import runtests
from collections import deque

def bfs(G, s, t):
    n = len(G)
    parent = [None for v in range(n)]
    visited = [False for v in range(n)]
    
    Q = deque()

    Q.append(s)
    visited[s] = True
    while Q:
        v = Q.popleft()

        for i in G[v]:
            if not visited[i]:
                parent[i] = v
                visited[i] = True
                Q.append(i)
    if parent[t] == None:
        return None
    
    return parent

def make_graph( G ):
    n = len(G)
    G.extend([[] for _ in range(n+2)])
    for i in range(n):
        for j in range(len(G[i])):
            G[i][j] += n
    for i in range(n):
        G[n + i].append(2*n+1)
        G[2*n].append(i)
    return G


def Ford(G, s, t):
    max_flow = 0
    parent = bfs(G, s, t)

    while parent:
        v = t
        while parent[v]:
            G[v].append(parent[v])
            G[parent[v]].remove(v)
            v = parent[v]

        max_flow += 1
        parent = bfs(G, s, t)
    
    return max_flow

def binworker( M ):
    G = make_graph(M)
    n = len(G)
    return Ford(G, n - 2, n - 1)

runtests( binworker, all_tests = False )



# Firma Binary Works zajmuje się produkcją kubełków do sortowania liczb. W firmie jest n pracow- ników oraz n maszyn pozwalających na tworzenie kubełków. Niestety praktycznie każde urządzenie pochodzi od innego wytwórcy i wymaga innych umiejętności. Stąd nie wszyscy pracownicy po- trafią obsługiwać każde z nich. Zadanie polega na zaimplementowaniu funkcji: Zadanie polega na zaimplementowaniu funkcji:
#     def binworker( M )
# gdzie M to tablica tablic o następującej interpretacji: Dla każdego i ∈ {0, . . . , n − 1} M [i] to lista numerów maszyn (ze zbioru {0,...,n} na których pracownik numer i potrafi pracować. Funkcja powinna zwrócić maksymalną liczbę pracowników, którzy mogą jednocześnie pracować (na danej maszynie może na raz pracować jednocześnie tylko jeden pracownik).
# Przykład. Rozważmy następujące dane:
# M=[ [ 0, 1, 3], #0 [ 2, 4], #1 [ 0, 2], #2 [ 3 ], #3 [ 3, 2] ] #4
# Wynikiem wywołania binworker(M) powinno być 5. W szczególności: - pracownik 0 może pracować na maszynie 1,
# - pracownik 1 może pracować na maszynie 4,
# - pracownik 2 może pracować na maszynie 0,
# - pracownik 3 może pracować na maszynie 3, - pracownik 4 może pracować na maszynie 2.