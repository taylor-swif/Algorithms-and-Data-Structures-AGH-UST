# bipartite graph (or bigraph) is a graph whose vertices
# can be divided into two disjoint and independent sets 

from queue import Queue

#G = [[1, 4], [0, 2], [1, 3, 5], [2, 4, 6], [0, 3, 5], [2, 4], [3, 7], [6]]
#G = [[3, 4, 5, 6], [3, 4, 5, 6], [4, 5, 6], [0, 1], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
def is_biparie(G, s):
    n = len(G)
    Q = Queue(0)
    color = [-1 for v in range(n)]

    Q.put(s)
    color[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if color[v] == -1:
                color[v] = (color[u] + 1)%2
                Q.put(v)
            else:
                if color[v] == color[u]:
                    return False
    return True
#print(is_biparie(G, 0))