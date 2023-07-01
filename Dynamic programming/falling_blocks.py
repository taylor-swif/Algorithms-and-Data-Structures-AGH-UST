# Kazdy klocek to przedzial postaci [a, b]. Dany jest ciag klocków [a1, b1], [a2, 62], . .., [an, bn]. 
# Klocki spadaja na os liczbowa w kolejnosci podanej w ciagu. Prosze zaproponowac algorytm, który oblicza ile klockow nalezy usunac z listy tak, 
# zeby kazdy kolejny spadajacy klocek mieścił się w całości w tym, który spadł tuz przed nim.

# f(i) - najwysza "wieza", jaką mozemy zbudowac, konczaca sie na klocu o indeksie i

def fitting(a, b):
    return a[0] <= b[0] and b[1] <= a[1]
# O(n^2)
def removed_blocks(A):
    n = len(A)
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if fitting(A[j], A[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return n - dp[n - 1]

# O(nlogn) based on lis

blocks = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]

print(removed_blocks(blocks))