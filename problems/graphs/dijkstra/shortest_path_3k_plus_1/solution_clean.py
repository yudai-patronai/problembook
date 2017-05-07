#!/usr/bin/env python3
import heapq

'''
Нужно построить вспомогательный граф, вершинами которого будут
состояния (v,c), где v — номер текущей вершины, c = 0, 1 или 2 —
остаток от деления количества ребер в пути на три. Любое ребро (u,v)
исходного графа в этом новом графе превратится в шесть направленыx
ребер ((u,0),(v,1)), ((v,0),(v,1)), ((u,1),(v,2)), ((v,1),(v,2)),
((u,2),(v,0)), ((v,2),(v,0)). После этого на вспомогательном графе
надо с помощью алгоритма Дейкстры найти путь минимального веса из
стартовой вершины с остатком 0 в конечную вершину, с остатком равным 1.

Пусть для удобства 3n+x - индекс вершины (n, x) вспомогательного графа.
'''
def zenc(n):
    return n * 3

def oenc(n):
    return n * 3 + 1

def tenc(n):
    return n * 3 + 2

def dec(n):
    return n // 3

def read_graph_weight(n, m):
    graph = [[] for i in range(3 * n)]
    for i in range(m):
        a, b, w = list(map(int, input().split()))
        graph[zenc(a)].append((oenc(b), w))
        graph[oenc(a)].append((tenc(b), w))
        graph[tenc(a)].append((zenc(b), w))
        graph[zenc(b)].append((oenc(a), w))
        graph[oenc(b)].append((tenc(a), w))
        graph[tenc(b)].append((zenc(a), w))

    return graph

def read_pairs(k):
    pairs = []
    for i in range(k):
        a, b = list(map(int, input().split()))
        pairs.append((zenc(a), oenc(b)))

    return pairs

def read_task():
    n, m = list(map(int, input().split()))
    graph = read_graph_weight(n, m)
    k = int(input())
    pairs = read_pairs(k)
    return graph, pairs


def dijkstra_mlogm_heap(graph, start, end):
    n = len(graph)
    dist = [float('+inf')] * n
    parent = [-1] * n
    queue = []

    dist[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        vd, v = heapq.heappop(queue)
        if vd > dist[v]:
            continue  # это фиктивный элемент очереди
        if v == end:
            break;

        for v2, w in graph[v]:
            if dist[v2] > vd + w:
                dist[v2] = vd + w
                parent[v2] = v
                heapq.heappush(queue, (dist[v2], v2))

    return parent

if __name__ == "__main__":
    graph, pairs = read_task()
    for a, b in pairs:
        parent = dijkstra_mlogm_heap(graph, a, b)
        path = [b]
        while path[0] != a:
            if parent[path[0]] == -1:
                print(-1)
                break
            path.insert(0, parent[path[0]])
        else:
            print(' '.join(map(str, map(dec, path))))
