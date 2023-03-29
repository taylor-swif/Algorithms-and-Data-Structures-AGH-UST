def binSearch(T, k, p, r):
    q = (p + r)//2
    if T[q] == k:
        return True
    if p == r:
        return False
    if T[q] < k:
        return binSearch(T, k, q + 1, r)
    else:
        return binSearch(T, k, p, q - 1)
    
T = [2, 3, 5, 7, 11, 13, 17]
num = 0 
while num != 69:
    num = int(input())
    print(binSearch(T, num, 0, len(T) - 1))