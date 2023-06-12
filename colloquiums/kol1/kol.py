from kol1testy import runtests
from queue import PriorityQueue as pq   

def ksum(T, k, p):
    n = len(T)
    visited = [False] * n
    
    minheap = pq() # k - maximum from window
    maxheap = pq() # p - k minimum from window
    for i in range(p):
        maxheap.put((-T[i], i))

    while minheap.qsize() < k:
        a, b = maxheap.get()
        visited[b] = True
        minheap.put((-a, b))
    res = minheap.queue[0][0]

    for i in range(1, n-p+1):
        while not minheap.empty() and minheap.queue[0][1] < i:
            minheap.get()
        while not maxheap.empty() and maxheap.queue[0][1] < i:
            maxheap.get()


        maxheap.put((-T[i+p-1], i+p-1))

        if visited[i-1]:
            maxt, maxtix = maxheap.get()
            visited[maxtix] = True
            minheap.put((-maxt, maxtix))

        elif -maxheap.queue[0][0] > minheap.queue[0][0]:
            maxt, maxtix = maxheap.get()
            mint, mintix = minheap.get()
            visited[maxtix] = True
            visited[mintix] = False

            maxheap.put((-mint, mintix))
            minheap.put((-maxt, maxtix))
            
        while not minheap.empty() and minheap.queue[0][1] < i:
            minheap.get()
        if not maxheap.empty() and maxheap.queue[0][1] < i:
            maxheap.get()
        res += minheap.queue[0][0]

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
# print(ksum([7, 9, 1, 5, 8, 6, 2, 12], 4, 5))
