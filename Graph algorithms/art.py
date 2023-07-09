def tarjan(G):
    n = len(G)

    visited = [False for v in range(n)]
    parent = [False for v in range(n)]
    time_arr = [0 for v in range(n)]
    low = [0 for v in range(n)]
    arts = []

    time = 0

    def tarjan_dfs(u, is_root):
        nonlocal time
        children = 0

        visited[u] = True
        time_arr[u] = time
        low[u] = time
        time += 1
        is_art = False

        for v in G[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                tarjan_dfs(v, False)
                low[u] = min(low[u], low[v])

                if is_root and not is_art and children >= 2:
                    is_art = True
                    arts.append(u)

                if not is_root and not is_art and low[v] >= time_arr[u]:
                    is_art = True
                    arts.append(u)
            elif v != parent[u]:
                low[u] = min(low[u], time_arr[v])

    # for v in range(num_vertices):
    #     if not visited[v]:
    tarjan_dfs(0, True)

    return arts

# Przykładowy graf jako lista sąsiedztwa

G = [[1, 2], [0, 4], [0, 3, 4], [2], [1, 2, 5], [4, 6, 7], [5, 7], [5, 6]]

arts = tarjan(G)
print("Punkty artykulacji:", arts)
