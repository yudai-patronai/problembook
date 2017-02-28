#!/usr/bin/python3

import heapq
import sys

with open(sys.argv[1]) as fin:
    n, m = map(int, fin.readline().split())

    g = {k:set() for k in range(n)}

    for i in range(m):
        f, t, w = map(int, fin.readline().split())
        g[f].add((t, w))
        g[t].add((f, w))

with open(sys.argv[2]) as fout:
    try:
        res = int(fout.readline())
    except:
        sys.exit(2)

with open(sys.argv[3]) as fans:
    ans = int(fans.readline())

if res == ans:
    sys.exit(0)

summ = {}

for i in [res, ans]:
    dist = [float('+inf')]*n

    q = [(i, 0)]

    while q:
        v, d = heapq.heappop(q)
        if dist[v] < d:
            continue

        dist[v] = d

        for s, w in g[v]:
            if dist[s] > dist[v] + w:
                heapq.heappush(q, (s, dist[v] + w))

    summ[i] = sum(dist)

sys.exit(0 if summ[res] == summ[ans] else 1)
