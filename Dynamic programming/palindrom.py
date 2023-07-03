# Find such a coherent fragment of this sequence in which the difference between the number of zeros and ones will be the greatest
def palindrom(S):
    n = len(S)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(1, n):
        dp[i][i] = 1
        if s[i] == s[i - 1]:
            dp[i - 1][i] = 1

    for l in range(3, n + 1):
        for i in range(0, n - l + 1):
            if s[i] == s[i + l - 1] and dp[i + 1][i + l - 2]:
                dp[i][i + l - 1] = 1
    maxx = 1
    for i in range(1):
        for j in range(n - 1, i, -1):
            if dp[i][j] == 1:
                maxx = max(maxx, j - i + 1)
                break
    print(*dp, sep='\n')
    return maxx
s = "kajak"
print(palindrom(s))