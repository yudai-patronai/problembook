#!/usr/bin/env python3
import os
from lib import random
import shutil

import slow_solution

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
random.seed(100)


def rand_numbers(sequence, n):
    return [random.choice(sequence) for i in range(n)]


def gen_test(tests_dir, sequence):
    if not hasattr(gen_test, 'ind'):
        gen_test.ind = 1
    else:
        gen_test.ind += 1

    print(gen_test.ind, len(sequence))

    test = os.path.join(tests_dir, '%.2d' % gen_test.ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(' '.join(map(str, sequence)) + '\n')

    with open(ans, 'w') as f:
        slow_solution.solve(sequence, f)


shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, 21):
    gen_test(tests_dir, rand_numbers(range(1, i * 5), i * 3))
    gen_test(tests_dir, rand_numbers(range(1, i * 10), i * 3))

gen_test(tests_dir, [100])
gen_test(tests_dir, range(100))
gen_test(tests_dir, range(100, 0, -1))
gen_test(tests_dir, [1] * 100)
gen_test(tests_dir, [1, 2, 3, 4, 5] * 100)

for _ in range(5):
    n = random.randint(5000, 10000)
    gen_test(tests_dir, [random.randint(0, 1000) for _ in range(n)])

gen_test(tests_dir, [i for i in range(10000)])
gen_test(tests_dir, [1000 - i for i in range(10000)])
a = [i for i in range(10000)]
for i in range(1, 10000, 2):
    a[i-1],a[i] = a[i],a[i-1]
gen_test(tests_dir, a)
