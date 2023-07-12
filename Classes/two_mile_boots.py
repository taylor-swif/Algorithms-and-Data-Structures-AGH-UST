from queue import PriorityQueue

# Dany jest wazony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania sie po grafie. Dwrmilowe buty umozliwiaja pokonywanie sciezki zlozonej z dwóch krawedzi grafu tak, jakby byla ona pojedyncza krawedzia o wadze równej maksimum wag obu krawedzi ze sciezki.
# Istnieje jednak ograniczenie - pomiedzy kazdymi dwoma uzyciami dwumilowych butów nalezy przejsc w grafie co najmniej jedna krawedé w sposób zwyczajny. Macierz G zawiera wagi krawedzi w grafie, bedace liczbami naturalnymi, wartosc 0 oznacza brak krawedzi.
# Prosze opisac, zaimplementowaé i oszacowac zlozonosé algorytmu znajdowania najkrotszej sciezki w grafie z wykorzystaniem mechanizmu dwumilowych butów.
# Rozwiazanie nalezy zaimplementowac w postaci funkcji:
# def jumper (G, s, w):
# która zwraca dlugosc najkrotszej scienki w grafie G pomiedzy wierzcholkami s i w, zgodnie z za-sadami uzywania dwumilowych butów.
# 'Zaimplementowana funkcja powinna by mozliwie jak najszybsza. Prose przedstawié zlozonosé czasowa oraz pamieciowa u¿ytego algorytmu.
# Przyklad. Rozwaimy nastepujacy graf:
# Najkrótsza Sciezka miedzy wierzcholkami 0 i 4 wykorzystujaca dwrmilowe buty bedzie scie¿ka [0, 1, 2, 4] o diugosci 10 (z. krawedzia (2, 4) bedaca dwumilowym skokiem). Scierka [0, 2, 4] zlozona z dwóch dwrumilowych skoków bylaby krotsza, ale nie spelnia warunków zadania.

def boots(G, x, y):
    n = len(G)
    dist_A = [float('inf') for _ in range(n)]
    dist_B = [float('inf') for _ in range(n)]
    dist_C = [float('inf') for _ in range(n)]
    parent_A = [None for _ in range(n)]
    parent_B = [None for _ in range(n)]
    parent_C = [None for _ in range(n)]
    dist_A[0] = 0

    def relax(u, v, way, edge):
        if way == 'A1':
            if dist_A[v] > dist_A[u] + edge:
                dist_A[v] = dist_A[u] + edge
                return True
            return False
        elif way == 'A2':
            if dist_C[v] > dist_A[u]:
                dist_C[v] = dist_A[u]
                return True
            return False
        elif way == 'C':
            if dist_B[v] > dist_C[u] + edge:
                dist_B[v] = dist_C[u] + edge
                return True
            return False
        elif way == 'B':
            if dist_A[v] > dist_B[u] + edge:
                dist_A[v] = dist_B[u] + edge
                return True
            return False


    Q = PriorityQueue()

    Q.put([0, 0, 'A', 0])

    while not Q.empty():
        _, u, way, last = Q.get()
        for v, edge in G[u]:
            if way == 'A':
                if relax(u, v, 'A1', edge): # goes to A
                    parent_A[v] = u
                    Q.put([dist_A[v], v, 'A', 0])
                if relax(u, v, 'A2', edge): # goes to C
                    parent_C[v] = u
                    Q.put([dist_C[v], v, 'C', edge])
            if way == 'B': 
                if relax(u, v, 'B', edge):# goes to A
                    parent_A[v] = u
                    Q.put([dist_A[v], v, 'A', 0])
            if way == 'C':
                kraw = max(edge, last)
                if relax(u, v, 'C', kraw):
                    parent_B[v] = u
                    Q.put([dist_B[v], v, 'B', 0])
    print(dist_A)
    print(dist_B)
    print(dist_C)
    print(parent_A)
    print(parent_B)
    print(parent_C)

G =[[(1, 1)], [(2, 1)], [(3, 7)], [(4, 8)], []]
print(boots(G, 0, len(G) - 1))