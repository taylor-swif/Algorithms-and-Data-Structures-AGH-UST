def heapify(T, i, n):
    r = 2*i + 2
    l = 2*i + 1

    max_i = i

    if l < n and T[max_i] < T[l]:
        max_i = l
    if r < n and T[max_i] < T[r]:
        max_i = r
    if max_i != i:
        T[max_i], T[i] = T[i], T[max_i]
        heapify(T, max_i, n)

def buildheap(T):
    n = len(T)
    for i in range((n-1)//2, -1, -1):
        heapify(T, i, n)

def heapSort(T):
    n = len(T)
    buildheap(T)
    for i in range(n-1, -1, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)

def reverse(s):
    n = len(s)
    if s[0] > s[n-1]:
        return s[::-1]
    else:
        return s
    
def strong_string(T):
    n = len(T)
    for i in range(n):
        T[i] = reverse(T[i])
    heapSort(T)


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
'''Two strings are said to be equivalent if they are either identical or would be identical if one of them were written backwards. For example, "cat" and "tok" are equivalent, as are "dog" and "dog". Given is an array T containing n strings of total length N (each string contains at least one character, so N ≥ n; in practice, it can be assumed that N ≫ n; each string consists only of lowercase Latin letters). The strength of the string T[i] is the number of indices j such that the strings T[i] and T[j] are equivalent. The T[i] string is the strongest if no other string is stronger.
Please implement the strong string(T) function, which returns the strength of the strongest string from the array T. For example, for the input:
#0123456
T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
a call to strong string(T) should return 3. The algorithm should be as fast as possible.
The problem can be solved in O(N + n log n) time, where N is the total length of the strings in the input array and n is the number of words.'''
'''
Mówimy, że dwa napisy są sobie równoważne, jeśli albo są identyczne, albo byłyby identyczne, gdyby jeden z nich zapisać od tyłu. Na przykład napisy “kot” oraz “tok” są sobie równoważne, podobnie jak napisy “pies” i “pies”. Dana jest tablica T zawierająca n napisów o łącznej długości N (każdy napis zawiera co najmniej jeden znak, więc N ≥ n; w praktyce można przyjąć, że N ≫ n; każdy napis składa się wyłącznie z małych liter alfabetu łacińskiego). Siłą napisu T[i] jest liczba indeksów j takich, że napisy T [i] oraz T [j] są sobie równoważne. Napis T [i] jest najsilniejszy, jeśli żaden inny napis nie ma większej siły.
Proszę zaimplementować funkcję strong string(T), która zwraca siłę najsilniejszego napisu z tablicy T. Na przykład dla wejścia:
#0123456
T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
wywołanie strong string(T) powinno zwrócić 3. Algorytm powinien być możliwie jak najszybszy.
Zadanie można rozwiązać w czasie O(N + n log n), gdzie N to łączna długość napisów w tablicy wejściowej a n to liczba wyrazów.'''