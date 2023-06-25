# check if there is subsequence of numbers that sums to T

#initial conditions:
# f(0, t) = A[0], t>= A[0], else 0

# f(i, t) = max( f(i - 1, t - A[i]) + A[i], f(i - 1, t))

def subseq(A, T):
    dp = [[0 for t in range(T + 1)] for a in range(len(A))]

    for a in range(A[0], T + 1):
        dp[0][a] = A[0]

    for i in range(1, len(A)):
        for t in range(T + 1):
            dp[i][t] = dp[i - 1][t]
            if t - A[i] >= 0:
                dp[i][t] = max(dp[i][t], dp[i - 1][t - A[i]] + A[i])
            if(dp[i][t] == T):
                print("there is")

    print(*dp, sep='\n')


A = [3, 0, 5, 2, 7, 13, 8]
T = 10

print(subseq(A, T))

# there is also a lot of increasing performance modifications
# we can clear array A from 0 and nums greater than T