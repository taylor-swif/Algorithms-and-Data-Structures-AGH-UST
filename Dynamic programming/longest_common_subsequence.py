

def LCS(A, B):
    n = len(A)
    m = len(B)

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = int(A[0] == B[0])

    # filling the first row
    for i in range(1, m):
        if A[0] == B[i] or dp[0][i - 1] > 0:
            dp[0][i] = 1

    # filling the firs column 
    for i in range(1, n):
        if A[i] == B[0] or dp[i - 1][0] > 0:
            dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + int(A[i] == B[j]))
            # if A[i] == B[j]:
            #     dp[i][j] = dp[i - 1][j - 1] + 1
            # else:
            #     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    print("  ",end="")
    for i in range(m):
        print(B[i], end=" ")
    
    print()
    for i in range(n):
        print(A[i], end=" ")
        for j in range(m):
            print(dp[i][j], end=" ")
        print()
    return dp[n - 1][m - 1]

A = "bsbininm"
B = "jmjkbkjkv"

print(LCS(A, B))