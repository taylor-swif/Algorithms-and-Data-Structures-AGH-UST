from random import randint
from collections import deque
WALL = '#'
PATH = '.'
AFTER_PATH = ' '
WALK = '+'
def create_maze(m, n):
    maze = [[WALL for _ in range(m)] for n in range(n)]
    number_of_paths = int((m-2)*(n-2)*1.5)
    for _ in range(number_of_paths):
        i = randint(1, n-2)
        j = randint(1, m-2)
        maze[i][j] = PATH

    i = randint(1, n-2)
    j = randint(1, m-2)
    maze[i][j] = 'S'

    y = randint(1, n-2)
    x = randint(1, m-2)
    while (i, j) == (x, y):
        y = randint(1, n-2)
        x = randint(1, m-2)
    
    maze[y][x] = 'T'
    
    return maze


def print_maze(maze):
    for i in range(len(maze)):
        # print(maze[i])
        for j in range(len(maze[i])):
            print(maze[i][j], end="")
        print()

def find_S_and_T(maze):
    n = len(maze)
    m = len(maze[0])
    s_found = False
    t_found = False
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if maze[i][j] == 'S':
                s_i = i
                s_j = j
                s_found = True
            elif maze[i][j] == 'T':
                t_i = i
                t_j = j
                t_found = True

            if t_found and s_found:
                return s_i, s_j, t_i, t_j

def find_path(maze):
    row = len(maze)
    col = len(maze[0])
    s_i, s_j, t_i, t_j = find_S_and_T(maze)
    maze[t_i][t_j] = PATH

    Q = deque()
    Q.append((s_i, s_j))

    while len(Q) > 0:
        v = Q.popleft()
        if maze[t_i][t_j] != PATH:
            break
        if v[0] - 1 > 0 and maze[v[0] - 1][v[1]] == PATH:
            maze[v[0] - 1][v[1]] = 'd'
            Q.append((v[0] - 1,v[1]))

        if v[0] + 1  < row - 1 and maze[v[0] + 1][v[1]] == PATH:
            maze[v[0] + 1][v[1]] = 'g'
            Q.append((v[0] + 1,v[1]))


        if v[1] - 1 > 0 and maze[v[0]][v[1] - 1] == PATH:
            maze[v[0]][v[1] - 1] = 'p'
            Q.append((v[0], v[1] - 1))


        if v[1] + 1  < col - 1 and maze[v[0]][v[1] + 1] == PATH:
            maze[v[0]][v[1] + 1] = 'l'
            Q.append((v[0], v[1] + 1))

    if(maze[t_i][t_j] != PATH):
        i, j = t_i, t_j
        c = maze[i][j]

        while c != 'S':
            if c == 'd':
                maze[i][j] = WALK
                i += 1
            elif c == 'g':
                maze[i][j] = WALK
                i -= 1
            elif c == 'p':
                maze[i][j] = WALK
                j += 1
            elif c == 'l':
                maze[i][j] = WALK
                j -= 1
            c = maze[i][j]
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if maze[i][j] != WALK and maze[i][j] != WALL:
                maze[i][j] = AFTER_PATH
    maze[s_i][s_j] = 'S'
    maze[t_i][t_j] = 'T'

maze = create_maze(30, 30)
# print_maze(maze)
find_path(maze)
print_maze(maze)