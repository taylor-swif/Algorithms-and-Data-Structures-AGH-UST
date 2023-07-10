from egz3atesty import runtests

def snow( T, I ):
    n = len(I)
    I = sorted(I, key= lambda x: x[0])
    # F = [1] * n
    maxx = 1
    for i in range(1, n):
        cnt = 1
        for j in range(i):
            if I[j][1] >= I[i][0]:
                # F[i] += 1
                cnt += 1
                if cnt > maxx:
                    maxx = cnt
    return maxx
# T = 100
# I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
# snow(T, I)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
