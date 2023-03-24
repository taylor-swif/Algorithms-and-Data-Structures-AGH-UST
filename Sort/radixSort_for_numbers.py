def countingSort(T, pos):
    n = len(T)
    C = [0]*10
    B = [0]*n

    for i in range(n):
        C[T[i]//pos%10] += 1

    

def radixSort(T):

    max_element = max(T)
