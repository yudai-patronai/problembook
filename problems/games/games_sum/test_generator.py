#!/usr/bin/env python3
import random
from lib.testgen import TestSet

def solve(k, a):
    m = max(a)
    d = [None] * (m + 1)
    d[0] = 0
    for i in range(1, m+1):
        used = [False] * (k + 1)
        for j in range(1, k+1):
            if i - j >= 0:
                used[d[i-j]] = True
        for j in range(k+1):
            if not used[j]:
                d[i] = j
                break
    s = 0
    for e in a:
        s ^= d[e]
    if s:
        return "YES\n"
    else:
        return "NO\n"


random.seed(42)
tests = TestSet()
tests.add("4 2\n5 3 6\n", solve(2, [3, 5, 6]))
tests.add("1 6\n15\n", solve(6, [15]))
tests.add("2 2\n4 2\n", solve(2, [4, 2]))
for i in range(5):
    n = random.randint(10, 100)
    k = random.randint(2, 50)
    a = [random.randint(1, 100) for _ in range(n)]
    tests.add("{} {}\n{}\n".format(n, k, " ".join(map(str, a))), solve(k, a))

for i in range(5):
    n = random.randint(200, 500)
    k = random.randint(5, 500)
    a = [random.randint(20, 500) for _ in range(n)]
    tests.add("{} {}\n{}\n".format(n, k, " ".join(map(str, a))), solve(k, a))
