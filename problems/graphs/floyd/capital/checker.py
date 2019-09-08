#!/usr/bin/python3

import heapq
import sys

with open(sys.argv[1]) as fin:
    n, m = map(int, fin.readline().split())

    g = {k: set() for k in range(n)}

    for i in range(m):
        f, t, w = map(int, fin.readline().split())
        g[f].add((t, w))
        g[t].add((f, w))

with open(sys.argv[2]) as fout:
    try:
        res = int(fout.readline())
    except:
        print('PE')
        sys.exit(2)

with open(sys.argv[3]) as fans:
    ans = int(fans.readline())

if res == ans:
    print('OK')
    sys.exit(0)

summ = {}

for i in [res, ans]:
    dist = [float('+inf')] * n

    q = [(0, i)]

    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue

        dist[v] = d

        for s, w in g[v]:
            if dist[s] > dist[v] + w:
                heapq.heappush(q, (dist[v] + w, s))

    summ[i] = sum(dist)

if summ[res] == summ[ans]:
    print('OK')
    sys.exit(0)
else:
    print('Correct distance is {}, but your distance is {}'.format(sum[ans], sum[res]))
    sys.exit(1)
