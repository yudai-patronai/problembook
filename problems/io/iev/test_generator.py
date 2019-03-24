#!/usr/bin/python3

import os
import shutil
from lib import random

N = 20
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

p = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
for i in range(1, N + 1):
    k = [random.randint(0, 20000) for _ in range(6)]
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write(" ".join(map(str, k)) + "\n")
    
    a = 0
    for x, y in zip(k, p):
        a += x * y
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write("{}\n".format(a))
