# Dana jest tablica A[n] z dlugosciami samochodów, które stoja w kolejce, zeby wjechac na prom. Prom ma dwa pasy (lewy i prawy), oba dlugosci L. Prosze napisac program, który
# wyznacza, które samochody powinny pojechac na który pas, zeby na promie zmiescilo sie jak najwiecej aut.
# Auta musza wjezdzac w takiej kolejnosci, w jakiej sa podane w tablicy

def ferry_3d(T, L):
    n = len(T)

    dp = [[[0 for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n)]
    dp[0][0][T[0]] =1
    dp[0][T[0]][0] =1
    res = 0
    for i in range(1, n):
        for l in range(L + 1):
            for r in range(L + 1):
                if dp[i - 1][l][r] == 1:
                    if l + T[i] <= L:
                        dp[i][l + T[i]][r] = 1
                        res = i + 1
                    if r + T[i] <= L:
                        dp[i][l][r + T[i]] = 1
                        res = i + 1
    return res

def ferry_2d(T, L):
    n = len(T)
    
    sum = [0 for _ in range(n)]
    dp = [[0 for _ in range(L + 1)] for _ in range(n)] #opisuje ile długości mam na lewej stronie, gdy zaparkowane jest i samochodow
    
    sum[0] = T[0]
    for i in range(1, n):
        sum[i] = T[i] + sum[i - 1]

    dp[0][T[0]] = T[0]
    res = 0
    for i in range(1, n):
        for j in range(L + 1):
            if dp[i - 1][j]:
                s1 = j
                s2 = sum[i] - j
                if s1 + T[i] <= L:
                    dp[i][s1 + T[i]] = 1
                    res = i + 1
                if s2 + T[i] <= L:
                    dp[i][s2 + T[i]] = 1
                    res = i + 1
    return res


t = [30, 30, 50, 60, 70]
l = 100
# t=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# l = 4
# t = [2,1,4,2,3]
# l = 6
# t = [2,1,4,4,2,3]
# l = 6
print(ferry_3d(t, l))