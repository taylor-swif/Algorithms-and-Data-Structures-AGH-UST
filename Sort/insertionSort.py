def insertionSort(T):
    n = len(T)
    if T[0] > T[1]:
        T[0], T[1] = T[1], T[0]

    for i in range(1, n - 1):
        if T[i+1] < T[i]:
            k = i + 1
            while k > 0 and T[k - 1] > T[k]:
                T[k - 1], T[k] = T[k], T[k - 1]
                k -= 1
