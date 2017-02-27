#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.abspath('..'))
import task

def bfs_shortest_cycle_x(graph, x):
    found = [False] * len(graph)
    parent = [-1] * len(graph)
    queue = [x]
    found[x] = True
    result = []

    loop_found = False

    while queue:
        v = queue.pop(0)
        for v2 in graph[v]:
            if v2 == x:
                loop_found = True
                queue = []
                break
            if not found[v2]:
                found[v2] = True
                parent[v2] = v
                queue.append(v2)

    if loop_found:
        a = [v]
        while a[0] != x and a[0] != -1:
            a.insert(0, parent[a[0]])

        return a

    return []

def bfs_shortest_cycle(graph):
    mi = float('+inf')
    mi_list = []

    for x in range(len(graph)):
        c = bfs_shortest_cycle_x(graph, x)
        if c and (len(c) < mi):
            mi = len(c)
            mi_list = c

    return mi_list

def solve(graph):
    c = bfs_shortest_cycle(graph)
    if c:
        return ' '.join(map(str, c)) + '\n'
    else:
        return 'NO CYCLES\n'

if __name__ == "__main__":
    n, m, g = task.read_task_directed()
    print(solve(g), end='')
