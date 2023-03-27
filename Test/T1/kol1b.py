from kol1btesty import runtests
from math import log10

def countingStringSort(s):
    n = len(s)
    C = [0]*26
    new_word = ""

    for i in range(n):
        C[ord(s[i]) - 97] += 1
    
    for i in range(26):
        new_word += C[i]*chr(i + 97)
    return new_word

def countingSort(T, pos):
    n = len(T)
    C = [0]*10
    B = [0]*n

    for i in range(n):
        C[T[i][1]//pos%10] += 1
    
    for i in range(1,10):
        C[i] += C[i - 1]

    for i in range(n-1, -1, -1):
        B[C[T[i][1]//pos%10] - 1] = T[i]
        C[T[i][1]//pos%10] -= 1
    
    for i in range(n):
        T[i] = B[i]
    # print(T)

def radixSort(T):
    n = len(T)

    max_len = 0
    for el in T:
        if el[1] > max_len:
            max_len = el[1]

    pos = 1
    while 10**(int(log10(max_len)) + 1) // pos > 0:
        countingSort(T, pos)
        pos *= 10
def countString(T, pos):
    n = len(T[0][0])
    C = [0]*26
    B = [0]*len(T)

    for i in range(len(T)):
        C[ord(T[i][0][n - 1 - pos]) - 97] += 1
    
    for i in range(1, 26):
        C[i] += C[i - 1]

    for i in range(len(T) - 1, -1, -1):
        B[C[ord(T[i][0][n - 1 - pos]) - 97] - 1] = T[i]
        C[ord(T[i][0][n - 1 - pos]) - 97] -= 1
    for i in range(len(T)):
        T[i] = B[i]
    
    

def radixString(T):
    #print(T)
    n = len(T[0][0])

    pos = 0
    while n - 1 - pos >= 0:
        countString(T, pos)
        pos += 1

    #finding max
    
    max_power = 0
    curr_power = 1
    last = T[0][0]

    for i in range(1,len(T)):
        if last == T[i][0]:
            curr_power += 1
            if curr_power > max_power:
                max_power = curr_power
        else:
            curr_power = 1
            last = T[i][0]

    return max_power

def f(T):
    n = len(T)

    for i in range(n):
        T[i] = (countingStringSort(T[i]), len(T[i]))
    radixSort(T)
    i = 0
    max_odp = 0
    # while i < n-1:
    #     start = i
    #     while T[i][1] == T[i+1][1]:
    #         i += 1
    #     stop = i
    #     #print(start, stop)
    #     A = T[start:stop + 1]
    #     #print(A)
    #     x = radixString(A)
    #     if x > max_odp:
    #         max_odp = x

    i = 0
    while i < n:
        start = i
        dl = T[i][1]
        while i < n and T[i][1] == dl:
            i += 1
        stop = i - 1
        # print(start, stop)
        A = T[start:stop + 1]
        # print(A)
        x = radixString(A)
        if x > max_odp:
            max_odp = x

    return max_odp
        

print(f(["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]))

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )