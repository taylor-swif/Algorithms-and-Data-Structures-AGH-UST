def roznica(S):
    n = len(S)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        if S[i] == "0":
            dp[i][i] = 1
        else:
            dp[i][i] = -1
    
    for a in range(n):
        for b in range(a + 1, n):
            if S[b] == "0":
                dp[a][b] = dp[a][b - 1] + 1
            else:
                dp[a][b] = dp[a][b - 1] - 1
    maxx = -float('inf')
    for i in range(n):
        for j in range(i, n):
            maxx = max(maxx, dp[i][j])
    print(*dp, sep='\n')
    return maxx
    

s = "11000010001"
print(roznica(s))