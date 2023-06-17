from queue import PriorityQueue

def collect_oil(T, i, j):
    sum = T[i][j]
    T[i][j] = 0
    if j + 1 < len(T[0]) and T[i][j + 1] > 0:
        sum += collect_oil(T, i, j + 1)
    if  j - 1 > 0 and T[i][j - 1] > 0:
        sum += collect_oil(T, i, j - 1)
    if i + 1 < len(T) and T[i + 1][j] > 0:
        sum += collect_oil(T, i + 1, j)
    if i - 1 >= 0 and T[i - 1][j]: 
        sum += collect_oil(T, i - 1, j)
    return sum

def plan(T):
    q = PriorityQueue()
    m = len(T[0])
    for j in range(len(T[0])):
        if T[0][j] > 0:
            x = collect_oil(T, 0, j)
            T[0][j] = x

    gas = T[0][0]
    T[0][0] = 0
    stops = 1
    i = 0

    while i + gas < m - 1:
        for k in range(i, i + gas + 1):
            q.put(-T[0][k])
            T[0][k] = 0
        i += gas
        gas = -q.get()
        stops += 1
        
    return stops

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( plan, all_tests = True )


# W roku 2050 Maksymilian odbywa podróż przez pustynię z miasta A do miasta B. Droga pomiędzy miastami jest linią prostą na której w pewnych miejscach znajdują się plamy ropy. Maksymilian porusza się 24 kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy. Cysterna wyposażona jest w pompę pozwalającą zbierać ropę z plam. Aby dojechać z miasta A do miasta B Maksymilian będzie musiał zebrać ropę z niektórych plam (by nie zabrakło paliwa), co każdorazowo wymaga zatrzymania cysterny. Niestety, droga jest niebezpieczna. Maksymilian musi więc tak zaplanować trasę, by zatrzymać się jak najmniej razy. Na szczęście cysterna Maksymiliana jest ogromna - po zatrzymaniu zawsze może zebrać całą ropę z plamy (w cysternie zmieściłaby się cała ropa na trasie).
# Zaproponuj i zaimplementuj algorytm wskazujący, w których miejscach trasy Maksymilian powi- nien się zatrzymać i zebrać ropę. Algorytm powinien być możliwe jak najszybszy i zużywać jak najmniej pamięci. Uzasadnij jego poprawność i oszacuj złożoność obliczeniową.
# Dane wejściowe reprezentowane są jako dwuwymiarowa tablica liczb naturalnych T, w której wartość T[u][v] to objętość ropy na polu o współrzędnych (u,v) (objętość 0 oznacza brak ropy). Współrzęd- ne u należą do zbioru {0,1,...,n−1} a współrzędne v to zbioru {0,1,...,m−1}. Miasto A znajduje się na polu (0, 0), zaś miasto B na polu (0, m − 1). Maksymilian porusza się jedynie po polach (0,0), (0,1),...(0,m−1). Bok każdego pola ma długość 1 kilometra. Plamą ropy jest dowolny spójny obszar pól zawierających ropę. Dwa pola należą do spójnego obszaru jeśli mają wspólny bok lub są połączone sekwencją pól (zawierających ropę) o wspólnych bokach. Zakładamy, że po- czątkowo cysterna jest pusta, ale pole (0,0) jest częścią plamy ropy, którą można zebrać przed wyruszeniem w drogę. Zakładamy również, że zadanie posiada rozwiązanie, t.j. da się dojechać z miasta A do miasta B.
# Algorytm należy zaimplementować w funkcji:
# def plan(T)
# która przyjmuje tablicę z opisem zadania i zwraca minimalną liczbę zatrzymań cysterny potrzebną do przejechania trasy (cysterna porusza się tylko po polach (0,v)). Postój na polu (0,0) również jest częścią rozwiązania.
