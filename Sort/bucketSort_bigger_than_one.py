from math import floor

def insertionSort(A):
    n = len(A)

    for i in range(n-1):
        if A[i + 1] < A[i]:
            k = i + 1
            while k > 0 and A[k] < A[k - 1]:
                A[k], A[k - 1] = A[k - 1], A[k]


def bucketSort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]

    max_num = max(A)

    for i in range(n):
        buckets[floor((A[i]/(max_num+1)*n))].append(A[i])

    
    k = 0
    for arr in buckets:
        insertionSort(arr)
        for num in arr:
            A[k] = num
            k += 1

