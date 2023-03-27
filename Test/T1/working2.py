from kol1btesty import runtests

def countString(T, pos):
    n = len(T[0])
    C = [0]*26
    B = [0]*len(T)

    for i in range(len(T)):
        C[ord(T[i][n - 1 - pos]) - 97] += 1
    
    for i in range(1, 26):
        C[i] += C[i - 1]

    for i in range(len(T) - 1, -1, -1):
        B[C[ord(T[i][n - 1 - pos]) - 97] - 1] = T[i]
        C[ord(T[i][n - 1 - pos]) - 97] -= 1
    for i in range(len(T)):
        T[i] = B[i]
    
    

def radixString(T):
    n = len(T[0])

    pos = 0
    while n - 1 - pos >= 0:
        countString(T, pos)
        pos += 1


    max_power = 0
    curr_power = 1
    last = T[0]

    for i in range(1,len(T)):
        if last == T[i]:
            curr_power += 1
            if curr_power > max_power:
                max_power = curr_power
        else:
            curr_power = 1
            last = T[i]

    return max_power

def sortLen(T):
    n = len(T)

    max_len = -1

    for str in T:
        if len(str) > max_len:
            max_len = len(str)
    
    C = [0]*(max_len+1)
    B = [0]*n

    for str in T:
        C[len(str)] += 1

    for i in range(1, max_len+1):
        C[i] += C[i - 1]
    
    for i in range(n - 1, -1, -1):
        B[C[len(T[i])] - 1] = T[i]
        C[len(T[i])] -= 1

    for i in range(n):
        T[i] = B[i]

def countingStringSort(s):
    n = len(s)
    C = [0]*26
    new_word = ""

    for i in range(n):
        C[ord(s[i]) - 97] += 1
    
    for i in range(26):
        new_word += C[i]*chr(i + 97)
    return new_word


def f(T):
    n = len(T)

    sortLen(T)

    A = []
    curr_len = len(T[0])

    res = 0

    for i in range(n):
        T[i] = countingStringSort(T[i])
        if curr_len == len(T[i]):
            A.append(T[i])
        else:
            if len(A) > res:
                curr_res = radixString(A)
                if curr_res > res:
                    res = curr_res
            curr_len = len(T[i])
            A = [T[i]]

    if len(A) > res:
        curr_res = radixString(A)
        if curr_res > res:
            res = curr_res
    
    return res

#print(f(["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]))

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )