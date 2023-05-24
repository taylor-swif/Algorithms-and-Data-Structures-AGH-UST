def is_euler(G):
    n = len(G)

    for i in range(n):
        counter = 0
        for j in range(n):
            counter += G[i][j]
        if counter % 2 == 1:
            return 0

    return 1

def euler_cycle(G):
    if not is_euler(G):
        return None
    
    n = len(G)
    
    path = []

    def DFSVisit(G, s):
        for i in range(len(G[s])):
            if G[s][i] == 1:
                G[s][i] = 0
                G[i][s] = 0
                DFSVisit(G, i)
        path.append(s)
    
    DFSVisit(G, 0)
    return path

print(euler_cycle([[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]))

