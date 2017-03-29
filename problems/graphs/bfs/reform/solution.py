#!/usr/bin/env python3
import heapq

#######################
# Library
#######################

def read_graph_weight(n, m):
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    return graph

def read_task_f(read_graph_func):
    args = list(map(int, input().split()))
    args.append(read_graph_func(args[0], args[1]))
    return args

def read_task_weight():
    return read_task_f(read_graph_weight)

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

        for v2, r in graph[v]:
            if dist[v2] > vd + r:
                dist[v2] = vd + r
                district[v2] = district[v]
                queue.add(v2)
                heapq.heappush(queue, (dist[v2], v2))

    return district

def solve(graph, *centers):
    district = dijkstra_mlogm_heap(graph, centers)
    return '\n'.join(map(str, district))

if __name__ == "__main__":
    n, m, *args = read_task_weight()
    centers = args[:-1]
    g = args[-1]
    print(solve(g, *centers), end='')
