#!/usr/bin/env python3

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

def read_graph():
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph

def solve(graph):
    return '\n'.join(map(str, bfs_dist_all(graph))) + '\n'

if __name__ == "__main__":
    print(solve(read_graph()))
