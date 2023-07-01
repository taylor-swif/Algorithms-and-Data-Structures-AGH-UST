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