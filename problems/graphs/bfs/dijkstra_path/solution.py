#!/usr/bin/env python3

def read_graph():
    n, m = map(int, input().split())
    s, f = map(int, input().split())

    graph = [[] for i in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    return graph, s, f


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
    return ' '.join(map(str, get_shortest_path(G, s, f)))

if __name__ == "__main__":
    print(solve(*read_graph()))
