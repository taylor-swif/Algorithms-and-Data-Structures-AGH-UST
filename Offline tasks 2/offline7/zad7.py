from zad7testy import runtests

# def is_true(arr):
#     for i in range(len(arr)):
#         if not arr[i]:
#             return False
#     return True

# def dfs(G, ns):
#     n = len(G)
#     visited = [False for v in range(n)]
#     parent = [None for v in range(n)]
#     visited[0] = True
#     done = 0
#     def DFSVisit(G, s, ns):
#         nonlocal done
#         nonlocal parent
#         if done:
#             return
#         # print(s, G[s][not ns])
#         for v in G[s][not ns]:
            
#             if v == 0:
#                 # print("czek")
#                 # print(visited)
#                 if is_true(visited):
#                     parent[0] = s
#                     # print(parent)
#                     done = 1
#                     return
#             elif not visited[v]:
#                 visited[v] = True
#                 parent[v] = s
#                 # print(v)
#                 DFSVisit(G, v, ns)
#                 if done: 
#                     return
#                 visited[v] = False
#                 parent[v] = None

#     DFSVisit(G, 0, ns)
#     if done:
#         return parent
#     return None



# def droga(G):
#     parent = dfs(G, 0)
#     if parent == None:
#         parent = dfs(G, 1)
#         if parent == None:
#             return None
#     path = []
#     v = parent[0]
#     while v != 0:
#         path.append(v)
#         v = parent[v]
#     path.append(0)
#     return path[::-1]
def find_gate(G,vertex, miasto_z):
    for i in range(2):
        for j in range(len(G[vertex][i])):
            if(G[vertex][i][j] == miasto_z):
                return i
    return -1



global_answ = []
exit_gate=-1



def sol(G,vertex,answer,visited,come_from,n):
    global global_answ
    global exit_gate

    if(len(global_answ) == n):
        return
 
    if(come_from == -1):## przypadek początkowy
        for i in range(2):
            for j in range(len(G[vertex][i])):
                visited[G[vertex][i][j]] = True
                answer.append(G[vertex][i][j])
               # print(G[vertex][i][j])

                exit_gate= i
                sol(G,G[vertex][i][j],answer,visited,vertex,n)
                
                visited[G[vertex][i][j]] = False
                answer.pop() 
    
    
    else:
        gate = find_gate(G,vertex,come_from)



        gate_to_consider = (gate+1)%2


        #print("looped in recursion/? ", vertex)
        for i in range(len(G[vertex][gate_to_consider])):
        
            if(len(answer) == n and G[vertex][gate_to_consider][i] == 0):
                
                gate_at_start = find_gate(G,0,vertex)
                if(gate_at_start == exit_gate):
                    return
         
                global_answ = answer[:]
                return True

            if not visited[G[vertex][gate_to_consider][i]]:
            
                visited[G[vertex][gate_to_consider][i]] = True
                answer.append(G[vertex][gate_to_consider][i])

                sol(G,G[vertex][gate_to_consider][i],answer,visited,vertex,n)
    

                visited[G[vertex][gate_to_consider][i]] = False
                answer.pop()


    




def droga( G ):
    global global_answ
    global_answ = []
    ## liczba miast
    n = len(G)
    ## wjechano z bramy północnej, wjechano z bramy południowej
    visited = [False for i in range(n)]
    visited[0] = True

    answer = [0]

    path = [-1] * n
    path[0] = 0

    ## start
    sol(G,0,answer,visited,-1,n)

    #print(global_answ)

    
    if(len(global_answ) != n):
        global_answ = None




    # tu prosze wpisac wlasna implementacje
    return global_answ


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
# droga([([1], [3, 4, 6]), ([2], [0]), ([3], [1]), ([0, 4, 6], [2]), ([5], [3, 6, 0]), ([6], [4]), ([0, 3, 4], [5])])