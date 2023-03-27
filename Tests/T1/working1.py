from kol1btesty import runtests

def countingSortString(s):
    n = len(s)
    C = [0]*26
    new_word = ""

    for i in range(n):
        C[ord(s[i])-97] += 1

    for i in range(26):
        if C[i] > 0:
            new_word += chr(i + 97)*C[i]
        
    return new_word

def countingSort(T, pos):
    n = len(T)
    C = [0]*10
    B = [0]*n

    for i in range(n):
        C[T[i][1]//pos%10] += 1
    
    for i in range(1,10):
        C[i] = C[i] + C[i - 1]

    for i in range(n-1, -1, -1):
        B[C[T[i][1]//pos%10] - 1] = T[i]
        C[T[i][1]//pos%10] -= 1

    for i in range(0, n):
        T[i] = B[i]

def radixSort(T):

    max_element = 0
    for i in range(len(T)):
        if T[i][1] > max_element:
            max_element = T[i][1]

    pos = 1
    while max_element // pos > 0:
        countingSort(T, pos)
        pos *= 10

def countingSortNew(T, pos, a, b, l):
    n = b - a + 1
    C = [0]*26
    B = [0]*n

    for i in range(a, b + 1):

        C[ord(T[i][0][l-1-pos])-97] += 1
        
    
    for i in range(1,26):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        y = T[i + a][0]
        z = T[i + a][0][l-1-pos]
        x = ord(T[i+ a][0][l-1-pos])-97
        B[C[ord(T[i + a][0][l-1-pos])-97] - 1] = T[i + a]
        C[ord(T[i + a][0][l-1-pos])-97] -= 1

    #print("A",T)
    for i in range(n):
        T[i+a] = B[i]
    #print("B",T)

def radixSortNew(T):
    n = len(T)

    lens =[]

    i = 0
    while i < n:
        start = i
        dl = T[i][1]
        while i < n and T[i][1] == dl:
            i += 1
        stop = i - 1
        lens.append((start, stop, dl))
    
    for el in lens:
        pos = 0
        while el[2]  > pos:
            countingSortNew(T, pos, el[0], el[1], el[2])
            pos += 1
        



def f(T):
    n = len(T)
    for i in range(n):
        T[i] = (countingSortString(T[i]), len(T[i]))
    radixSort(T)
    radixSortNew(T)

    max_power = 0
    curr_power = 1
    last = T[0]

    for i in range(1,n):
        if last == T[i]:
            curr_power += 1
            if curr_power > max_power:
                max_power = curr_power
        else:
            curr_power = 1
            last = T[i]

    return max_power
T = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
#print(f(T))
# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
