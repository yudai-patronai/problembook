#!/usr/bin/env python3
import bisect
import os
import sys

sys.path.append(os.path.abspath('../..'))
import task

def prima(graph, x):
    parent = [-1] * len(graph)
    dist = [float('+inf') for _ in graph]
    queue = [(0, x)]
    dist[x] = 0
    marked = set()

    while queue:
        _, v = queue.pop(0)
        marked.add(v)

        for v2, r in graph[v]:
            if v2 not in marked and dist[v2] > r:
                i = bisect.bisect_left(queue, (dist[v2], v2))
                if i < len(queue) and queue[i][1] == v2:
                    del queue[i]
                dist[v2] = r
                parent[v2] = v
                bisect.insort(queue, (dist[v2], v2))

    return dist, parent

def solve(graph):
    dist, parent = prima(graph, 0)
    l = []
    for i in range(1, len(parent)):
        l.append("%d %d" % (parent[i], i))

    return str(sum(dist)) + '\n' + '\n'.join(l) + '\n'

if __name__ == "__main__":
    n, m, g = task.read_task_weight()
    print(solve(g), end='')
