#!/usr/bin/python3

import os
import shutil
import random

N = 50
MAX_L = 1000

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N+1):
    l = random.randint(1, MAX_L)
    if i == 1:
        c = 0
    elif i == 2:
        c = l
    else:
        c = random.randint(0, l-1)

    ans = sorted([random.randint(1, l*10) for j in range(l)])

    while c > 0:
        pos = random.randint(0, l-1)
        if ans[pos] != 0:
            ans[pos] = 0
            c -= 1

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(' '.join(map(str, ans)))

    positions = [k for k, x in enumerate(ans) if x > 0]
    for j in range(len(positions)-1, 1, -1):
        k = random.randint(0, j)
        y = positions[j]
        z = positions[k]
        ans[y], ans[z] = ans[z], ans[y]
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write(' '.join(map(str, ans)))
