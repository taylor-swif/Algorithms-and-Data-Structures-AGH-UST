# from queue import PriorityQueue

# que = PriorityQueue(3)

# que.put((2,'a'))
# que.put((1,'b'))
# que.put((3,'c'))
# print(que.full())

# que.put((5,'d'))
# print("pomidor")
# print(que.full())
from random import randint
def merge(T, p, q, r):
    A = T[p:r +1]

    q -= p
    r -= p
    i = 0
    j = q + 1
    k = p
    while i < q + 1 and j < r + 1:
        if A[i] <= A[j]:
            T[k] = A[i]
            i += 1  
        else:
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

def mergeSort(T, p, r):
    if p == r:
        return
    q = (p + r)//2
    mergeSort(T, p, q)
    mergeSort(T, q + 1, r)
    merge(T, p, q, r)


def countingSort(T):
    n = len(T)
    C = [0]*21
    B = [0]*n
    
    for i in range(n):
        C[T[i]] += 1
    
    for i in range(1, 20):
        C[i] += C[i - 1]
    
    for i in range(n-1, -1, -1):
        B[C[T[i]] - 1] = T[i]
        C[T[i]] -= 1
    for i in range(n):
        T[i] = B[i]

T = [randint(1, 20) for i in range(10)]
print(T)
countingSort(T)
print(T)