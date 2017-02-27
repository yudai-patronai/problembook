#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.abspath('../..'))
import task

def bfs_dist(graph, x, y):
    if x == y:
        return 0

    dist = [-1] * len(graph)
    queue = [x]
    dist[x] = 0

    while queue:
        v = queue.pop(0)
        for v2 in graph[v]:
            if dist[v2] == -1:
                dist[v2] = dist[v] + 1
                if v2 == y:
                    return dist[v2]

                queue.append(v2)

    return -1

def solve(graph, x, y):
    return str(bfs_dist(graph, x, y)) + '\n'

if __name__ == "__main__":
    n, m, x, y, g = task.read_task()
    print(solve(g, x, y), end='')
