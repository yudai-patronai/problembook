#!/usr/bin/env python3


def read_graph_weight(n, m):
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    return graph


def read_task():
    n, m, *centers = list(map(int, input().split()))
    graph = read_graph_weight(n, m)
    return graph, centers


def dijkstra_n2_pop(graph, centers):
    n = len(graph)
    district = [-1] * n  # область
    dist = [float('+inf')] * n
    queue = []

    for x in centers:
        district[x] = x
        dist[x] = 0
        queue.append(x)

    while queue:
        min_i = 0
        for i in range(1, len(queue)):
            if dist[queue[i]] < dist[queue[min_i]]:
                min_i = i

        v = queue.pop(min_i)

        for v2, w in graph[v]:
            if dist[v2] > dist[v] + w:
                dist[v2] = dist[v] + w
                district[v2] = district[v]
                if v2 not in queue:
                    queue.append(v2)

    return district


if __name__ == "__main__":
    graph, centers = read_task()
    district = dijkstra_n2_pop(graph, centers)
    print('\n'.join(map(str, district)))
