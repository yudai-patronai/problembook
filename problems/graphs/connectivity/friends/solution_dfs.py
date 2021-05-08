def dfs(G, u, visited):  # стандартный dfs для матрицы смежности
    visited[u] = True
    for v, w in enumerate(G[u]):
        if w and not visited[v]:
            dfs(G, v, visited)


V, S = map(int, input().split())
G = [[0] * V for _ in range(V)]
for u in range(V):
    row = map(int, input().split())
    for v, w in enumerate(row):
        if w:  # запись только "гарантированной" дружбы
            G[u][v] = G[v][u] = w  # дружба работает в обе стороны

visited = [False] * V
dfs(G, S, visited)
print(sum(visited) - 1)
