import heapq
def spacetravel( n, E, S, a, b ):

    G =[[] for _ in range(n)]

    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    for i in S:
        for j in S:
            if j != i:
                G[i].append((j, 0))
                G[j].append((i, 0))
        
    dist = [float('inf') for v in range(n)]
    prev = [None for v in range(n)]
    dist[a] = 0

    pq = []
    heapq.heappush(pq, (0, a))

    done = [False for v in range(n)]
    done[a] = True

    while pq:
        weight_u, u = heapq.heappop(pq)
        
        for (v, weight) in G[u]:
            if(dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
        done[u] = True


    if dist[b] == float('inf'):
        return None
    return dist[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( spacetravel, all_tests = True )

# Układ planetarny Algon składa się z n planet o numerach od O do n - l. Niestety własności fizyczne układu powodują, że nie da się łatwo przelecieć między dowolnymi dwiema planetami. Na szczęście mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpo- średnich przelotów. Każdy element listy E to trójka postaci (u, v, t), gdzie u i v to numery planet
# (można założyć, że u < v) a t to czas podróży między nimi (przelot z u do v trwa tyle samo co z v do u). Dodatkową nietypową własnością układu Algon jest to, że niektóre planety znajdują się w okolicy osobliwości. Znajdując się przy takiej planecie możliwe jest zagięcie czasoprzestrzeni umożliwiające przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym.
# Zadanie polega na zaimplementowaniu funkcji: def spacetravel( n, E, S, a, b )
# która zwraca najkrótszy czas podróży z planety a do planety b, mając do dyspozycji listęmożliwych bezpośrednich przelotów E oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie istnieje, to funkcja powinna zwrócić None.
# Rozważmy następujące dane:
# E = [(0,1, 5), (1,2,21), (1,3, 1), (2,4, 7), (3,4,13), (3,5,16), (4,6, 4), (5,6, 1)]
# S = [ o, 2, 3 ] a=1
# b=5
# n=7
# 1
# wywołanie startravel(n, E, S, a, b) powinno zwrócić liczbę 13. Odwiedzamy po kolei planety 1, 3, 2, 4, 6 i kończymyna planecie 5 (z planety 2 do 3 dostajemy sięprzez zagięcieczasoprzestrzeni). Gdyby a= l ab= 2 to wynikiem byłby czas przelotu 1.