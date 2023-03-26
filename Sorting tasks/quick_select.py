# kth order statistic

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
            print(q)
            print(T)
            return T[q]
        elif q < k:
            return quickSelect(T, k, q + 1, r)
        else:
            return quickSelect(T, k, p, q - 1)




    