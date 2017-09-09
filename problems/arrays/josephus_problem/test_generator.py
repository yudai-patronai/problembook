#!/usr/bin/env python3

import os
from lib import random
import shutil

import solution


def generate_answer(name, n, A):
    with open("%s.a" % name, 'w') as f:
        f.write(str(solution.solve(n, A)))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 51):
        N = random.randint(1, 100)
        K = random.randint(1, 10 ** (1 + test // 6))
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(str(N) + " " + str(K))
        generate_answer(test_name, N, K)
