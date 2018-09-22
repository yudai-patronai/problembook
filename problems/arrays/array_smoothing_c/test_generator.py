#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

def solve(n, seq):
    res = [int((seq[i - 1] + seq[i] + seq[(i + 1) % n]) / 3) for i in range(len(seq))]
    return ' '.join(map(str, res))

def generate_answer(name, n, seq):
    with open("%s.a" % name, 'w') as f:
        f.write(solve(n, seq))

def write_test(name, seq):
    n = len(seq)
    with open(name, "w") as f:
        f.write('{}\n'.format(n))
        f.write(' '.join(map(str, seq)))
    generate_answer(name, n, seq)

def generate_test(name, testn):
    minn, maxn = 100, 1000
    n = random.randint(minn, maxn)
    seq = [random.randint(1, 50) for _ in range(n)]
    write_test(name, seq)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test("%02d" % 1, [7, 2, 3])
    write_test("%02d" % 2, [39, 2, 36, 13])

    for test_idx in range(3, 8):
        test_name = os.path.join(test_folder, "%02d" % test_idx)
        print("generating %s..." % test_name)
        generate_test(test_name, test_idx)
