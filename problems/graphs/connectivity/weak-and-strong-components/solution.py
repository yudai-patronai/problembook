#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2000000)

def dfs(graph, order=None):
    visited = [False for i in range(len(graph))]
    if order is None:
        order = range(len(graph))
    for vertex in order:
        if not visited[vertex]:
            found = []
            dfs_impl(graph, vertex, visited, found)
            yield found


def dfs_impl(graph, current, visited, found):
    visited[current] = True
    for vertex in graph[current]:
        if not visited[vertex]:
            dfs_impl(graph, vertex, visited, found)
    found.append(current)


def find_components(graph):
    bigraph = [[] for i in range(len(graph))]
    for first, adjacent in enumerate(graph):
        for second in adjacent:
            bigraph[first].append(second)
            bigraph[second].append(first)
    return list(dfs(bigraph))


def reverse_graph(graph):
    reversed_graph = [[] for i in range(len(graph))]
    for first, adjacent in enumerate(graph):
        for second in adjacent:
            reversed_graph[second].append(first)
    return reversed_graph


def find_strong_components(graph):
    order = sum(dfs(graph), [])
    strong = list(dfs(reverse_graph(graph), order[::-1]))
    return strong


def read_graph():
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n)]
    for i in range(m):
        first, second = map(int, input().split())
        graph[first].append(second)
    return graph


if __name__ == "__main__":
    graph = read_graph()
    components = find_components(graph)
    strong_components = find_strong_components(graph)
    print(len(components), len(strong_components))
