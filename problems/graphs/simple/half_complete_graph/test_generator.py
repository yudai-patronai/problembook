#!/usr/bin/env python3

import os
import random
import shutil
import subprocess as sp

def generate_complete_random_rest(graph, n, m):
    for i in range(m):
        v1 = random.randint(0, n-1)
        v2 = random.randint(0, n-1)
        while graph[v1][v2]:
            v1 = random.randint(0, n-1)
            v2 = random.randint(0, n-1)
        graph[v1][v2] = 1
    return graph

def generate_random_graph(n, m, p, seed, c):
    random.seed(seed)
    graph = []

    graph = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            graph[i][j] = 0

    if m >= n * (n-1) / 2:
        if random.randint(0, 5) > 1:
            done = 0
            for i in range(n):
                for j in range(i + 1, n):
                    if random.randint(0, 1):
                       graph[i][j] = 1
                    else:
                        graph[j][i] = 1
                    done += 1
            generate_complete_random_rest(graph, n, m - done)
        else:
            generate_complete_random_rest(graph, n, m)
    else:
        generate_complete_random_rest(graph, n, m)

    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                edges.append([i, j])
    return edges


def generate_answer(test, truth=None):
    with open(test) as f:
        with open("%s.a" % test, "w") as g:
            sp.check_call(["./solution.py"], stdin=f, stdout=g)
    with open("%s.a" % test) as f:
        answer = f.readline()
    if truth is not None:
        assert truth == answer
    return answer


def write_graph(graph, n, m, filename):
    with open(filename, 'w') as f:
        f.write("{} {}\n".format(n, m))
        for row in graph:
            f.write("%s\n" % " ".join(map(str, row)))


simple_tests = [
]


def generate_test(test, n, m, p, c):
    test_name = os.path.join(test_folder, "%02d" % test)
    graph = generate_random_graph(n, m, p, "seed_%d_test" % test, c)
    write_graph(graph, n, m, test_name)
    answer = generate_answer(test_name)
    print("generated %s with n=%d, m=%d, answer=%s" % (test_name, n, m,answer))


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

    for n, m, p in ([(4, 15, 0.6), (5, 10,  1),  (5, 13,  1), (5, 15,  1), (10, 1, 0.3), 
                    (10, 90,  0.7), (20, 11, 0.2), (20, 300, 0.7), (20, 250, 0.7),(20, 250, 0.7),(20, 250, 0.7),(20, 250, 0.7), (35, 30, 0.1), (35, 500, 0.5), 
                    (50, 2, 0.1), (50, 1500, 0.7), (50, 1900, 0.7), (50, 1900, 0.7), (50, 1900, 0.7), (88,123, 0.1),
                    (88, 200, 0.5), (100, 500, 0.05)]):
        test += 1
        generate_test(test, n, m, p, 3)
