from zad1testy import Node, runtests

def heapify(t, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    min_idx = i

    if l < n and t[l].val < t[min_idx].val:
        min_idx = l

    if r < n and t[r].val < t[min_idx].val:
        min_idx = r

    if min_idx != i:
        t[i], t[min_idx] = t[min_idx], t[i]
        heapify(t, min_idx, n)

def sortH(p, k):
    k += 1
    g = Node(None)
    w = g
    heap = [0] * k

    for i in range(k):
        heap[i] = p
        p = p.next

    for i in range(k//2, -1, -1):
        heapify(heap, i, k)
    
    while p is not None:
        g.next = heap[0]
        g = g.next
        heap[0] = p
        p = p.next
        heapify(heap, 0, k)

    for i in range(k):
        g.next = heap[0]
        g = g.next
        heap[0] = Node(float('inf'))
        heapify(heap, 0, k)

    return w.next



SortH(n1, 2)

#runtests( SortH ) 