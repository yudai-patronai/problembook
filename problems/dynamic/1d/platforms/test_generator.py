#!/usr/bin/env python3

import os
from lib import random
import shutil
from solution import solve

random.seed(42)

manual_tests = [
    {"task": [1, 5, 10],
     "ans": 9},

    {"task": [1],
     "ans": 0},

    {"task": [20, 14],
     "ans": 6},

    {"task": [5, 22, 10],
     "ans": 15},
]

def generate_manual_test(name, task):
    n = len(task["task"])
    heights = task["task"]
    ans = task["ans"]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        for i in heights:
            f.write(str(i) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))

def generate_test(name, n=None):
    if not n:
        n = random.randint(10, 1000)

    heights = [random.randint(1, 50) for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        for i in heights:
            f.write(str(i) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(solve(n, heights)))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, len(manual_tests) + 1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_manual_test(test_name, manual_tests[test-1])

    #random tests n < 1000
    for test in range(len(manual_tests) + 1, len(manual_tests) + 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

    #big tests
    test_name = os.path.join(test_folder, "%02d" % (test + 1))
    print("generating %s..." % test_name)
    generate_test(test_name, 20000)

    test_name = os.path.join(test_folder, "%02d" % (test + 2))
    print("generating %s..." % test_name)
    generate_test(test_name, 30000)
