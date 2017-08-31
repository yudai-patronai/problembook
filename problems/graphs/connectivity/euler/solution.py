#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2000000)


def dfs(edges, order=None):
    visited = [False for i in range(len(edges))]
    if order is None:
        order = range(len(edges))
    for i in order:
        if not visited[i]:
            yield dfs_impl_recursive(edges, i, visited)


def dfs_impl_recursive(graph, start, visited):
    found = []
    dfs_impl_internal(graph, start, visited, found)
    return found


def dfs_impl_internal(edges, current, visited, found):
    visited[current] = True
    for v in edges[current]:
        if not visited[v]:
            dfs_impl_internal(edges, v, visited, found)
    found.append(current)


def check_euler(edges):
    for es in edges:
        if len(es) % 2 != 0:
            return False

    components = list(dfs(edges))
    return len(components) == 1


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    edges = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    if check_euler(edges):
        print("YES")
    else:
        print("NO")
