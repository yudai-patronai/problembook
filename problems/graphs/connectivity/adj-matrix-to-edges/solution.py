#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input())  # число вершин графа
    G = []
    edges = []
    for i in range(n):
        g = list(map(int, input().split()))
        G.append(g)

    for i in range(n):
        g = G[i]
        for j in range(n):
            if g[j]:
                edges.append((i, j, g[j]))
    for e in edges:
        print(*e)
