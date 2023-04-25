# finding 4-length cycle in undirected graph
# graph is given as adjacency matrix

def cycle4(G):
    n = len(G)
    for i in range(n):
        for j in range(i + 1, n):
            counter = 0
            for k in range(n):
                if G[i][k] and G[j][k]:
                    counter += 1
            if counter >= 2:
                return True
    return False
