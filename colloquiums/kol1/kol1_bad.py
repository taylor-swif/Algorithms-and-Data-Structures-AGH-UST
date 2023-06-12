# Kamil Kawula
# Algorytm dziala w taki sposob, ze tworze n-p tablic zawierajacych odpowiednie elementy z kolejnych przedzialow danej tablicy, nastepnie ją sortuje i wybieram k-ty najwiekszy element, pozniej sumuje wybrane elemnty, algorytm jest poprawny, poniewaz z posortowanej tablicy zawsze dobrze wybiore k-ty najwiekszy element
# Zlozonosc czasowa to O(np), poniewaz sortuje liniowo, zlozonosc pamieciowa to O(n), poniewaz uzywam sortowania radix
from kol1testy import runtests


def countingSort(T, pos, n):
    C = [0]*11
    B = [0]*n

    for i in range(n):
        C[T[i]//pos%10] += 1

    for i in range(1, 10):
        C[i] += C[i-1]
    
    for i in range(n-1,-1,-1):
        B[C[T[i]//pos%10] - 1] = T[i]
        C[T[i]//pos%10] -= 1
    for i in range(n):
        T[i] = B[i]


def radix(T, n):
    max_num = -1
    for i in range(n):
        if T[i] > max_num:
            max_num = T[i]

    pos = 1
    while max_num // pos > 0:
        countingSort(T, pos, n)
        pos *= 10


def ksum(T, k, p):
    n = len(T)
    sum = 0
    for i in range(n - p + 1):
        A = T[i:i+p]
        radix(A, len(A))
        sum += A[p-k]
    
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )