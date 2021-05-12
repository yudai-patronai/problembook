#!/usr/bin/env python3
import random
from lib.testgen import TestSet

def solve(n, m):
    d = [[None] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            d[i][j] = False
            if i-1 >= 0 and j-2 >= 0:
                d[i][j] = (not d[i-1][j-2]) or d[i][j]
            if i-2 >= 0 and j-1 >= 0:
                d[i][j] = (not d[i-2][j-1]) or d[i][j]
    if d[-1][-1]:
        return "YES\n"
    else:
        return "NO\n"


random.seed(42)
tests = TestSet()
tests.add("4 4\n", "NO\n")
tests.add("5 1\n", "NO\n")
tests.add("2 3\n", "YES\n")
tests.add("3 3\n", "NO\n")
for i in range(5):
    n = random.randint(10, 100)
    m = random.randint(10, 100)
    tests.add("{} {}\n".format(n, m), solve(n, m))

for i in range(5):
    n = random.randint(200, 500)
    m = random.randint(200, 500)
    tests.add("{} {}\n".format(n, m), solve(n, m))
