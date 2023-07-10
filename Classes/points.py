# pokrycie przedziałami jednostkowymi. Dany jest zbior punktow na prostej. Prosze podac algorytm, ktory znajduje minimalna liczbe przedzialow jednostkowych domknietych,
# potrzebnych do pokrycia wszystkich punktow z X. 
# Przyklad: jesli X = (0.25, 0.5, 1.6) to potrzeba dowch przedzialow, np. [0.2, 1.2] oraz [1.4, 2.4]



def points(A):
    n = len(A)
    A.sort()
    cnt = 0
    start = 0
    buckets = [[A[0]]]
    for i in range(1, n):
        if A[i] - A[start] <= 1:
            buckets[cnt].append(A[i])
            continue
        else:
            start = i
            cnt += 1
            buckets.append([A[start]])
            
    print(buckets)

    return cnt + 1
    

A = [0.25, 0.5, 1.6, 1.7, 5,5,5,5, 100]
print(points(A))
