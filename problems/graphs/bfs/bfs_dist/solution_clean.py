from collections import deque


def bfs_distance(G, start, end):
    dist = {u: -1 for u in G}
    
    queue = deque([start])
    dist[start] = 0
    while queue:
        u = queue.pop()
        for v in G[u]:
            if dist[v] == -1:  # not visited vertex
                dist[v] = dist[u] + 1
                queue.appendleft(v)
            if v == end:
                return dist[end]
    return None


V, E, start, end = map(int, input().split())
G = {u: set() for u in range(V)}
for _ in range(E):
    u, v = map(int, input().split())
    G[u].add(v)
    G[v].add(u)

distance = bfs_distance(G, start, end)
print(distance)
