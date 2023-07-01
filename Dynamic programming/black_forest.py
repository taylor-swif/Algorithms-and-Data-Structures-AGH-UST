# Black Forest to las rosnacy na osi liczbowej gdzies w poludniowej Angli. Las
# sklada sie z n drzew rosnacych na pozycjach 0, ..., n - 1. Dla kazdego i € {0,.
# ..,n-1} zany jest zysk ci, jaki mozna osiagnac scinajac drzewo z pozycji i. John Lovenoses chce uzyskac maksymalny zysk ze scinanych
# drew, ale prawo zabrania scinania dwoch drew pod rzad. Prosze zaproponowac algorytm, dzieki któremu
# John znajdzie optymalny plan wvcinki.

# f(i) - maksymalny zysk jaki mozemy uzyskać ścinając drzewa spośród i pierwszych
def forest(A):
    n = len(A)
    dp = [float('inf') for _ in range(n)]
    dp[0], dp[1] = A[0], A[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + A[i], dp[i - 1])
    
    return dp[n - 1]


A = [1, 8, 3, 4, 5, 1, 2]
A = [8, 1, 3, 4, 5, 1, 2]
A = [8, 12, 3, 4, 7, 1, 2, 10]
print(forest(A))