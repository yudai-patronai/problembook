#!/usr/bin/python3

import os
from lib import random
import shutil

N_TESTS = 50
N_VERTS = 50

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

random.seed(42)

for k in range(1, N_TESTS + 1):
    g = []
    n_verts = random.randint(1, N_VERTS)

    n_components = 1 if k % 2 == 0 else random.randint(2, N_VERTS)
    components = [[] for i in range(n_components)]
    for i in range(n_verts):
        components[random.randrange(n_components)].append(i)

    components = [c for c in components if c]
    n_components = len(components)

    for c in components:
        edges = set()
        for edge in zip(c, c[1:]):
            edges.add(edge)
        for i in range(random.randrange(0, len(c))):
            edge_from = random.choice(c)
            edge_to = random.choice(c)
            edge_from, edge_to = min(edge_from, edge_to), max(edge_from, edge_to)
            if edge_from != edge_to:
                edges.add((edge_from, edge_to))
        g.extend(edges)

    with open(os.path.join(tests_dir, '{0:0>2}'.format(k)), 'w') as fin:
        fin.write('{}\n{}\n'.format(n_verts, len(g)))
        for edge in g:
            fin.write('{} {}\n'.format(*edge))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(k)), 'w') as fout:
        fout.write('YES' if n_components == 1 else 'NO')
