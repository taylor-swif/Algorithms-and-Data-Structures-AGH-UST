def bubbleSort(T):
    n = len(T)

    for i in range(n):
        for j in range(0, n-1-i):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]