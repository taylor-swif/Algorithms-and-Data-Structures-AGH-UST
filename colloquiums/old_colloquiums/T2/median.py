def merge(T, p, q, r):
    A = T[p:r+1]

    k = p
    q -= p
    r -= p

    i = 0
    j = q + 1

    while i < q + 1 and j < r + 1:
        if A[i] <= A[j]:
            T[k] = A[i]
            i += 1
        else:
            T[k] = A[j]
            j += 1
        k +=1

    while i < q + 1:
        T[k] = A[i]
        i += 1
        k += 1

    while j < r + 1:
        T[k] = A[j]
        j += 1
        k += 1


def mergeSort(T, p, r):
    if p < r:
        q = (p + r)//2
        mergeSort(T, p, q)
        mergeSort(T, q + 1, r)
        merge(T, p, q, r)

def median(T):

    A = []
    for tab in T:
        for item in tab:
            A.append(item)
    
    n = len(A)
    mergeSort(A, 0, n - 1)

    x, y, k = 0, n//2, n//2 + int(n**0.5)-1
    for i in range(int(n**0.5)):
        for j in range(int(n**0.5)):
            if i == j:
                T[i][j] = A[y]
                y += 1
            elif i > j:
                T[i][j] = A[x]
                x += 1
            else:
                T[i][j] = A[k]
                k += 1



T = [ [ 2, 5, 3], [ 11,7,13], [17,19,23]]
median(T)

for arr in T:
    print(arr)