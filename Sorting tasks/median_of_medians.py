# kth order statistic

def insertionSort(T):
    n = len(T)

    for i in range(0, n - 1):
        if T[i+1] < T[i]:
            k = i + 1
            while k > 0 and T[k] < T[k-1]:
                T[k], T[k - 1] = T[k - 1], T[k]
                k -= 1

def median_of_medians(A, k):
    
    medians = []

    fives = [A[i:i+5] for i in range(0, len(A), 5)]
    #medians = [ insertionSort(arr)[len(arr)//2] for arr in fives]
    
    for arr in fives:
        insertionSort(arr)
        medians.append(arr[len(arr)//2])
    if len(medians) <= 5:
        insertionSort(medians)
        pivot = medians[len(medians)//2]
    else:
        q = median_of_medians(medians, len(medians)//2)

    left = [num for num in A if num < pivot]
    right = [num for num in A if num > pivot]

    x = len(left)

    if k == x:
        return pivot
    elif k < x:
        return median_of_medians(left, k)
    else:
        return median_of_medians(right, k - x - 1)
    