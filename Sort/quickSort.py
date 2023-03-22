def partition_Lomuto(T, p, r):
    x = T[r]
    i = p - 1

    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quickSort(T, p, r):
    if p < r:
        q = partition_Lomuto(T, p, r)
        quickSort(T, p, q - 1)
        quickSort(T, q + 1, r)


T = [2, 1, 4, 5, 1, 6, 7, 9, 12, 3, 4]
print(T)
quickSort(T, 0, len(T) - 1)
print(T)