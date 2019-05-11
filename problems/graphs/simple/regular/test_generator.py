#!/usr/bin/python3

import os
from lib import random
import shutil
import heapq

N_TESTS = 9
N_VERTS = 100

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

random.seed(42)

for k in range(1, N_TESTS + 1):
    g = []
    n_verts = random.randint(2, N_VERTS)
    is_regular = random.randint(0, 1)
    if is_regular:
        total_deg = random.randint(0, n_verts-1)
        deg = [0]*n_verts
        verts = []
        if total_deg:
            for i in range(n_verts):
                heapq.heappush(verts, (0, i))
        while verts:
            _, u = heapq.heappop(verts)
            try:
                _, v = heapq.heappop(verts)
            except IndexError:
                break
            g.append((u, v))
            deg[u] += 1
            deg[v] += 1
            if deg[u] != total_deg:
                heapq.heappush(verts, (deg[u], u))
            if deg[v] != total_deg:
                heapq.heappush(verts, (deg[v], v))
    else:
        m = random.randint(1, n_verts*(n_verts-1)//2)
        edges = set()
        for _ in range(m):
            u = random.randint(0, n_verts-2)
            v = random.randint(u+1, n_verts-1)
            while (u, v) in edges:
                u = random.randint(0, n_verts - 2)
                v = random.randint(u + 1, n_verts - 1)
            edges.add((u, v))
        g = [x for x in edges]

    with open(os.path.join(tests_dir, '{0:0>2}'.format(k)), 'w') as fin:
        fin.write('{} {}\n'.format(n_verts, len(g)))
        for edge in g:
            fin.write('{} {}\n'.format(*edge))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(k)), 'w') as fout:
        deg = [0] * n_verts
        for edge in g:
            deg[edge[0]] += 1
            deg[edge[1]] += 1
        for i in range(1, n_verts):
            if deg[i] != deg[i - 1]:
                fout.write('NO\n')
                break
        else:
            fout.write('YES\n')

with open(os.path.join(tests_dir, '{0:0>2}'.format(10)), 'w') as fin:
    fin.write('{} {}\n'.format(1, 0))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(10)), 'w') as fout:
    fout.write('YES\n')
