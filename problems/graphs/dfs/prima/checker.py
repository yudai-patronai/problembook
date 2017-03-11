#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath('../..'))

class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата

# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 3:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[3]

def bfs_is_connective(graph):
    found = [False] * len(graph)
    queue = [0]
    found[0] = True
    nb_found = 1

    while queue:
        v = queue.pop(0)
        for v2 in graph[v]:
            if not found[v2]:
                found[v2] = True
                queue.append(v2)
                nb_found += 1

    return nb_found == len(graph)


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

with open(answer_file) as f:
    min_weight = int(f.readline().rstrip())

with open(input_file) as f:
    n, m = map(int, f.readline().split())
    edges = {}
    for l in f.readlines():
        a, b, w = map(int, l.split())
        if a < b:
            edges[(a, b)] = w
        else:
            edges[(b, a)] = w

try:
    with open(output_file) as f:
        o_weight = int(f.readline().rstrip())
        sub = set()
        for l in f.readlines():
            a, b = map(int, l.split())
            if a < b:
                sub.add((a, b))
            else:
                sub.add((b, a))
except (IOError, ValueError):
    print('FAIL')
    sys.exit(CheckerResult.PE)

if o_weight != min_weight:
    print('FAIL')
    sys.exit(CheckerResult.WA)

if len(sub) != n - 1:
    print('FAIL')
    sys.exit(CheckerResult.WA)

vert = set([i for e in sub for i in e])

if len(vert) == n and sub.issubset(edges) and \
        bfs_is_connective(edges_to_graph(n, list(sub))) and \
        sum([edges[e] for e in sub]) == min_weight:
    print('OK')
    sys.exit(CheckerResult.OK)
else:
    print('FAIL')
    sys.exit(CheckerResult.WA)
