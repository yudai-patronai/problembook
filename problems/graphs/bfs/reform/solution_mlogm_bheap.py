#!/usr/bin/env python3
import heapq


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


def dijkstra_mlogm_heap(graph, centers):
    n = len(graph)
    district = [-1] * n  # область
    dist = [float('+inf')] * n
    queue = []

    for x in centers:
        district[x] = x
        dist[x] = 0
        heapq.heappush(queue, (0, x))

    while queue:
        vd, v = heapq.heappop(queue)
        if vd >= dist[v]:
            continue  # это фиктивный элемент очереди

        for v2, w in graph[v]:
            if dist[v2] > vd + w:
                dist[v2] = vd + w
                district[v2] = district[v]
                queue.add(v2)
                heapq.heappush(queue, (dist[v2], v2))

    return district


if __name__ == "__main__":
    graph, centers = read_task()
    district = dijkstra_mlogm_heap(graph, centers)
    print('\n'.join(map(str, district)))
