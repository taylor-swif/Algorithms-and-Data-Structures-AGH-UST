def merge(T, p, q ,r):
    A = [T[p + i] for i in range(r - p  +1)]


    r -= p
    q -= p

    i = 0
    j = q + 1
    k = p
    
    while i < q + 1 and j < r + 1:
        if A[i] <= A[j]:
            T[k] = A[i]
            i += 1
        elif A[i] > A[j]:
            T[k] = A[j]
            j += 1
        k += 1
    
    while i < q + 1:
        T[k] = A[i]
        i += 1
        k += 1
    
    while j < r + 1:
        T[k] = A[j]
        j += 1
        k += 1




def mergeSort(T, p, r):
    if p == r:
        return
    
    q = (p + r)//2

    mergeSort(T, p, q)
    mergeSort(T, q + 1, r)
    merge(T, p, q, r)

T = [2, 1, 4, 5, 1, 6, 7, 9, 12, 3, 4]
mergeSort(T, 0, len(T) - 1)
print(T)
