#!/usr/bin/env python3
import heapq

'''
Нужно построить вспомогательный граф, вершинами которого будут
состояния (v,c), где v — номер текущей вершины, c = 0, 1, 2, 3, 4 —
остаток от деления количества ребер в пути на пять. Любое ребро (u,v)
исходного графа в этом новом графе превратится в 10 направленый ребер
((u,0),(v,1)), ((v,0),(v,1)), ((u,1),(v,2)), ((v,1),(v,2)),
((u,2),(v,3)), ((v,2),(v,3)), ((u,3),(v,4)), ((v,3),(v,4)),
((u,4),(v,0)), ((v,4),(v,0)). После этого на вспомогательном графе
надо с помощью алгоритма Дейкстры найти путь минимального веса из
стартовой вершины с остатком 0 в конечную, с остатком равным 2.

Пусть для удобства 5n+x - индекс вершины (n, x) вспомогательного графа.
'''
def enc0(n):
    return n * 5

def enc1(n):
    return n * 5 + 1

def enc2(n):
    return n * 5 + 2

def enc3(n):
    return n * 5 + 3

def enc4(n):
    return n * 5 + 4

def dec(n):
    return n // 5

def read_graph_weight(n, m):
    graph = [[] for i in range(5 * n)]
    for i in range(m):
        a, b, w = list(map(int, input().split()))
        graph[enc0(a)].append((enc1(b), w))
        graph[enc1(a)].append((enc2(b), w))
        graph[enc2(a)].append((enc3(b), w))
        graph[enc3(a)].append((enc4(b), w))
        graph[enc4(a)].append((enc0(b), w))
        graph[enc0(b)].append((enc1(a), w))
        graph[enc1(b)].append((enc2(a), w))
        graph[enc2(b)].append((enc3(a), w))
        graph[enc3(b)].append((enc4(a), w))
        graph[enc4(b)].append((enc0(a), w))

    return graph

def read_pairs(k):
    pairs = []
    for i in range(k):
        a, b = list(map(int, input().split()))
        pairs.append((enc0(a), enc2(b)))

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
