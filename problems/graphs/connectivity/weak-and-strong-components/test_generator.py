#!/usr/bin/env python3

import os
import subprocess as sp
import random


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
"""3
3
1 2
2 0
0 1
""",

"""4
4
0 1
1 2
2 3
1 0
""",

"""5
6
1 2
2 3
3 2
2 1
4 1
2 0
""",

"""0
0
""",

"""8
9
1 0
0 2
3 0
3 5
5 4
4 3
2 1
6 7
7 0
""",

"""3
2
1 2
2 0
""",
]


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
            if i == j:
                continue
            if random.random() < p:
                graph[i].append(j)
    for edges in graph:
        random.shuffle(edges)
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
    test = 0
    for d in simple_tests:
        test += 1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(d)
        generate_answer(test_name)
    for n, k in ([(10, 1)] * 2 + [(10, 2)] * 2 + [(10, 3)] + [(10, 9)] +
                 [(100, 1)] * 2 + [(100, 2)] * 2 + [(100, 3)] * 4 + [(100, 4)] * 4 + [(100, 90)] +
                 [(300, 1)] + [(300, 3)] + [(300, 5)] + [(300, 50)] + [(300, 250)] +
                 [(990, 1)] * 2 + [(990, 2)] * 2 + [(990, 3)] * 3 + [(990, 4)] * 4 + [(990, 5)] * 4 + [(990, 7)] * 4 + [(990, 9)] * 2 + [(900, 100)] * 2
                 # [(3000, 1)] * 2 + [(3000, 2)] * 2 + [(3000, 3)] * 2 + [(3000, 4)] * 2 + [(3000, 5)] * 2 + [(3000, 7)] * 2 +
                 # [(10000, 1)] * 2 + [(10000, 2)] * 2 + [(10000, 3)] * 2 + [(10000, 5)] * 2 + [(10000, 7)] * 2 + [(10000, 5000)]
                 # [(100000, 1)] + [(100000, 2)] + [(100000, 3)] + [(100000, 5)] + [(100000, 7)] + [(100000, 10)]
                ):
        test += 1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        p = k / n
        graph = generate_random_graph(n, p, "test=%d,n=%d,k=%d" % (test, n, k))
        dump_graph(graph, test_name)
        answer = generate_answer(test_name)
        print("generated: %s, %s" % (get_graph_size(graph), answer))
