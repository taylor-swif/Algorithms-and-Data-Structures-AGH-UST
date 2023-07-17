from egz1Atesty import runtests
from queue import PriorityQueue

def djikstra(G, s):
  n = len(G)
  dist = [float('inf') for _ in range(n)]
  done = [False for _ in range(n)]
  dist[s] = 0
  Q = PriorityQueue()
  Q.put((0, s))

  while not Q.empty():
    w, v = Q.get()

    for u, w_u in G[v]:
      if not done[u] and dist[u] > w_u + dist[v]:
        dist[u] = w_u + dist[v]
        Q.put((dist[u], u))
    done[v] = True
  
  return dist


def gold(G,V,s,t,r):
  n = len(G)
  dist = djikstra(G, s)
  new_G = [[] for _ in range(n)]
  for i in range(n):
    for j in range(len(G[i])):
      new_G[i].append((G[i][j][0], G[i][j][1] * 2 + r))
  min_cost = dist[t]

  for v in range(n):
    cost = dist[v] - V[v]
    dist_po = djikstra(new_G, v)
    cost += dist_po[t]
    min_cost = min(cost, min_cost)

  
  return min_cost

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = False )
