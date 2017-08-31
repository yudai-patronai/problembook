#!/usr/bin/env python3

from lib.graphs import task


def bfs_dist_all(graph):
    dist = [-1] * len(graph)
    queue = [0]
    dist[0] = 0

    while queue:
        v = queue.pop(0)
        for v2 in graph[v]:
            if dist[v2] == -1:
                dist[v2] = dist[v] + 1
                queue.append(v2)

    return dist


def solve(graph):
    return '\n'.join(map(str, bfs_dist_all(graph))) + '\n'


if __name__ == "__main__":
    n, m, g = task.read_task()
    print(solve(g), end='')
