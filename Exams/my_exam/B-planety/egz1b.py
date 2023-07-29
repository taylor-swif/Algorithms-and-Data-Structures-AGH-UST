from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(D)
    dp = [[float('inf') for _ in range(E + 1)] for _ in range(n)]
    
    
    for b in range(E + 1):
        dp[0][b] = C[0] * b

    if T[0][0] > 0:
        if dp[0][0] + T[0][1] < dp[T[0][0]][0]:
            dp[T[0][0]][0] = dp[0][0] + T[0][1]

    for i in range(1, n):
        dist = D[i] - D[i - 1]
        for fuel in range(E - dist + 1):
            dp[i][fuel] = min(dp[i][fuel], dp[i - 1][fuel + dist])
        
        for fuel in range(1, E + 1):
            dp[i][fuel] = min(dp[i][fuel], dp[i][fuel - 1] + C[i])

        if T[i][0] > i:
            if dp[i][0] + T[i][1] < dp[T[i][0]][0]:
                dp[T[i][0]][0] = dp[i][0] + T[i][1]

    return min(dp[n -1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
