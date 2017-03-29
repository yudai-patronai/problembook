#!/usr/bin/env python3


def read_graph_weight(n, m):
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    return graph


def read_task():
    task = list(map(int, input().split()))
    task.append(read_graph_weight(task[0], task[1]))
    return task


def dijkstra_n2_set(graph, centers):
    n = len(graph)
    district = [-1] * n  # область
    dist = [float('+inf')] * n
    queue = set()

    for x in centers:
        district[x] = x
        dist[x] = 0
        queue.add(x)

    while queue:
        min_dist = float('+inf')
        for j in queue:
            if dist[j] < min_dist:
                min_dist = dist[j]
                v = j

        queue.remove(v)

        for v2, r in graph[v]:
            if dist[v2] > dist[v] + r:
                dist[v2] = dist[v] + r
                district[v2] = district[v]
                queue.add(v2)

    return district


if __name__ == "__main__":
    n, m, *centers, graph = read_task()
    district = dijkstra_n2_set(graph, centers)
    print('\n'.join(map(str, district)))
