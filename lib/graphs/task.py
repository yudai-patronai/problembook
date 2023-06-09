#!/usr/bin/python3

import os
import shutil
from lib import random
import solution
import sys
import bisect

random.seed(100)

def read_graph(n, m):
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph

def read_graph_weight(n, m):
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    return graph

def read_graph_directed(n, m):
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    return graph

def read_graph_weighted_to_adj_matrix(n, m):
    matrix = [[float('+inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    for i in range(m):
        a, b, w = map(int, input().split())
        matrix[a][b] = w
        matrix[b][a] = w

    return matrix

def read_task_f(read_graph_func):
    args = list(map(int, input().split()))
    args.append(read_graph_func(args[0], args[1]))
    return args

def read_task():
    return read_task_f(read_graph)

def read_task_weight():
    return read_task_f(read_graph_weight)

def read_task_directed():
    return read_task_f(read_graph_directed)

def read_task_weight_adj_matrix():
    return read_task_f(read_graph_weighted_to_adj_matrix)

def gen_tree_edges(n):
    return [(random.randint(0, k-1), k) for k in range(1, n)]

def gen_graph_edges(n, m, connective=True):
    g = set(gen_tree_edges(n)) if connective else set()

    for i in range(m):
        a = random.randrange(n)
        b = random.randrange(n - 1)
        if a > b:
            a, b = b, a
        elif a == b:
            b = n - 1
        g.add((a, b))

    g = list(g)
    for i in range(len(g)):
        if random.random() < 0.5:
            g[i] = g[i][::-1]

    random.shuffle(g)

    return g

def edges_to_graph(n, edges, directed=False):
    res = [[] for i in range(n)]
    if not edges:
        return res

    if len(edges[0]) == 2:
        for e in edges:
            a, b = e
            res[a].append(b)
            if not directed:
                res[b].append(a)
    else:
        for e in edges:
            a, b, d = e
            res[a].append((b, d))
            if not directed:
                res[b].append((a, d))

    return res

def edges_to_adj_matrix(n, edges, directed=False):
    m = [[float('+inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        m[i][i] = 0

    if not edges:
        return m

    if len(edges[0]) == 2:
        for e in edges:
            a, b = e
            m[a][b] = 1
            if not directed:
                m[b][a] = 1
    else:
        for e in edges:
            a, b, d = e
            m[a][b] = d
            if not directed:
                m[b][a] = d

    return m

def add_rand_weight(edges):
    return [(a, b, random.randrange(1, 100)) for a, b in edges]

def gen_test(tests_dir, ind, n, edges, *args, **kwargs):
    m = len(edges)
    params = ' '.join(map(str, (n, m) + args))
    directed = kwargs.get('directed', False)
    print('test %d ' % ind + params)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(params + '\n')
        for e in edges:
            f.write(' '.join(map(str, e)) + '\n')

    with open(ans, 'w') as f:
        if kwargs.get('adj_matrix', False):
            f.write(solution.solve(edges_to_adj_matrix(n, edges, directed=directed), *args))
        else:
            f.write(solution.solve(edges_to_graph(n, edges, directed=directed), *args))

def gen_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        gen_test(tests_dir, t, n, gen_graph_edges(n, i))
        t += 1

    for i in range(5):
        n = 4 + i * 2
        gen_test(tests_dir, t, n, gen_graph_edges(n, 0))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph_edges(n, 100))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph_edges(n, 10000))
        t += 1

def gen_test_directed(tests_dir, t, n, e):
    gen_test(tests_dir, t, n, gen_graph_edges(n, e, connective=False),
             directed=True)

def gen_tests_directed(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in [1,5,2] + list(range(3,10)):
        n = 2 + i * 2
        gen_test_directed(tests_dir, t, n, i * i)
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test_directed(tests_dir, t, n, 500)
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test_directed(tests_dir, t, n, 1000)
        t += 1

def gen_test_weight_xy(tests_dir, t, n, e, x, y):
    gen_test(tests_dir, t, n, add_rand_weight(gen_graph_edges(n, e)),
             x, y)

def gen_test_weight_centers(tests_dir, t, n, e, centers):
    gen_test(tests_dir, t, n, add_rand_weight(gen_graph_edges(n, e)),
             *centers)

def gen_test_weight(tests_dir, t, n, e, add_xy=True, adj_matrix=False):
    if add_xy:
        gen_test_weight_xy(tests_dir, t, n, e, random.randrange(n), random.randrange(n))
    else:
        gen_test(tests_dir, t, n, add_rand_weight(gen_graph_edges(n, e)), adj_matrix=adj_matrix)

def gen_tests_weight_xy(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        gen_test_weight(tests_dir, t, n, i)
        t += 1

    for i in range(5):
        n = 2 + i * 2
        gen_test_weight(tests_dir, t, n, 0)
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test_weight(tests_dir, t, n, 5)
        t += 1

    for i in range(2):
        n = random.randrange(100, 1000)
        gen_test_weight_xy(tests_dir, t, n, 10, 5, 5)
        t += 1

    for i in range(18):
        n = random.randrange(100, 1000)
        gen_test_weight(tests_dir, t, n, 100)
        t += 1

def gen_tests_weight_adj(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        gen_test_weight(tests_dir, t, n, i, add_xy=False, adj_matrix=True)
        t += 1

    for i in range(5):
        n = 2 + i * 2
        gen_test_weight(tests_dir, t, n, 0, add_xy=False, adj_matrix=True)
        t += 1

    for i in range(40):
        n = random.randrange(10, 100)
        e = random.randrange(10, n * 5)
        gen_test_weight(tests_dir, t, n, e, add_xy=False, adj_matrix=True)
        t += 1

# graph:
# [
#   [(v1, dist1), (v2, dist2),,,]
#   ...
# ]
#
# return (dist, parent)
# parent[i] - parent of i'th vertex
def dijkstra(graph, x, y):
    parent = [-1] * len(graph)

    if x == y:
        return (0, parent)

    dist = [float('+inf') for _ in graph]
    queue = [(0, x)]
    dist[x] = 0

    while queue:
        vd, v = queue.pop(0)
        if v == y:
            return (vd, parent)

        for v2, r in graph[v]:
            if dist[v2] > dist[v] + r:
                i = bisect.bisect_left(queue, (dist[v2], v2))
                if i < len(queue) and queue[i][1] == v2:
                    del queue[i]
                dist[v2] = dist[v] + r
                parent[v2] = v
                bisect.insort(queue, (dist[v2], v2))

    return (None, None)
