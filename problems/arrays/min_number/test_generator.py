#!/usr/bin/env python3

import os
from lib import random
import shutil

import solution

random.seed(42)

manual_tests = [ (1, 1), (4321, 1234), (1990, 1099), (1000, 1000)]

def generate_manual_test(name, task):
    n = task[0]
    ans = task[1]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
    # answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))

def generate_test(name):
    n = random.randint(100, 100000)
    with open(name, "w") as f:
        f.write(str(n) + '\n')
    # answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(solution.solve(n)) + '\n')

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, len(manual_tests) + 1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_manual_test(test_name, manual_tests[test-1])

    # random tests
    for test in range(len(manual_tests) + 1, len(manual_tests) + 7):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)
