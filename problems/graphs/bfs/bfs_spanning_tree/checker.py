#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath('../..'))
import task

class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата

# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 3:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]

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

with open(input_file) as f:
    n, m = map(int, f.readline().split())
    edges = set()
    for l in f.readlines():
        a, b = map(int, l.split())
        if a < b:
            edges.add((a, b))
        else:
            edges.add((b, a))

try:
    with open(output_file) as f:
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

if len(sub) != n - 1:
    print('FAIL')
    sys.exit(CheckerResult.PE)

vert = set([i for e in sub for i in e])

if len(vert) == n and sub.issubset(edges) and \
        bfs_is_connective(task.edges_to_graph(n, list(sub))):
    print('OK')
    sys.exit(CheckerResult.OK)
else:
    print('FAIL')
    sys.exit(CheckerResult.WA)
