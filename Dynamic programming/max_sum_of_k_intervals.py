# Rozważamy ciag (a0, .., an-1) liczb naturalnych. Załóżmy, ze zostałpodzielony na k spójnych podcingów: 
# (do, ..., al1), (al1 +1, ..., al2), ..., (alk-1+1, .., an-1). Przez wartość i-go podciagu rozumiemy sume jego elementów 
# a przez najgorszy podciag rozumiemy podciag o najmniejszej wartosci (roz- strzygajac remisy w dowolny sposób). 
# Wartością podziału jest wartość jego najgorszego podciagu. Zadanie polega na znalezieniu podzialu ciagu (a0, . .., an-1) 
# o maksymalnej wartosci.

# F[k][i] - oznacza maksymalną wartości minimalnego podziału dla podziału na k podciągów kończącego się na indeksie i

def k_intervals(A, k):
    n = len(A)
    s = [0 for _ in range(n)]
    s[0] = A[0] # the array that is used to calculate the sum of the interval
    dp = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(1, n):
        s[i] = s[i - 1] + A[i]
        dp[1][i] = s[i]
    
    for t in range(2, k + 1): # finding maximum value for each t splits
        for i in range(t - 1, n):
            for j in range(t - 2, i):
                dp[t][i] = max(dp[t][i], min(dp[t - 1][j], s[i] - s[j]))

    print(*dp, sep='\n')
    
    return dp[k][n - 1]

    
A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
# A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
k = 3
print(k_intervals(A, k))