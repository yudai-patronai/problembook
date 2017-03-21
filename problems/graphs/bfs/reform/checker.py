#!/usr/bin/python3
import sys
import os
import bisect

class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата

def dijkstra(graph, x, y):
    parent = [-1] * len(graph)

    if x == y:
        return (0, parent)

    dist = [float('+inf') for _ in graph]
    queue = [(0, x)]
    dist[x] = 0

    while queue:
        vd, v = queue.pop(0)
        if v == y:
            return (vd, parent)

        for v2, r in graph[v]:
            if dist[v2] > dist[v] + r:
                i = bisect.bisect_left(queue, (dist[v2], v2))
                if i < len(queue) and queue[i][1] == v2:
                    del queue[i]
                dist[v2] = dist[v] + r
                parent[v2] = v
                bisect.insort(queue, (dist[v2], v2))

    return (None, None)

# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 3:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[2]

with open(input_file) as f:
    n, m, *centers = map(int, f.readline().split()) 
    graph = [[] for i in range(n)]
    for line in f.readlines():
        a, b, w = map(int, line.split())
        graph[a].append((b, w))
        graph[b].append((a, w))

with open(answer_file) as f:
    ans = list(map(int, f.readlines()))

try:
    with open(output_file) as f:
        outp = list(map(int, f.readlines()))
except (IOError, ValueError):
    print('FAIL1')
    sys.exit(CheckerResult.PE)

if len(outp) != n:
    print('FAIL2')
    sys.exit(CheckerResult.PE)

if not set(outp).issubset(centers + [-1]):
    print('FAIL3')
    print(outp)
    print(centers)
    sys.exit(CheckerResult.PE)

for x in range(n):
    if ans[x] == outp[x]:
        continue
    if dijkstra(graph, x, ans[x])[0] != dijkstra(graph, x, outp[x])[0]:
        print('FAIL4')
        sys.exit(CheckerResult.PE)

print('OK')
sys.exit(CheckerResult.OK)
