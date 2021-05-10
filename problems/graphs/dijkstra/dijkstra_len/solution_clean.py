import heapq


def dijkstra_distance(G, start, end):
    inf = float('inf')
    visited = {u: False for u in G}
    distance = {u: inf for u in G}

    distance[start] = 0
    pqueue = [(distance[u], u) for u in G]
    heapq.heapify(pqueue)

    while pqueue:
        distmin, umin = heapq.heappop(pqueue)
        if visited[umin]:
            continue
        if distmin == inf:
            break
        for v, w in G[umin]:
            if distance[v] > distance[umin] + w:
                distance[v] = distance[umin] + w
                heapq.heappush(pqueue, (distance[v], v))
        visited[umin] = True
    return distance[end]


V, E, start, end = map(int, input().split())
G = {u: set() for u in range(V)}
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].add((v, w))
    G[v].add((u, w))

d = dijkstra_distance(G, start, end)
print(d)
