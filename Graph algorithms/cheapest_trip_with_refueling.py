# We are given a graph, in which the vertices are cities and the edges are roads between them. We know
# the fuel price in per liter for each city and the length in kilometers for each road. Our car has
# a 100 liter tank and burns one liter per kilometer. We start from city_A with an empty tank. What is
# the minimum cost that we have to pay for fuel to get to the city_B?
import heapq

def cheapest_trip_with_refueling(G, cost, a, b, capacity):
    n = len(G)
    d = [[float('inf') for v in range(capacity + 1)] for v in range(n)]
    parent = [[None for v in range(capacity + 1)] for v in range(n)]
    
    heap = []
    heapq.heappush(heap, (0, a, 0))

    d[a][0] = 0


    def relax(fin, dist, start, gas, curr_tank):
        if d[fin][curr_tank + gas - dist] > d[start][curr_tank] + gas * cost[start]:
            d[fin][curr_tank + gas - dist] = d[start][curr_tank] + gas * cost[start]
            return True
        return False



    while heap:
        _, u, curr_tank = heapq.heappop(heap)

        for v, dist in G[u]:
            if dist <= capacity:
                for gas in range(0, capacity + 1):
                    if curr_tank + gas >= dist and curr_tank + gas <= capacity:
                        if relax(v, dist, u, gas, curr_tank):
                            parent[v][gas -dist] = u
                            heapq.heappush(heap, (d[v][curr_tank + gas - dist], v, curr_tank + gas - dist))
    
    print(parent)
    return min(d[b])


G =[
    [(1,7),(3,10),(5,30)],
    [(0,7),(3,8),(2,14)],
    [(1,14),(3,9),(4,15)],
    [(0,10),(1,8),(2,9),(4,20),(5,5)],
    [(2,15),(3,20),(5,15)],
    [(0,30),(3,5),(4,15)]
]

cost = [20,3,100,5,5,10]

print(cheapest_trip_with_refueling(G, cost, 0, 5, 30))