#!/usr/bin/env python3

import os
from lib import random
import shutil

import solution

random.seed(42)

manual_tests = [
    {"task": [1, 2, 3, 4, 5, 4, 3, 2, 1],
     "ans": (0, [])},

    {"task": [1, 2, 1, 2, 2],
     "ans": (3, [1, 2, 1])},

    {"task": [1],
     "ans": (0, "")},
]

def generate_manual_test(name, task):
    seq = task["task"]
    n = len(seq)
    ans = task["ans"]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, seq)))
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans[0]) + '\n')
        f.write(' '.join(map(str, ans[1])))


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
    #manual
    for test in range(1, len(manual_tests) + 1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_manual_test(test_name, manual_tests[test - 1])
    #random
    for test in range(len(manual_tests) + 1, len(manual_tests) + 4):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, random.randint(5, 15))

    for test in range(len(manual_tests) + 4, len(manual_tests) + 8):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, random.randint(20, 40))

    #big test
    test_name = os.path.join(test_folder, "%02d" % (test + 1))
    print("generating %s..." % test_name)
    generate_test(test_name, 90)

    # big test
    test_name = os.path.join(test_folder, "%02d" % (test + 2))
    print("generating %s..." % test_name)
    generate_test(test_name, 100)
