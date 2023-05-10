from math import inf


def floyd_warshall(G):
    n = len(G)
    d = [[inf]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                d[i][i] = 0
                continue
            d[i][j] = G[i][j]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    return d


G = [[0, 5, 2, 3, inf, inf],
    [5, 0, 1, inf, 2, inf],
    [2, 1, 0, 4, inf, 7],
    [3, inf, 4, 0, inf, 0],
    [inf, 2, inf, inf, 0, inf],
    [inf, inf, 7, 0, inf, 0]]

d = floyd_warshall(G)
for row in d:
    print(row)
