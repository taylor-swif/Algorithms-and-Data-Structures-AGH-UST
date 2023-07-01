
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

# https://cp-algorithms.com/sequences/longest_increasing_subsequence.html#solution-in-on-log-n-with-dynamic-programming-and-binary-search
def lis_v2(A):
    n = len(A)
    last = [float('inf') for _ in range(n + 1)]
    last[0] = float('-inf')

    for i in range(n):
        for j in range(1, n + 1):
            if last[j - 1] < A[i] < last[j]:
                last[j] = A[i]
    print(last)

    for i in range(n, 0, -1):
        if last[i] < float('inf'):
            return i
    return 0

### nlogn
def binary_search(A, val): # returns first greater than val
    left_idx = 0
    right_idx = len(A) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) //2

        if val > A[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    return left_idx

def lis_v2_nlogn(A):
    n = len(A)
    last = [float('inf') for _ in range(n + 1)]
    last[0] = float('-inf')

    for i in range(n):
        idx = binary_search(last, A[i])
        last[idx] = A[i]

A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
A = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
print(lis_v2(A))