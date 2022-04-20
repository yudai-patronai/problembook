#!/usr/bin/env python3

import os.path as osp
import random
from collections import deque


class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self._reachable = [set() for _ in n]
        self._parents = [set() for _ in n]
        self.edges = []

    def gen(self):
        max_vertex_num = self.n - 1
        while len(self.edges) < self.m:
            u = random.randint(0, max_vertex_num)
            v = random.randint(0, max_vertex_num)
            if u == v or u in self._reachable[v] or u in self._parents[v]:
                continue
            self.edges.append((u, v))
            self._parents[v].add(u)
            queue = deque((u))
            self._add_to_reachable(queue, v)

    def _add_to_reachable(self, queue:deque, v):
        for u in queue:
            self._reachable[u].add(v)
            queue.extend(self._parents[u])

    def dfs(self, u, state):
        for edge in self.edges:
            if u == edge[0]:
                v = edge[1]
                if state[v] is None:
                    self.dfs(v, state)
                if not state[v]:
                    state[u] = True
        if state[u] is None:
            state[u] = False


def solve(g, k):
    n = g.n
    state = [None] * n
    g.dfs(k, state)
    return "First" if state[k] else "Second"


random.seed(42)
tests_dir = osp.join(osp.dirname(__file__), 'tests')
test_num = 0

def add_test(in_data, out_data):
    global test_num
    test_num += 1
    with open(osp.join(tests_dir, "{:02}".format(test_num)), "w") as f:
        f.write(in_data)
    with open(osp.join(tests_dir, "{:02}.a".format(test_num)), "w") as f:
        f.write(out_data)


def gen_test(n, m):
    k = random.randint(0, n-1)
    g = Graph(n, m)
    g.gen()
    out_data = solve(g, k)
    in_data = "{} {} {}\n".format(g.n, g.m, k)
    for edge in g.edges:
        in_data += "{} {}\n".format(*edge)
    add_test(in_data, out_data)


for i in range(5):
    n = 2 + i * 2
    m = random.randint(0, i)
    gen_test(n, m)

for i in range(5):
    n = 4 + i * 2
    m = random.randint(0, 2*i)
    gen_test(n, m)

for i in range(20):
    n = random.randrange(100, 1000)
    m = random.randint(0, i*i / 4)
    gen_test(n, m)
