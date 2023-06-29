# Given is a chessboard A of dimensions n × n. The chessboard contains rational numbers. 
# Move from square (1,1) to square (n, n) using only "down" and "right" moves. 
# Entry to a field costs as much as the number there. Please provide an algorithm
# finding the minimum cost route.

def chess(C):
    rows = len(C)
    cols = len(C[0])

    dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = C[0][0]
    #filling the first row
    for i in range(1, cols):
        dp[0][i] = dp[0][i - 1] + C[0][i]

    #filling the first col
    for i in range(1,cols):
        dp[i][0] = dp[i - 1][0] + C[i][0]
    
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + C[i][j]

    print(*dp, sep="\n")

    return dp[rows - 1][cols - 1]

C = [
    [3, 4, 5, 2, 1],
    [7, 2, 13, 7, 8],
    [3, 1, 4, 1, 5],
    [2, 8, 11, 1, 3],
    [3, 5, 1, 3, 2]
]
print(chess(C))