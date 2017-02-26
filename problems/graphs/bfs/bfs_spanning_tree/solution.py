#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.abspath('..'))
import task

def bfs_spanning_tree(graph):
    found = [False] * len(graph)
    queue = [0]
    found[0] = True
    result = []

    while queue:
        v = queue.pop(0)
        for v2 in graph[v]:
            if not found[v2]:
                found[v2] = True
                queue.append(v2)
                result.append((v, v2))

    return result

def solve(graph):
    return '\n'.join(['%d %d' % e for e in bfs_spanning_tree(graph)]) + '\n'

if __name__ == "__main__":
    n, m, g = task.read_task()
    print(solve(g), end='')
