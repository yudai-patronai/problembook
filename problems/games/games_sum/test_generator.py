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
tests.add("3 2\n5 3 6\n", solve(2, [5, 3, 6]))
tests.add("1 6\n14\n", solve(6, [14]))
tests.add("2 2\n4 2\n", solve(2, [4, 2]))
for i in range(5):
    n = random.randint(10, 100)
    k = random.randint(2, 50)
    a = [random.randint(1, 100) for _ in range(n)]
    tests.add("{} {}\n{}\n".format(n, k, " ".join(map(str, a))), solve(k, a))

tests.add("8 3\n4 12 36 5 9 9 12 13\n", solve(3, [4, 12, 36, 5, 9, 9, 12, 13]))
tests.add("6 4\n15 100 12 3 500 6\n", solve(4, [15, 100, 12, 3, 500, 6]))

for i in range(5):
    n = random.randint(200, 1000)
    k = random.randint(5, 500)
    a = [random.randint(20, 500) for _ in range(n)]
    tests.add("{} {}\n{}\n".format(n, k, " ".join(map(str, a))), solve(k, a))
