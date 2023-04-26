

def square(G):
    n = len(G)
    G_new = [[0 for v in range(n)] for v in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                G_new[i][j] = 1
    print(G_new)

    for i in range(n):
        for j in range(n):
            if i == j or G[i][j] == 0:
                continue
            for k in range(n):
                if G[j][k] == 1:
                    G_new[i][k] = 1

    print(G_new)

G = [[3], [0, 5], [], [], [], [2, 4, 6], [0]]
# def to_matrix(G):
n = len(G)
G_new = [[0 for v in range(n)] for v in range(n)]
for i in range(n):
    for j in range(len(G[i])):
        G_new[i][G[i][j]] = 1
G = G_new

# to_matrix(G)
# print(G)
square(G)