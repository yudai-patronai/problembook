#!/usr/bin/env python3

import os
from lib import random
import shutil
from solution import solve

random.seed(42)

manual_tests = [
    {"task": (4, 10),
     "ans": 2},

    {"task": (8, 10),
     "ans": 5},

    {"task": (360, 1000),
     "ans": 179},

    {"task": (1000, 10000),
     "ans": 5939}
]


def gen_test(name, k, p, ans):
    with open(name, "w") as f:
        f.write(str(k) + '\n')
        f.write(str(p) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))


def generate_manual_test(name, task):
    k, p = task["task"]
    gen_test(name, k, p, task["ans"])


def generate_test(name):
    k = random.randint(100, 999)
    while k in [a["task"][0] for a in manual_tests]:
        k = random.randint(100, 999)
    p = 10 ** len(str(k))
    gen_test(name, k, p, solve(k, p))

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    # manual tests
    for test, task in enumerate(manual_tests):
        test_name = os.path.join(test_folder, "%02d" % (test + 1))
        print("generating %s..." % test_name)
        generate_manual_test(test_name, task)
    # random tests
    for test in range(len(manual_tests) + 1, len(manual_tests) + 15):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)
