
def countingSort(T, k):
    n = len(T)
    C = [0]*k
    B = [0]*n

    for i in range(n):
        C[T[i]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    
    
    for i in range(n - 1, -1, -1):
        B[C[T[i]] - 1] = T[i]
        C[T[i]] -= 1
        
    for i in range(n):
        T[i] = B[i]

T = [2, 1, 4, 5, 1, 6, 7, 9, 8, 3, 4]
countingSort(T, len(T))
print(T)