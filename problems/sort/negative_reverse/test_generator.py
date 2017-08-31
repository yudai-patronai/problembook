#!/usr/bin/python3

import os
import random
import shutil

N = 50
MAX_L = 500

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N + 1):
    l = random.randint(2, MAX_L)
    if i == 1:
        l1 = 0
    elif i == 2:
        l1 = l
    else:
        l1 = random.randint(1, l - 1)
    l2 = l - l1

    negative = []
    positive = []

    k = 1
    for j in range(l1):
        negative.append(-k)
        k += random.randint(0, 100)

    k = random.randint(0, 1)
    for j in range(l2):
        positive.append(k)
        k += random.randint(0, 100)

    ans = negative + positive
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(' '.join(map(str, ans)))

    random.shuffle(ans)
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write(' '.join(map(str, ans)))
