#!/usr/bin/env python3

import os
import random
import shutil
import os.path as osp
from lib.graphs import task

random.seed(42)
tests_dir = osp.join(osp.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)
test_num = 0


def dfs(u, used, state, edges):
    used[u] = True
    to_win = 0
    deg = 0
    for x, v in edges:
        if x != u:
            continue
        deg += 1
        if not used[v]:
            dfs(v, used, state, edges)
        if state[v] is None:
            pass
        elif not state[v]:
            state[u] = True
            break
        else:
            to_win += 1
    else:
        if to_win == deg:
            state[u] = False


def solve(n, edges, k):
    used = [False] * n
    state = [None] * n
    dfs(k, used, state, edges)
    if state[k] is None:
        return "Draw"
    elif not state[k]:
        return "Lose"
    else:
        return "Win"


def add_test(in_data, out_data):
    global test_num
    test_num += 1
    with open(osp.join(tests_dir, "{:02}".format(test_num)), "w") as f:
        f.write(in_data)
    with open(osp.join(tests_dir, "{:02}.a".format(test_num)), "w") as f:
        f.write(out_data + "\n")


def gen_test(n, m):
    k = random.randint(0, n-1)
    edges = task.gen_graph_edges(n, m, False)
    out_data = solve(n, edges, k)
    in_data = "{} {} {}\n".format(n, len(edges), k)
    for edge in edges:
        in_data += "{} {}\n".format(*edge)
    add_test(in_data, out_data)


for i in range(5):
    n = 2 + i * 2
    m = random.randint(1, n)
    gen_test(n, m)

for i in range(5):
    n = 4 + i * 2
    m = random.randint(0, 2*n)
    gen_test(n, m)

for i in range(20):
    n = random.randrange(50, 100)
    m = random.randint(0, round(n*n / n**0.5))
    gen_test(n, m)
