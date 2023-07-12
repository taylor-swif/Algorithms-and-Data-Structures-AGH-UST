from queue import PriorityQueue
# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzcholki to
# miasta a krawedzie to drogi laczace miasta. Da kazdej drogi znana jest jej dlugosc (wyrazona w kilometrach# BOB jedzie za darmo
# jako liczba naturalna). Alicja i Bob prowadza (na zmiane) autobus z miasta « € V do miasta y € V, zamienia-
# jac sie za kierownica w kazdym kolejnym miescie. Alicja wybiera trase oraz decyduje, kto prowadzi pierwszy. Prosze zapropnowac algorytm, który wskazuje taka trase (oraz osobe, która ma prowadzié pierwsza), zeby Alicia przeiechala jak naimniei kilometrów. Algorvtm powinien bvé jak naiszvbszy (ale prede wszvstkim
# poprawn).

BOB = 1
ALA = 0
def ula(G, s, t):
    n = len(G)
    d = [[float('inf'), float('inf')] for _ in range(n)]
    Q = PriorityQueue()
    d[s][0] = d[s][1] = 0
    Q.put((0, s, 0))
    Q.put((0, s, 1))

    # bob jechal = 1
    # ala jechala = 0
    # prev = x oznacza ze do v dojechal x
    def relax(u, v, cost, prev):
        if prev == BOB:
            if d[v][ALA] > d[u][BOB] + cost:
                d[v][ALA] = d[u][BOB] + cost
                Q.put((d[v][ALA], v, ALA))
        else: #if prev == ALA:
            if d[v][BOB] > d[u][ALA]:
                d[v][BOB] = d[u][ALA]
                Q.put((d[v][BOB], v, BOB))

    while not Q.empty():
        weight, u, prev = Q.get()

        for cost, v in G[u]:
            relax(u, v, cost, prev)

    print(*d, sep='\n')

G = [[[10,1],[50,3],[200,6]],
     [[10,0],[10,3]],
     [[10,3],[30,4]],
     [[10,1],[50,0],[10,2]],
     [[30,2],[40,5]],
     [[200,6],[40,4]],
     [[200,5],[200,0]]]

print(ula(G, 0, 5))