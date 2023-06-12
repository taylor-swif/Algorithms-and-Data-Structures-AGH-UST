from kol1testy import runtests
# quick select

def partitionLomuto(T, p, r):
    x = T[r]

    i = p - 1
    q = p

    while i < r:
        i += 1
        if T[i] < x:
            T[i], T[q] = T[q], T[i]
            q += 1
    
    T[r], T[q] = T[q], T[r]
    return q

def quickSelect(T, k, p, r):

    if p < r:

        q = partitionLomuto(T, p, r)
        if q == k:
            return T[q]
        elif q < k:
            return quickSelect(T, k, q + 1, r)
        else:
            return quickSelect(T, k, p, q - 1)
    # if p == q
    return T[p]


def ksum(T, k, p):
    n = len(T)
    sum = 0
    for i in range(n - p + 1):
        x = T[i:i + p]
        y = quickSelect(x, p - k, 0, p - 1)
        sum += y
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )