#!/usr/bin/python3

import os
from lib import random
import shutil

random.seed(33)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, 11):
    num = random.randint(100, 999)
    ans = num // 100 + (num % 100) // 10 + num % 10

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write(str(num))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(str(ans))

