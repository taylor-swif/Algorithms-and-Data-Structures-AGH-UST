def heapify(T, i, n):
    max_i = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and T[l] > T[max_i]:
        max_i = l
    if r < n and T[r] > T[max_i]:
        max_i = r
    
    if max_i != i:
        T[max_i], T[i] = T[i], T[max_i]
        heapify(T, max_i, n)

def buildheap(T):
    n = len(T)
    
    for i in range((n-1)//2, -1, -1):
        heapify(T, i, n)

def heap_sort(T):
    n = len(T)
    buildheap(T)
    j = 0
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        if T[i] - j <= 0:
            break
        j += 1
        heapify(T, 0, i)
    
def snow( S ):
    sum = 0
    n = len(S)
    heap_sort(S)
    i = n-1
    j = 0
    while S[i] > 0 and i >=0:
        if S[i] - j > 0:
            sum = sum + S[i] - j
        else:
            break
        j += 1
        i -= 1

    return 


"""
A system that shows servers in a specific area requires a snow supplier.
A group of motivated professors found a gorge in the mountains from which you can bring snow. 
The ravine is divided to n areas and has entrances from the west and east. 
There is an external amount of snow in each area of the ravine, described in list S. 
For S[0] for the number of cubic meters of snow immediately at the western entrance, 
S[1] for the number of cubic meters of snow in the next area, and S[n −1] is the number 
of cubic meters of snow at the eastern entrance (it is known that the content is S is a natural 
number). Professors with a machine that can be the source of snow from the indicated area, 
entering from the west or east respectively. Unfortunately, there are three times
1. On the way to the area, the machines melts all the snow in the areas they pass through 
(unless it has already been collected). For example, approaching from the west to 
Area 2 resets S[0] and S[1] (because it drives over them) and S[2] (because it collects snow).
2. Each day's machine can only snow from one area, entering either from the west or the east.
3. Due to the high temperature, exactly one cubic meter of snow is melted at each point every day.
The task is to implement the function:
definitely snow (S)
which appears how many cubic meters can be used from the ravine 
(collected snow is protected and does not melt anymore).

Example:
input: S = [1,7,3,4,1]
output: 11

The solution is to sort an array and collect the biggest heaps of snow first. The complexity of the solution is O(nlogn)
"""