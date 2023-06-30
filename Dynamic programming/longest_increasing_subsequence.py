
# f(i) - length of the longest subseq ending on A[i]

def ps(A, P, i): # parent searching
    if P[i] != -1:
        ps(A, P, P[i])
    print(A[i])

def lis(A):
    n = len(A)
    F = [1] * n
    #P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                #P[i] = j
                F[i] = F[j] + 1

    # ps(A, P, 8)
    return max(F)#, P

A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
print(lis(A))