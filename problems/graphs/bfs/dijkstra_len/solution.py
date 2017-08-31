#!/usr/bin/env python3

from lib.graphs import task


def solve(graph, x, y):
    dist, parent = task.dijkstra(graph, x, y)
    return '%d\n' % dist


if __name__ == "__main__":
    n, m, x, y, g = task.read_task_weight()
    print(solve(g, x, y), end='')
