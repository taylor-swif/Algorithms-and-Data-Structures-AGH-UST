# Public transport in a certain city is quite strangely organized. There is a separate charge for
# each section between two stations. However, the total cost incurred from the start of the journey
# is subtracted from this amount (if it is negative you just pay nothing). We are given a connection
# graph in any representation (undirected, weighted). Find the minimum cost of driving this route.

from queue import PriorityQueue

def weird_fees(G, s):
    n = len(G)  
    d = [float('inf') for v in range(n)]
    
    Q = PriorityQueue()
    d[s] = 0
    Q.put((0, s))

    def relax(u, v, weight):
        if weight - d[u]< 0:
            actual_weight = 0
        else:
            actual_weight = weight - d[u]
        
        if d[v] > d[u] + actual_weight:
            d[v] = d[u] + actual_weight
            return True
        return False
    
    while not Q.empty():
        _, u = Q.get()
        
        for v, weight in G[u]:
            if relax(u, v, weight):
                Q.put((d[v], v))
    return d



graph = [[(1, 60), (3, 120), (4, 40)],
         [(0, 60), (2, 80)],
         [(1, 80), (4, 100), (7, 70)],
         [(0, 120), (6, 150)],
         [(0, 40), (2, 100), (5, 90)],
         [(4, 90), (6, 60)],
         [(3, 150), (5, 60), (7, 90)],
         [(2, 70), (6, 90)]]
print(weird_fees(graph, 0))