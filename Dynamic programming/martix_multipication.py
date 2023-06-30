# this algorithm calculate minimum cost of matrix chain multipication

def min_mult_rek(dims, i, j):
    if i == j:
        return 0
    
    min = float('inf')
    for k in range(i, j):
        left = min_mult_rek(dims, i, k)
        right = min_mult_rek(dims, k + 1, j)
        skrt = dims[i-1] * dims[k] * dims[j]
        res = left + right + skrt

        if (res < min):
            min = res
    return min

def make_dims(A):
    dims = [0 for _ in range(len(A) + 1)]
    dims[0] = A[0][0]
    for i in range(1, len(A)):
        dims[i] = A[i][0]
    dims[len(A)] = A[len(A) - 1][1]
    return dims

def min_mult_dp(A):
    n = len(A)

    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0 # that's for matrix multipication by itself
        # when length of subsequence equals 1

    for i in range(n - 1):
        dp[i][i + 1] = A[i][0] * A[i][1] * A[i + 1][1] # (AB), (BC), (CD)...
    
    for j in range(2, n): # length of the product, starting from length 3
        for i in range(n - j): # starting index
            for k in range(i, i + j): # checking each possibilities
                dp[i][i + j] = min(dp[i][i + j], dp[i][k] + dp[k + 1][i + j] + A[i][0] * A[k][1] * A[i + j][1])

    print(*dp, sep='\n')
    return dp[0][n - 1]

A1 = [(1, 3), (3, 5)] # 15
A2 = [(1, 3), (3, 5), (5, 7)] # 50
A3 = [(40, 20), (20, 30), (30, 10), (10, 30)] # 26000
A4 = [(10, 20), (20, 30), (30, 40), (40, 30)] # 30K
A4 = [(2, 2), (2, 8), (8, 6), (6, 9), (9, 9), (9, 2), (2, 1), (1, 9), (9, 6)] # 287
A5 = [(2, 2), (2, 8), (8, 6), (6, 9), (9, 9), (9, 2), (2, 1)] # 221
# print(min_mult_rek(make_dims(A2), 1, len(A2)))
print(min_mult_dp(A5))