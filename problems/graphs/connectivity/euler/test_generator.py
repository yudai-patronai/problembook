#!/usr/bin/env python3

# TODO: Improve tests

import os
from lib import random
import shutil
import subprocess as sp

simple_tests = [
    ("""4
4
0 1
1 2
2 3
3 0
""", "YES\n"),

    ("""3
2
0 1
1 2
""", "NO\n"),

    ("""1
0
""", "YES\n"),

    ("""2
1
0 1
""", "NO\n"),

    ("""6
6
0 1
2 1
0 2
3 4
4 5
5 3
""", "NO\n"),

    ("""6
7
0 1
2 1
0 2
3 4
4 5
5 3
0 5
""", "NO\n"),

    ("""6
7
0 1
2 1
0 2
3 4
4 5
5 2
2 3
""", "YES\n"),
]


def generate_answer(test):
    with open(test) as f:
        with open("%s.a" % test, "w") as g:
            sp.check_call(["./solution.py"], stdin=f, stdout=g)
    with open("%s.a" % test) as f:
        answer = f.read()
    return answer


def graph_sum(graphs, seed):
    random.seed(seed)
    n = sum([len(g) for g in graphs])
    total_graph = [set() for i in range(n)]
    vertex_map = [i for i in range(n)]
    random.shuffle(vertex_map)
    shift = 0
    for g in graphs:
        for v, es in enumerate(g):
            for e in es:
                total_graph[vertex_map[v + shift]].add(vertex_map[e + shift])
        shift += len(g)
    return total_graph


def generate_almost_euler_graph(seed):
    random.seed(seed)
    n = random.randint(0, 300)
    m = random.randint(0, n * n // 2)
    graph = [set() for i in range(n)]
    start = random.randint(0, n - 1)
    current = start
    visited = set()
    visited.add(current)
    for i in range(m):
        end = random.randint(0, n - 1)
        if end == current or (end in graph[current]):
            continue
        graph[current].add(end)
        graph[end].add(current)
        current = end
        visited.add(current)

    if current == start or current not in graph[start] and len(visited) == n:
        is_euler = True
        graph[start].add(current)
        graph[current].add(start)
    else:
        is_euler = False
    return graph, is_euler


def generate_random_graph(seed):
    random.seed(seed)
    n = random.randint(0, 300)
    m = random.randint(0, n * n // 2)
    graph = [set() for i in range(n)]
    for i in range(m):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        if a != b:
            graph[a].add(b)
            graph[b].add(a)
    return graph, False


def get_graph_size(graph):
    return len(graph), sum([len(bs) for bs in graph])


def dump_graph(graph, name):
    n, m = get_graph_size(graph)
    with open(name, "w") as f:
        f.write("%d\n%d\n" % (n, m / 2))
        for a, bs in enumerate(graph):
            for b in bs:
                m += 1
                if a < b:
                    if hash("%d,%d,%s" % (a, b, name)) % 2 == 0:
                        f.write("%d %d\n" % (a, b))
                    else:
                        f.write("%d %d\n" % (b, a))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    test = 0
    for data, answer in simple_tests:
        test += 1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(data)
        got = generate_answer(test_name)
        assert answer == got, "%s - %s" % (answer, got)

    while test < 45:
        for func in (generate_random_graph, generate_almost_euler_graph):
            test += 1
            test_name = os.path.join(test_folder, "%02d" % test)
            print("generating %s..." % test_name)
            graph, is_euler = func("test=%s" % test)
            dump_graph(graph, test_name)
            answer = generate_answer(test_name).strip()
            print("generated: %s, %s - %s" % (get_graph_size(graph), is_euler, answer))

    while test < 50:
        test += 1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        graphs = [generate_almost_euler_graph("test=%s,%d" % (test, i))[0] for i in range(1 + test % 4)]
        graph = graph_sum(graphs, "test=%s" % test)
        dump_graph(graph, test_name)
        answer = generate_answer(test_name).strip()
        print("generated: %s - %s" % (get_graph_size(graph), answer))
