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


def dijkstra_n2_marks(graph, centers):
    n = len(graph)
    district = [-1] * n  # область
    dist = [float('+inf')] * n
    in_progress = [True] * n

    for x in centers:
        district[x] = x
        dist[x] = 0

    for i in range(n):
        v = 0
        for j in range(1, n):
            if in_progress[j] and dist[j] < dist[v]:
                v = j

        in_progress[v] = False

        for v2, r in graph[v]:
            if dist[v2] > dist[v] + r:
                dist[v2] = dist[v] + r
                district[v2] = district[v]

    return district


if __name__ == "__main__":
    n, m, *centers, graph = read_task()
    district = dijkstra_n2_marks(graph, centers)
    print('\n'.join(map(str, district)))
