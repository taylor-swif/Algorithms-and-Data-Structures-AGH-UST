def partitionLomuto(T, p, r):
    pivot = T[r]
    i = p - 1

    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1

def partitionLomutov2(T, p, r):
    x = T[r]

    i = p - 1
    k = p

    while i < r:
        i += 1
        if T[i] < x:
            T[i], T[k] = T[k], T[i]
            k += 1
    T[r], T[k] = T[k], T[r]

    return k

def partiotionHoare(T, p, r):
    pivot = T[p]
    i = p - 1
    j = r + 1

    while True:

        i += 1
        while T[i] < pivot:
            i += 1

        j -= 1
        while T[j] > pivot:
            j -= 1
        
        if i >= j:
            return i

        T[i], T[j] = T[j], T[i]
      



def quickSort(T, p, r):
    if p < r:

        q = partitionLomuto(T, p, r)
        quickSort(T, p, q - 1)

        #q = partiotionHoare(T, p, r)
        #quickSort(T, p, q)
        
        quickSort(T, q + 1, r)

def quickSortTail(T, p, r):
    while p < r:

        q = partitionLomuto(T, p, r)
        quickSort(T, p, q - 1)
        p = q + 1


T = [2, 1, 4, 5, 1, 6, 7, 9, 12, 3, 4]
print(T)
quickSortTail(T, 0, len(T) - 1)
print(T)