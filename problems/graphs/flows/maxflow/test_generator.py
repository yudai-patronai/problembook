#!/usr/bin/env python3

import os
import shutil
import random

random.seed(100)


def w():
    return random.randint(1, 10000)


def gen_network(n, m):
    all_edges = {i: {j for j in range(1, n) if j != i} for i in range(n-1)}
    unused = {i for i in range(1, n-1)}
    used = {0}
    edges = []
    sinks = unused.copy()
    while unused:
        u = random.sample(used, 1)[0]
        v = random.sample(unused, 1)[0]
        edges.append((u, v, w()))
        all_edges[u].discard(v)
        if not all_edges[u]:
            del all_edges[u]
        sinks.discard(u)
        used.add(v)
        unused.remove(v)
    u = random.sample(used, 1)[0]
    edges.append((u, n-1, w()))
    all_edges[u].discard(n-1)
    if not all_edges[u]:
        del all_edges[u]
    sinks.discard(u)
    m -= n-1
    while sinks:
        u = random.sample(sinks, 1)[0]
        v = random.sample(all_edges[u], 1)[0]
        edges.append((u, v, w()))
        sinks.discard(u)
        all_edges[u].discard(v)
        if not all_edges[u]:
            del all_edges[u]
        m -= 1
    while m > 0:
        u = random.sample(all_edges.keys(), 1)[0]
        v = random.sample(all_edges[u], 1)[0]
        edges.append((u, v, w()))
        all_edges[u].discard(v)
        if not all_edges[u]:
            del all_edges[u]
        m -= 1
    return edges


class Edge:
    def __init__(self, i, v, c):
        self.i = i
        self.v = v
        self.c = c
        self.f = 0


def dfs(u, adj_list, used, p, t, d):
    used[u] = True
    if u == t:
        return True
    for e in adj_list[u]:
        v = e.v
        if not used[v] and e.c-e.f >= d:
            p.append(e)
            if dfs(v, adj_list, used, p, t, d):
                return True
            p.pop()
    return False


def solve(n, input):
    adj_list = [set() for _ in range(n)]
    edges = []
    for i, u in enumerate(input):
        u, v, c = u
        e = Edge(2 * i, v, c)
        adj_list[u].add(e)
        edges.append(e)
        e = Edge(2 * i + 1, u, 0)
        adj_list[v].add(e)
        edges.append(e)
    s = 0
    t = n-1

    max_flow = 0
    d = 1
    while d * 2 <= 10000:
        d *= 2
    while d:
        path = []
        used = [False] * n
        if not dfs(0, adj_list, used, path, t, d):
            d //= 2
            continue
        f = float("inf")
        v = 0
        for e in path:
            u = v
            v = e.v
            if f > e.c - e.f:
                f = e.c - e.f
        for e in path:
            u = v
            v = e.v
            e.f += f
            edges[e.i ^ 1].f -= f
        max_flow += f
    return max_flow


def gen_test(ind, n, m):
    edges = gen_network(n, m)
    m = len(edges)
    max_flow = solve(n, edges)

    test = os.path.join(tests_dir, '%.2d' % ind)
    with open(test, "w") as f:
        f.write("{} {}\n".format(n, m))
        for e in edges:
            f.write(" ".join(map(str, e)) + '\n')

    with open(test + ".a", "w") as f:
        f.write("{}\n".format(max_flow))


def manual_test(ind, n, edges):
    m = len(edges)
    max_flow = solve(n, edges)

    test = os.path.join(tests_dir, '%.2d' % ind)
    with open(test, "w") as f:
        f.write("{} {}\n".format(n, m))
        for e in edges:
            f.write(" ".join(map(str, e)) + '\n')

    with open(test + ".a", "w") as f:
        f.write("{}\n".format(max_flow))


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)
t = 1
manual_test(t, 4, [
    (0, 1, 2),
    (0, 2, 3),
    (1, 3, 5),
    (2, 3, 1)
])
t += 1

manual_test(t, 3, [(0, 1, 10), (1, 2, 12)])
t += 1

manual_test(t, 7, [
    (0, 1, 12),
    (0, 2, 4),
    (1, 3, 1),
    (2, 3, 4),
    (3, 4, 9),
    (3, 5, 43),
    (4, 6, 1),
    (5, 6, 45),
    (0, 3, 12),
    (3, 6, 6)
])
t += 1

for i in range(5):
    n = 2 + i * 2
    m = random.randint(n-1, i * (i-1) + 2 * (n-1) + 1)
    gen_test(t, n, m)
    t += 1

for i in range(5):
    n = random.randrange(10, 50)
    m = random.randint(n-1, n * 5)
    gen_test(t, n, m)
    t += 1

n = 100
m = 110
gen_test(t, n, m)
