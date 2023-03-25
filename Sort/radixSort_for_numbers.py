def countingSort(T, pos):
    n = len(T)
    C = [0]*10
    B = [0]*n

    for i in range(n):
        C[T[i]//pos%10] += 1
    
    for i in range(1,10):
        C[i] = C[i] + C[i - 1]

    for i in range(n-1, -1, -1):
        B[C[T[i]//pos%10] - 1] = T[i]
        C[T[i]//pos%10] -= 1

    for i in range(0, n):
        T[i] = B[i]

def radixSort(T):

    max_element = max(T)

    pos = 1
    while max_element // pos > 0:
        countingSort(T, pos)
        pos *= 10

T = [1 ,21, 6, 7, 10, 123, 1023, 121]
radixSort(T)
print(T)