#!/usr/bin/env python3

import os
from lib import random
import shutil
import subprocess as sp


def generate_random_graph(n, p, seed, c):
    random.seed(seed)
    graph = [[0 for j in range(n)] for i in range(n)]

    if random.randint(0, 1):
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    graph[i][j] = 1
                    graph[j][i] = 1
    else:
        for i in range(n):
            for j in range(n):
                graph[i][j] = random.randint(0, 1)

    return graph


def generate_answer(test, truth=None):
    with open(test) as f:
        with open("%s.a" % test, "w") as g:
            sp.check_call(["./solution.py"], stdin=f, stdout=g)
    with open("%s.a" % test) as f:
        answer = f.readline()
    if truth is not None:
        assert truth == answer
    return answer


def write_graph(graph, filename):
    with open(filename, 'w') as f:
        f.write("%d\n" % len(graph))
        for row in graph:
            f.write("%s\n" % " ".join(map(str, row)))


simple_tests = [
    (
        "".join([
            "7\n",
            "0 1 0 0 0 1 1\n",
            "1 0 1 0 0 0 0\n",
            "0 1 0 0 1 1 0\n",
            "0 0 0 0 0 0 0\n",
            "0 0 1 0 0 1 0\n",
            "1 0 1 0 1 0 0\n",
            "1 0 0 0 0 0 0\n",
        ]),
        "YES\n",
    ),
    (
        "".join([
            "3\n",
            "0 1 1\n",
            "1 0 1\n",
            "0 1 0\n",
        ]),
        "NO\n",
    ),
    (
        "".join([
            "3\n",
            "0 0 0\n",
            "1 1 0\n",
            "1 1 0\n",
        ]),
        "NO\n",
    ),
    (
        "".join([
            "3\n",
            "0 1 1\n",
            "1 0 1\n",
            "1 1 0\n",
        ]),
        "YES\n",
    ),
    (
        "".join([
            "3\n",
            "0 0 1\n",
            "0 0 1\n",
            "1 0 0\n",
        ]),
        "NO\n",
    ),
]


def generate_test(test, n, p, c):
    test_name = os.path.join(test_folder, "%02d" % test)
    graph = generate_random_graph(n, p, "seed_%d_test" % test, c)
    write_graph(graph, test_name)
    answer = generate_answer(test_name)
    print("generated %s with n=%d, answer=%s" % (test_name, n, answer))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    test = 0
    for d, a in simple_tests:
        test += 1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(d)
        generate_answer(test_name, a)

    for n, p in (
    [(4, 0.6), (5, 1), (10, 0.3), (10, 0.7), (20, 0.2), (20, 0.7), (35, 0.1), (35, 0.5), (50, 0.1), (50, 0.7),
     (88, 0.1),
     (88, 0.5), (100, 0.05), (100, 0.3), (100, 0.9)]):
        test += 1
        generate_test(test, n, p, 3)
