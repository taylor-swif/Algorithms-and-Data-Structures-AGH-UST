from zad1testy import Node, runtests

def buildheap(T, k):
    for i in range(k-1, -1, -1):
        heapify(T, i, k)

def heapify(T, i, k):
    l = 2*i + 1
    r = 2*i + 2

    min_i = i
    if l < k and T[min_i] > T[l]:
        min_i = l
    if r < k and T[min_i] > T[r]:
        min_i = r

    if min_i != i:
        T[min_i], T[i] =  T[i], T[min_i]
        heapify(T, min_i, k)


def print_node(n):
    while n.next != None:
        print(n.val, end=" ")
        n = n.next
    print()
    
def print_tab_val(T):
    n = len(T)
    for i in range(n):
        print(T[i], end=" ")
    print()

def SortH(p,k):
    k += 1
    head = p

    heap = [float('inf') for _ in range(k)]


    for i in range(k):
        if head != None:
            heap[i] = head.val
            head = head.next
        else:
            break

    buildheap(heap, k)
    res = Node()
    g = res

    while head != None:
        pomidor = Node()
        if heap[0] == float('inf'):
            break
        pomidor.val = heap[0]

        res.next = pomidor
        res = res.next
        heap[0] = head.val
        head = head.next
        heapify(heap, 0, k)

    while heap[0] != float('inf'):
        pomidor = Node()
        pomidor.val = heap[0]

        res.next = pomidor
        res = res.next
        heap[0] = float('inf')
        heapify(heap, 0, k)

    return g.next

n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n1.val = 2
n2.val = 1
n3.val = 4
n4.val = 3
n5.val = 6
n6.val = 5

#n1 = SortH(n1, 2)
#print_node(n1)

runtests( SortH ) 
