from queue import PriorityQueue

def trip(G, A, B):
    n = len(G)
    d = [[float('inf'), float('inf'), float('inf')] for _ in range(n)]
    Q = PriorityQueue()
    
    for i in range(3):
        d[A][i] = 0

    def relax(u, v, cost):
        if cost == 1:
            if d[v][0] > d[u][1] + cost:
                d[v][0] = d[u][1] + cost
                Q.put((d[v][0], v, 1))
            if d[v][0] > d[u][2] + cost:
                d[v][0] = d[u][2] + cost
                Q.put((d[v][0], v, 1))
        
        if cost == 5:
            if d[v][1] > d[u][0] + cost:
                d[v][1] = d[u][0] + cost
                Q.put((d[v][1], v, 5))
            if d[v][1] > d[u][2] + cost:
                d[v][1] = d[u][2] + cost
                Q.put((d[v][1], v, 5))
        if cost == 8:
            if d[v][2] > d[u][0] + cost:
                d[v][2] = d[u][0] + cost
                Q.put((d[v][2], v, 8))
            if d[v][2] > d[u][1] + cost:
                d[v][2] = d[u][1] + cost
                Q.put((d[v][2], v, 8))

    Q.put((0, A, 0))
    
    while not Q.empty():
        weight, u, prev = Q.get()
        for v in range(n):
            if G[u][v] > 0 and G[u][v] != prev:
                relax(u, v, G[u][v])

    print(d)
    return d[B]

G = [ 
[0,5,1,8,0,0,0],
[5,0,0,1,0,8,0],
[1,0,0,8,0,0,8],
[8,1,8,0,5,0,1],
[0,0,0,5,0,1,0],
[0,8,0,0,1,0,5],
[0,0,8,1,0,5,0] ]

print(trip(G, 5, 2))