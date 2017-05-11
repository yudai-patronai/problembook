#!/usr/bin/python3

import os
import shutil
import random

N = 50

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N+1):
    x1 = random.randint(1, 8)
    y1 = random.randint(1, 8)
    x2 = random.randint(1, 8)
    y2 = random.randint(1, 8)
    while x1 == x2 and y1 == y2:
        x2 = random.randint(1, 8)
        y2 = random.randint(1, 8)


    ans = 'YES' if abs(x1 - x2) == abs(y1 - y2) else 'NO'

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n{1}\n{2}\n{3}\n".format(x1, y1, x2, y2))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(ans)
