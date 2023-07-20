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
  dist = [[float('inf'), float('inf')] for _ in range(n)]
  Q = PriorityQueue()
  dist[s][0] = 0
  # dist[s][1] = -V[s]
  Q.put((0, s, 0))
  # Q.put((-V[s], s, 1))

  def relax(u, v, w, mode):
    nonlocal r

    if mode == 0:
      if dist[v][0] > dist[u][0] + w:
        dist[v][0] = dist[u][0] + w
        Q.put((dist[v][0], v, 0))

      if dist[v][1] > dist[u][0] + w - V[v]:
        dist[v][1] = dist[u][0] + w - V[v]
        Q.put((dist[v][1], v, 1))

    if mode == 1:
      if dist[v][1] > dist[u][1] + 2 * w + r:
        dist[v][1] = dist[u][1] + 2 * w + r
        Q.put((dist[v][1], v, 1))
    

  while not Q.empty():
    _, u, mode = Q.get()
    
    for v, w in G[u]:
      relax(u, v, w, mode)
      

  return min(dist[t][0], dist[t][1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )