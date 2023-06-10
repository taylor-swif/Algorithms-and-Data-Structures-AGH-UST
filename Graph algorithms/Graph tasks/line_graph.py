
# G - graph
# m - number of edges
# input has to be sorted
# The line graph made of the  edges of another graph
def line_graph(G, m):
    n = len(n)
    GE = [[] for _ in range(m)]

    i = 0
    for v in range(n):
        for u in G[v]:
            edge = (v, u, i)
            i += 1
            for w in G[u]:
                if v == w:
                    continue

