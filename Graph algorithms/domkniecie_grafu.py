def domkniecie(G):
    n = len(G)
    for t in range(n):
        for x in range(n):
            for y in range(n):
                G[x][y] |= G[x][t] & G[t][y]
    return G

def to_matrix(G):
    n = len(G)
    new = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for v in G[i]:
            new[i][v] = new[v][i] = 1
    for row in new:
        print(row)
    return new

G = [[1], [2], [3], []]
G = to_matrix(G)
G = domkniecie(G)
for row in G:
    print(row)