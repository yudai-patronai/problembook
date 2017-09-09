#!/usr/bin/python3

import os
from lib import random
import shutil

N = 50
MAX_L = 10000

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N + 1):
    l = random.randint(1, MAX_L)
    if i == 1:
        l1 = 0
    elif i == 2:
        l1 = l
    else:
        l1 = random.randint(2, l - 1)
    l2 = l - l1

    even = []
    odd = []

    k = 0
    for j in range(l1):
        even.append(k)
        k += 2 * random.randint(0, 100)

    k = 1
    for j in range(l2):
        even.append(k)
        k += 2 * random.randint(0, 100)

    ans = even + odd
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(' '.join(map(str, ans)))

    random.shuffle(ans)
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write(' '.join(map(str, ans)))
