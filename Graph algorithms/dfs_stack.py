from collections import deque



def DFS_stack(G):
    n = len(G)
    visited = [False for v in range(n)]
    time_arr = [-1 for v in range(n)]
    parent = [None for v in range(n)]

    time = 1
    stack = deque()

    def DFS_Visit(G):
        nonlocal stack, time

        while len(stack) > 0:

            v = stack.pop()
            time_arr[v] = time
            time += 1
            for u in G[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
    

    stack.append(0)
    visited[0] = True
    DFS_Visit(G)
    
    print(visited)
    # print(parent)
    print(time_arr)

G = [[1, 4], [0, 2], [1, 3, 5], [2, 4, 6], [0, 3, 5], [2, 4], [3, 7], [6]]
DFS_stack(G) 