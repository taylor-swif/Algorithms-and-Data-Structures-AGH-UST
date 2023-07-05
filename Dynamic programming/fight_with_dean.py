# Dana jest talia N kart wyrażona poprzez tablicę A liczb naturalnych zawierającą wartości tych kart. Można przyjąć, że talia posiada parzystą ilość kart. Karty zostały rozłożone na bardzo szerokim stole w kolejności pojawiania się w tablicy. Dziekan poinformował Cię, że podwyższy Ci ocenę z WDI o pół stopnia, jeżeli wygrasz z nim w pewną grę, polegającą na braniu kart z jednego lub drugiego końca stołu na zmianę. Zakładając, że zaczynasz rozgrywkę, musisz znaleźć jaką maksymalnie sumę wartości kart uda Ci się uzyskać. Jednak, co ważne, musisz przyjąć, że dziekan jest osobą bardzo inteligentną i także będzie grał w 100% na tyle optymalnie, na tyle to możliwe. Aby nie oddawać losu w ręce szczęścia postanowiłeś, że napiszesz program, który zagwarantuje Ci wygraną (lub remis). Twój algorytm powinien powiedzieć Ci, jaka jest maksymalna suma wartości kart, którą masz szansę zdobyć grając z Garkiem.
# Algorytm należy zaimplementować jako funkcję postaci:
# def garek( A ):
#   ...
# która przyjmuje tablicę liczb naturalnych T i zwraca liczbę będącą maksymalną możliwą do uzyskania sumą wartości kart.
# Przykład. Dla tablicy: T = [8, 15, 3, 7]
# Wynikiem jest liczba 22

def cards(A):
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = A[i]
    
    for i in range(n - 1):
        dp[i][i + 1] = max(A[i], A[i + 1])

    for i in range(n):
        dp[i][i] = A[i]
        dp[i - 1][i] = max(A[i - 1], A[i])    

    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = max(A[i] + min(dp[i + 1][j - 1], dp[i + 2][j]), A[j] + min(dp[i][j - 2], dp[i + 1][j - 1]))
    
    return dp[0][n - 1]

A = [8, 100, 4, 3, 7]
print(cards(A))