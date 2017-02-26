#!/usr/bin/python3

import os
import shutil
import random
import solution
import sys

random.seed(100)

def edge_ind(a, b):
    if a > b:
        a, b = b, a
    return a + b * (b - 1) / 2

def gen_tree(n):
    return [(random.randint(0, k-1), k) for k in range(1, n)]

def gen_tree2(n):
    power = [0] * n
    powersum = 0
    result = []

    for k in range(1, n):
        x = int(random.random() * powersum)
        v = 0
        s = power[0]
        while s < x:
            v += 1
            s += power[v]

        power[v] += 1
        power[k] = 1
        powersum += 2
        result.append((v, k))

    return result

def gen_graph(n, m):
    g = set(gen_tree(n))

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

def graph_edges_to_list(n, graph):
    res = [[] for i in range(n)]
    for e in graph:
        a, b = e
        res[a].append(b)
        res[b].append(a)

    return res

def gen_test(tests_dir, ind, n, graph):
    print('test %d %d' % (ind, n))
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'
    m = len(graph)

    with open(test, 'w') as f:
        f.write('%d\n%d\n' % (n, m))
        for e in graph:
            f.write('%d %d\n' % e)

    with open(ans, 'w') as f:
        f.write(solution.solve(graph_edges_to_list(n, graph)))

def gen_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        gen_test(tests_dir, t, 2 + i * 2, gen_graph(2 + i * 2, i))
        t += 1

    for i in range(5):
        gen_test(tests_dir, t, 2 + i * 2, gen_graph(2 + i * 2, 0))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph(n, 100))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph(n, 10000))
        t += 1

if __name__ == "__main__":
    gen_tests(sys.argv[1])
