#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2000000)

def dfs(edges, order=None, recursive=True):
    visited = [False for i in range(len(edges))]
    if order is None:
        order = range(len(edges))
    for i in order:
        if not visited[i]:
            if recursive:
                yield dfs_impl_recursive(edges, i, visited)
            else:
                yield dfs_impl(edges, i, visited)


def dfs_impl(graph, start, visited):
    found = []
    stack = [(start, 0)]
    visited[start] = True
    while stack:
        vertex, index = stack.pop()
        edges = graph[vertex]

        next_vertex = None
        while index < len(edges):
            edge = edges[index]
            index += 1
            if not visited[edge]:
                next_vertex = edge
                break

        if next_vertex is None:
            found.append(vertex)
        else:
            stack.append((vertex, index))
            stack.append((next_vertex, 0))
            visited[next_vertex] = True
    return found


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


def find_components(edges):
    graph = [[] for i in range(len(edges))]
    for a, bs in enumerate(edges):
        for b in bs:
            graph[a].append(b)
            graph[b].append(a)
    return list(dfs(graph))


def find_strong_components(graph):
    reversed_graph = [[] for i in range(len(graph))]
    for a, bs in enumerate(graph):
        for b in bs:
            reversed_graph[b].append(a)
    order = sum(dfs(graph), [])
    strong = list(dfs(reversed_graph, order[::-1]))
    return strong


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    edges = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)

    components = find_components(edges)
    strong_components = find_strong_components(edges)
    print(len(components), len(strong_components))
