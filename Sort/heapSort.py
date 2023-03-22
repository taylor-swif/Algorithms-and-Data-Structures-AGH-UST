def heapify(T, i, n):
    l = 2*i + 1
    r = 2*i + 2

    max_i = i
    
    if l < n and T[l] > T[max_i]:
        max_i = l
    if r < n and T[r] > T[max_i]:
        max_i = r
    
    if max_i != i:
        T[i], T[max_i] = T[max_i], T[i]
        heapify(T, max_i, n)

def buildHeap(T):
    n = len(T)
    for i in range((n-1)//2, -1, -1):
        heapify(T, i, n)
        

def heapSort(T):
    n = len(T)
    buildHeap(T)

    for i in range(n-1, 0, -1):

        T[i], T[0] = T[0], T[i]
        heapify(T, 0, i)

