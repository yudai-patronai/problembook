#!/usr/bin/python3

import os
import shutil
# from lib import random

NUM_TEST = 50
# random.seed(10000)

manual_tests = [(1, 2, 2, 3, 1), (2, 1, 0, 1, 2), (1, 2, 3, 2, 2), (1, 3, 2), (2, 1, 3)]

def generate_test(name, task, ans):
    with open(name, "w") as f:
        f.write(str(len(task)) + '\n')
        f.write(' '.join(map(str, task)))
    # answer
    with open("%s.a" % name, 'w') as f:
        f.write(ans)

def extreme_points(N, x):
    assert N == len(x)

    if N == 1 or N == 2:
        return ''

    buf = []
    for i in range(1, N-1):
        if x[i-1] > x[i] < x[i+1] or x[i-1] < x[i] > x[i+1]:
            buf.append(i)

    return ' '.join(map(str, buf))

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

for i in range(1, len(manual_tests) + 1):
    test_name = os.path.join(test_dir, "%02d" % i)
    task = manual_tests[i-1]
    ans = extreme_points(len(task), task)
    print("generating %s..." % test_name)
    generate_test(test_name, task, ans)

# random tests
# for test in range(len(manual_tests) + 1, len(manual_tests) + 7):
#     test_name = os.path.join(test_dir, "%02d" % test)
#     print("generating %s..." % test_name)
#     generate_test(test_name)
