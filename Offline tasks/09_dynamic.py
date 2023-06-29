from zad9testy import runtests

# n^2
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

def min_cost_nlogn( O, C, T, L ):
 
    oc = [(o, c) for o, c in zip(O, C)]
    oc.append((0, 0))
    oc.append((L, 0))
    oc.sort()

    n = len(oc)
    F0 = [float('inf') for _ in range(n)]
    F1 = [float('inf') for _ in range(n)]
    F0[0], F1[0] = 0, 0
    
    Q0 = PriorityQueue()
    Q1 = PriorityQueue()
    Q1_2T = PriorityQueue()
    
    Q0.put((0, 0))
    Q1.put((0, 0))
    Q1_2T.put((0, 0))
    
    for i in range(1, n):

        while True:
            m1 = Q1.get()
            if oc[i][0] - m1[1] <= T:
                break
        Q1.put(m1)        

        while True:
            m1_2T = Q1_2T.get()
            if oc[i][0] - m1_2T[1] <= 2*T:
                break
        Q1_2T.put(m1_2T)

        while True:
            m0 = Q0.get()
            if oc[i][0] - m0[1] <= T:
                break
        Q0.put(m0)

        F0[i] = m0[0] + oc[i][1]
        F1[i] = min(m1[0], m1_2T[0]) + oc[i][1]

        Q0.put((F0[i], oc[i][0]))
        Q1_2T.put((F0[i], oc[i][0]))
        Q1.put((F1[i], oc[i][0]))

    # print(F0)
    # print(F1)

    return F1[n-1]

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

# print(min_cost(O, C, T, L)) 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
