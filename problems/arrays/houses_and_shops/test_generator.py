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
    for test in range(1, 21):
        N = 2 + random.randint(1, test // 10 * 100 + test * 10)
        A = ["1", "2"] + [random.choice(["0", "1", "2"]) for i in range(N - 2)]
        random.shuffle(A)

        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(str(N) + "\r\n")
            f.write(" ".join(map(str, A)))
        generate_answer(test_name, N, A)
