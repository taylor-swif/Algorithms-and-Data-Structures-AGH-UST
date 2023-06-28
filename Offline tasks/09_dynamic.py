from zad9testy import runtests

def min_cost( O, C, T, L ):
 
    oc = list(zip(O, C))
    oc.append((0,0))
    oc.append((L, 0))
    oc.sort()
    n = len(oc)
    f0 = [float('inf') for _ in range(n)]
    f1 = [float('inf') for _ in range(n)]
    f0[0] = 0
    f1[0] = 0

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if oc[i][0] - oc[j][0] <= T:
                f0[i] = min(f0[i], f0[j] + oc[i][1])
                f1[i] = min(f1[i], f1[j] + oc[i][1])
            elif T < oc[i][0] - oc[j][0] <= 2*T:
                f1[i] = min(f1[i], f0[j] + oc[i][1])
            else:
                break
                
    return f1[n-1]

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

# print(min_cost(O, C, T, L)) 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
