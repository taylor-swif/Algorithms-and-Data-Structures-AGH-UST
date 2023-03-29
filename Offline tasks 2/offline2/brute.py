from zad2testy import runtests
def merge(T, p, q ,r, idx):
    A = [T[p + i] for i in range(r - p  +1)]


    r -= p
    q -= p

    i = 0
    j = q + 1
    k = p
    
    while i < q + 1 and j < r + 1:
        if A[i][idx] <= A[j][idx]:
            T[k] = A[i]
            i += 1
        elif A[i][idx] > A[j][idx]:
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




def mergeSort(T, p, r, idx):
    if p == r:
        return
    
    q = (p + r)//2

    mergeSort(T, p, q, idx)
    mergeSort(T, q + 1, r, idx)
    merge(T, p, q, r, idx)

def merg(L, P):
    i = 0
    j = 0
    l = len(L)
    p = len(P)
    Merged = []
    #print(L, P)
    while i < l and j < p:
        if L[i][0] < P[j][0]:
            Merged.append(L[i])
            i += 1
        elif L[i][0] == P[j][0]:
            if L[i][1] > P[j][1]:
                Merged.append(L[i])
                i += 1
            else:
                Merged.append(P[j])
                j += 1
        else:
            Merged.append(P[j])
            j += 1

    while i<l:
        Merged.append(L[i])
        i += 1
    while j<p:
        Merged.append(P[j])
        j += 1

    return Merged


def mergsort(A, p, k):
    #print("Rekursja")
    if p == k:
        #print("najmniejsza")
        return [A[p]]
    else:
        #print("glebiej ",p,k)
        L = mergsort(A, p,(p+k) // 2)
        P = mergsort(A, ((p+k) // 2) + 1, k)

        New = merg(L, P)
        #print(New," Nowa")

        return New
def depth(L):
    n = len(L)
    #L = sorted(L, key=lambda x:x [1], reverse=True)
    #L = sorted(L, key=lambda x:x [0])
    
    mergeSort(L, 0, n-1, 1)
    L = L[::-1]
    mergeSort(L, 0, n-1, 0)
    #L = mergsort(L, 0, n - 1)

    main = []

    for i in range(n):
        change = False
        for arr in main:
            if L[i][0] >= arr[0][0] and L[i][1] <= arr[0][1]:
                arr[1] += 1
                change = True
            elif L[i][0] <= arr[0][0] and L[i][1] >= arr[0][1]:
                arr[0] = L[i]
                change = True
        if not change:
            main.append([L[i], 0])
    
    res = 0
    for arr in main:
        if arr[1] > res:
            res = arr[1]                 
    return res
#print(depth([[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64], [22, 85], [7, 52], [41, 42], [23, 72], [9, 58], [28, 31], [53, 58], [3, 8], [6, 85], [47, 84], [30, 41], [27, 76], [10, 81], [36, 67], [61, 98], [35, 88], [6, 81], [20, 55], [9, 14], [35, 60], [34, 37], [43, 64], [6, 41], [56, 67], [82, 97], [72, 79], [6, 53], [71, 80], [1, 14], [80, 87], [38, 77], [60, 91], [6, 81], [68, 75], [1, 74], [24, 51], [17, 90], [28, 71]]))
runtests( depth ) 
