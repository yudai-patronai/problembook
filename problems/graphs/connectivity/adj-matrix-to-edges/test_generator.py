#!/usr/bin/env python3

import os
from lib import random
import shutil
import subprocess as sp


def get_graph_size(graph):
    return len(graph), sum([len(bs) for bs in graph])


def dump_graph(graph, name):
    n, m = get_graph_size(graph)
    with open(name, "w") as f:
        f.write("%d\n%d\n" % (n, m))
        for a, bs in enumerate(graph):
            for b in bs:
                m += 1
                f.write("%d %d\n" % (a, b))


simple_tests = [
    """4
    0 0 0 0
    0 0 0 0
    0 0 0 0
    0 0 0 0
    """,
    """3
    2 0 1
    14 8 3
    31 0 0
    """,
]


def dump_graph(graph, name):
    n, m = get_graph_size(graph)
    with open(name, "w") as f:
        f.write("%d\n" % (n))
        for g in graph:
            line = ' '.join(str(p) for p in g) + '\n'
            f.write(line)


def generate_answer(test):
    with open(test) as f:
        with open("%s.a" % test, "w") as g:
            sp.check_call(["./solution.py"], stdin=f, stdout=g)
    with open("%s.a" % test) as f:
        answer = list(map(int, f.readline().split()))
    return answer


def generate_random_graph(n, p, seed):
    if n > 3000:
        return generate_big_graph(n, p, seed)
    random.seed(seed)
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            num = random.randint(-100, 100)
            graph[i].append(num)
    return graph


def generate_big_graph(n, p, seed):
    random.seed(seed)
    graph = [set() for i in range(n)]
    m = int(n * (n - 1) * p)
    for i in range(m):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        graph[a].add(b)
    return graph


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    test = 0
    for d in simple_tests:
        test += 1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(d)
        generate_answer(test_name)

    param_list = [(3, 1), (20, 2), (100, 13), (41, 30), (33, 17), (16, 1)]
    for n, k in param_list:
        p = k / n
        graph = generate_random_graph(n, p, "test=%d,n=%d,k=%d" % (test, n, k))
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        dump_graph(graph, test_name)
        print("graph dumped")
        answer = generate_answer(test_name)
        print("generated: %s, %s" % (get_graph_size(graph), answer))
        test += 1
