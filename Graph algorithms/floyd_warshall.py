from math import inf
def floyd_warshall(G):
    n = len(G)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][i] = 0
                continue
            dp[i][j] = G[i][j]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][t] + dp[t][j] < dp[i][j]:
                    dp[i][j] = dp[i][t] + dp[t][j]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][t] + dp[t][j] < dp[i][j]:
                    dp[i][j] = float('-inf')

    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if dp[i][j] > dp[i][k] + dp[k][j]:
    #                 dp[i][j] = dp[i][k] + dp[k][j]

    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if dp[i][j] > dp[i][k] + dp[k][j]:
    #                 dp[i][j] = float('-inf')
    #                 # return False
    
    return dp

# G = [[0, 5, 2, 3, inf, inf],
#     [5, 0, 1, inf, 2, inf],
#     [2, 1, 0, 4, inf, 7],
#     [3, inf, 4, 0, inf, 0],
#     [inf, 2, inf, inf, 0, inf],
#     [inf, inf, 7, 0, inf, 0]]
E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
G = [[inf, 5, inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, 20, inf, inf, 30, 60, inf, inf, inf], [inf, inf, inf, 10, 75, inf, inf, inf, inf, inf], [inf, inf, -15, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf, inf, 100], [inf, inf, inf, inf, 25, inf, 5, inf, 50, inf], [inf, inf, inf, inf, inf, inf, inf, -50, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf, -10, inf], [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]]
INF = inf
graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]
W = floyd_warshall(G)
print(*W, sep='\n', end='\n\n')

W = floyd_warshall(graph)
print(*W, sep='\n', end='\n\n')

