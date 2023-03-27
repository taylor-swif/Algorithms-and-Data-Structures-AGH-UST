# useless, but working

def countingSort(T, pos):
    n = len(T)
    C = [0]*26
    B = [0]*n

    for i in range(n):
        if len(T[i]) - 1 >= pos:

            C[ord(T[i][len(T[i])-1-pos])-97] += 1
        else:
            C[0] += 1
        
    
    for i in range(1,26):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        if len(T[i])-1 >= pos:
            B[C[ord(T[i][len(T[i])-1-pos])-97] - 1] = T[i]
            C[ord(T[i][len(T[i])-1-pos])-97] -= 1
        else:
            B[C[0] - 1] = T[i]
            C[0] -= 1


    for i in range(0, n):
        T[i] = B[i]

def radixSort(T):

    max_len = 0
    for word in T:
        if len(word) > max_len:
            max_len = len(word)

    pos = 0
    while max_len + 1 > pos:
        countingSort(T, pos)
        pos += 1


