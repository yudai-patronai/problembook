#!/usr/bin/env python3
import bisect
import os
import sys

sys.path.append(os.path.abspath('..'))
import task

def dijkstra(G, start):
    shortest_path = [float('+inf') for i in range(len(G))]
    shortest_path[start] = 0
    queue = [start]
    prev = [-1 for i in range(len(G))]
    while queue:
        current = queue.pop(0)
        for neighbour, weight in G[current]:
            new_shortest_path = shortest_path[current] + weight
            if new_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = new_shortest_path
                queue.append(neighbour)
                prev[neighbour] = current
    return shortest_path, prev


def get_shortest_path(G, start, finish):
    _, path = dijkstra(G, start)
    result = [finish]
    cur = finish
    while cur != start:
        result.append(path[cur])
        cur = path[cur]
    return result[::-1]


def solve(G, s, f):
    return ' '.join(map(str, get_shortest_path(G, s, f))) + '\n'

if __name__ == "__main__":
    n, m, x, y, g = task.read_task_weight()
    print(solve(g, x, y), end='')
