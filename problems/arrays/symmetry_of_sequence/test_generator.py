#!/usr/bin/env python3

import os
import random
import shutil

import solution

random.seed(42)


def generate_answer(name, n, seq):
    with open("%s.a" % name, 'w') as f:
        f.write(solution.solve(n, seq))


def makePalindrome(n):
    half = [random.randint(1, 9) for i in range(n // 2)]
    p = half + ([random.randint(1, 9)] if n % 2 else []) + half[::-1]
    return p


def generate_task(n):
    p = makePalindrome(n)
    task_len = random.randint(n // 2 + 1, n)
    return task_len, p[:task_len]


def generate_test(name, n):
    l, seq = generate_task(n)
    with open(name, "w") as f:
        f.write(str(l) + '\n')
        f.write(' '.join(map(str, seq)))
    generate_answer(name, l, seq)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 71):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
