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
                    articulation_points.append(u)

                if not is_root and not is_art and low[v] >= time_arr[u]:
                    is_art = True
                    articulation_points.append(u)
            elif v != parent[u]:
                low[u] = min(low[u], time_arr[v])

    # for v in range(num_vertices):
    #     if not visited[v]:
    tarjan_dfs(0, True)

    return articulation_points

# Przykładowy graf jako lista sąsiedztwa
G = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}

articulation_points = tarjan(G)
print("Punkty artykulacji:", articulation_points)
