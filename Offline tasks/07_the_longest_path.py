def maze(L):
    n = len(L)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    first = [-1 for _ in range(n)]
    second = [-1 for _ in range(n)]
    for i in range(n - 1):
        if L[i + 1][0] == '.':
            dp[i + 1][0] = dp[i][0] + 1
        else:
            break
    
    for j in range(1, n):
        if not( L[0][j] == "#" or dp[0][j - 1] == -1): 
            first[0] = dp[0][j - 1] + 1

        for i in range(1, n):
            if L[i][j] != "#":
                if first[i - 1] == -1 and dp[i][j - 1] == -1:
                    first[i] = -1
                else:
                    first[i] = max(first[i - 1], dp[i][j - 1]) + 1

        if not (L[n - 1][j] == "#" or dp[n - 1][j - 1] == -1): 
            second[n-1] = dp[n-1][j - 1] + 1
        for i in range(n-2, -1, -1):
            if L[i][j] != "#":
                if second[i + 1] == -1 and dp[i][j - 1] == -1:
                    second[i] = - 1
                else:
                    second[i] = max(second[i + 1], dp[i][j - 1]) + 1

        for i in range(n):
            if L[i][j] == '.':
                dp[i][j] = max(second[i], first[i])

        first = [-1 for _ in range(n)]
        second = [-1 for _ in range(n)]
    return dp[n-1][n-1]


# Magiczny Wojownik otrzymał od Dobrego Maga kolejną szansę. Musi przejść przez kwadratowy labirynt złożony z N × N komnat. Rozpoczyna wędrówkę w komnacie o współrzędnych (0, 0) znaj- dującej się na planie w lewym górnym rogu i musi dotrzeć do komnaty o współrzędnych (n−1,n−1) w prawym dolnym rogu. Niektóre komnaty (zaznaczone na planie znakiem #) są niedostępne i nie można do nich się dostać. Wojownikowi wolno poruszać się tylko w trzech kierunkach, opisanych na planie jako Góra, Prawo i Dół oraz nie wolno mu wrócić do komnaty w której już był. Zadanie postawione przez Maga polega na odwiedzeniu jak największej liczby komnat. Zadanie polega na zaimplementowaniu funkcji:
# def maze ( L )
# która otrzymuje na wejściu tablicę L opisującą labirynt i zwraca największą liczbę komnat, które może odwiedzić Wojownik na swojej drodze lub −1 jeśli dotarcie do końca drogi jest niemożliwe. Komnaty początkowej nie liczymy jako odwiedzonej. Funkcja powinna być możliwie jak najszybsza.
# Labirynt opisuje lista L = [W0 , W1 , W2 , . . . , Wn−1 ], gdzie każde Wi to napis o długości n znaków. Znak kropki ’.’ oznacza dostępną komnatę a znak ’#’oznacza komnatę niedostępną.
# Przykład. Rozważmy następujący labirynt:
#     L = [ "....",
#           "..#.",
#           "..#.",
# "...." ]
# Optymalna droga wojownika to: DDDPGGGPPDDD, podczas której Wojownik odwiedził 12 kom- nat.