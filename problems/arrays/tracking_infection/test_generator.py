#!/usr/bin/env python3

import os
from lib import random
import shutil

NUM_RANDOM_TESTS = 10
random.seed(2020)

manual = {
    "test": [
        [0, 50],
        [1, 0, 2, 1, 3, 2, 4, 3, 5, 4],
        [4, 5, 3, 4, 2, 3, 1, 2, 0, 1],
        [1, 5, 3, 4, 0, 1, 1, 2, 4, 5]
    ],
    "answer": [
        [2],
        [1],
        [6],
        [3]
    ]
}

def generate_answer(name, n, seq):
    seq.reverse()
    r = [False] * 100
    r[0] = True
    for s in seq:
        if r[s[0]]:
            r[s[1]] = True
    haz = 0
    for el in r:
        if el:
            haz += 1
    with open(name + '.a', "w") as f:
        f.write(str(haz) + '\n')

def generate_test(name, testn):
    maxn = 5 if testn < 5 else 10000000
    n = random.randint(5, maxn)
    seqf = [[random.randint(0, 99), random.randint(99)] for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        f.write("\n".join(map(str, [" ".join([str(p[0]), str(p[1])]) for p in seqf])))
    generate_answer(name, n, seqf)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for idx, (test, answer) in enumerate(zip(manual["test"], manual["answer"])):
        test_name = os.path.join(test_folder, "%02d" % (idx + 1,))
        with open(test_name, "w") as f:
            f.write("{}\n".format(int(len(test)/2)))
            f.write(" ".join(map(str, test)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(map(str, answer)))
    for test in range(len(manual["test"])+1, len(manual["test"])+NUM_RANDOM_TESTS+1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
