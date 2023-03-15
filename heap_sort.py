def heapify(T, i, n):

    l = 2*i + 1
    r = 2*i + 2

    max_i = i
    
    if l < n and T[l] > T[i]:
        max_i = l

def heapsort(T):
