#!/usr/bin/env python3

import os
import shutil
import solution
import random

random.seed(42)

def generate_answer(name, n, k, seq):
    with open("%s.a" % name, 'w') as f:
        f.write(solution.solve(n, k, seq))

def generate_test(name, testn):
    minn = 1 if testn < 10 else 10
    maxn = 15 if testn < 10 else 40
    n = random.randint(minn, maxn)
    k = random.randint(1, 5)
    seq = [random.randint(1, 50) for _ in range(n)]
    with open(name, "w") as f:
        f.write(' '.join(map(str, (n, k))) + '\n')
        f.write(' '.join(map(str, seq)))
    generate_answer(name, n, k, seq)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 71):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
