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

def djikstra_rabunek(G, s, r):
  n = len(G)
  dist = [float('inf') for _ in range(n)]
  done = [False for _ in range(n)]
  dist[s] = 0
  Q = PriorityQueue()
  Q.put((0, s))

  while not Q.empty():
    w, v = Q.get()

    for u, w_u in G[v]:
      if not done[u] and dist[u] > w_u *  2 + r + dist[v]:
        dist[u] = w_u * 2 + r + dist[v]
        Q.put((dist[u], u))
    done[v] = True
  
  return dist


def gold(G,V,s,t,r):
  n = len(G)
  dist = djikstra(G, s)
  min_cost = dist[t]
  dist_po = djikstra_rabunek(G, t, r)

  for v in range(n):
    cost = dist[v] - V[v] + dist_po[v]
    min_cost = min(cost, min_cost)

  return min_cost
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )