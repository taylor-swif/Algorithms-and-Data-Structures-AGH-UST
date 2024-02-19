from kol1btesty import runtests

def count_letters_in_word(word):
    result = [0]*26
    for character in word:
        result[ord(character) - 97] +=1
    return result

def find_max(A):
    n = len(A)
    max_val = 0
    for i in range(26):
        for j in range(n):
            if(A[j][i] > max_val):
                max_val = A[j][i]
    return max_val 
    
def counting_sort(A, i, k):
    n = len(A)
    C = [0]*(k+1)
    B = [0]*n

    for j in range(n):
        C[(A[j][i])] = C[(A[j][i])]+1

    for j in range(1,k):
        C[j] += C[j-1]
    
    for j in range(n-1, -1, -1):
        B[C[A[j][i]]-1] = A[j]
        C[A[j][i]]-=1
    for j in range(n):
        A[j] = B[j]

def f(T):
    to_sort_array = [count_letters_in_word(word) for word in T]
    max_k = find_max(to_sort_array)
    for i in range(26-1,-1,-1):
        counting_sort(to_sort_array,i,max_k+1)

    max_len = 1
    curr_len = 1
    for i in range(1, len(to_sort_array)):
        if(to_sort_array[i] == to_sort_array[i-1]):
            curr_len += 1
        else:
            if(curr_len>max_len):
                max_len = curr_len
            curr_len = 1
    return max(max_len,curr_len)


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
# print(f(["tygrys", "kot", "wilk","trysyg", "wlik", "sygryt","tygrys", "likw"]))
runtests( f, all_tests=True )