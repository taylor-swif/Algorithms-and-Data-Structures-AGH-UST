# A - amount to make a charge of
# C - total coins provided

def charge(A, C):
    dp = [float('inf') for _ in range(A + 1)]
    dp[0] = 0

    for i in range(1, A + 1):
        for coin in C:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    return dp[A]

A = 15
C = [1, 5, 8]
print(charge(A, C))