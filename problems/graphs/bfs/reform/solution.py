#!/usr/bin/env python3
import bisect
import os
import sys

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

def dijkstra(graph, centers):
    district = [-1] * len(graph)
    dist = [float('+inf') for _ in graph]

    queue = []
    for x in centers:
        queue.append((0,x))
        dist[x] = 0
        district[x] = x

    while queue:
        vd, v = queue.pop(0)

        for v2, r in graph[v]:
            if dist[v2] > dist[v] + r:
                i = bisect.bisect_left(queue, (dist[v2], v2))
                if i < len(queue) and queue[i][1] == v2:
                    del queue[i]
                dist[v2] = dist[v] + r
                district[v2] = district[v]
                bisect.insort(queue, (dist[v2], v2))

    return district

def solve(graph, *centers):
    district = dijkstra(graph, centers)
    return '\n'.join(map(str, district))

if __name__ == "__main__":
    n, m, *args = read_task_weight()
    centers = args[:-1]
    g = args[-1]
    print(solve(g, *centers), end='')
