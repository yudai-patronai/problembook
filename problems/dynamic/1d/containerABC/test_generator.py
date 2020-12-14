#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)
MAX_N = 20


def solve(n):
    d = [[None] * 3 for _ in range(n)]
    d[0] = [1, 1, 1]
    for i in range(1, n):
        d[i][0] = d[i-1][1] + d[i-1][2]
        d[i][1] = d[i][2] = sum(d[i-1])
    return(sum(d[-1]))


def generate_test(name, n):
    with open(name, "w") as f:
        f.write(str(n) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(solve(n)))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    questions = [2, 10, 3, 7, 8]
    questions.extend(random.sample(range(11, MAX_N), 10))
    if MAX_N not in questions:
        questions[-1] = MAX_N

    for test, n in enumerate(questions):
        test_name = os.path.join(test_folder, "%02d" % (test+1))
        print("generating %s..." % test_name)
        generate_test(test_name, n)
