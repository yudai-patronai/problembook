#!/usr/bin/python3
from lib import random
from lib.testgen import TestSet


def solve(a):
    n = len(a)
    ans = ' '.join(map(str, a)) + '\n'
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                ans += ' '.join(map(str, a)) + '\n'
    return ans


NUM_TEST = 10
random.seed(10000)

tests = TestSet()

manual = [
    [-5, 3, 1, 7, 10, -4],
    [9, 2, 4, 2, 9, 5, -1, -8],
]

for A in manual:
    question = ' '.join(map(str, A)) + '\n'
    tests.add(question, solve(A))

for i in range(NUM_TEST - len(manual)):
    A = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]

    question = ' '.join(map(str, A)) + '\n'
    tests.add(question, solve(A))
