from math import floor
def bubbleSort(T):
    n = len(T)

    for i in range(n):
        for j in range(0, n-1-i):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]


def bucketSort(T):
    n = len(T)
    A = [[] for i in range(n)]

    interval = 1/n

    for i in range(n):
        print(T[i], T[i]/interval, floor(T[i]/interval), interval)
        A[floor(T[i]/interval)].append(T[i])

    print(A)

    for t in A:
        if len(T) > 1:
            bubbleSort(t)
    
    k = 0
    for t in A:
        for num in t:
            T[k] = num
            k += 1
