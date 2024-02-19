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

def depth(L):
    n = len(L)
    #L = sorted(L, key=lambda x:x [1], reverse=True)
    #L = sorted(L, key=lambda x:x [0])
    
    mergeSort(L, 0, n-1, 1)
    L = L[::-1]
    mergeSort(L, 0, n-1, 0)

    curr = L[0]
    i = 1
    cnt = 0
    cnt_max = 0
    zmiana = 0
    change = False
    while i < n:
        
        if L[i][0] >= curr[0] and L[i][1] <= curr[1]:
                cnt += 1
        else:
            if not change:
                zmiana = i
                change = True
            if L[i][0] >= curr[1]:
                change = False
                if cnt > cnt_max:
                    cnt_max = cnt
                cnt = 0
                curr = L[zmiana]
                i = zmiana
        i += 1
    if cnt > cnt_max:
        cnt_max = cnt
    return cnt_max

#print(depth([[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64], [22, 85], [7, 52], [41, 42], [23, 72], [9, 58], [28, 31], [53, 58], [3, 8], [6, 85], [47, 84], [30, 41], [27, 76], [10, 81], [36, 67], [61, 98], [35, 88], [6, 81], [20, 55], [9, 14], [35, 60], [34, 37], [43, 64], [6, 41], [56, 67], [82, 97], [72, 79], [6, 53], [71, 80], [1, 14], [80, 87], [38, 77], [60, 91], [6, 81], [68, 75], [1, 74], [24, 51], [17, 90], [28, 71]]))

L = [ [1, 6],
    [5, 6],
    [2, 5],
    [8, 9],
    [1, 6]]
#print(depth(L))
runtests( depth ) 


# for arr in main:
#             if L[i][0] >= arr[0][0] and L[i][1] <= arr[0][1]:
#                 arr[1] += 1
#                 change = True
#             elif L[i][0] <= arr[0][0] and L[i][1] >= arr[0][1]:
#                 arr[0] = L[i]
#                 change = True
#         if not change:
#             main.append([L[i], 0])