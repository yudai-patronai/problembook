from lib.testgen import TestSet
from lib.random import randint


def question(n, m, a, b):
    res = "{}\n{}\n{}\n{}\n".format(
        n, " ".join(map(str, a)),
        m, "\n".join(map(lambda x: " ".join(map(str, x)), b))
    )
    return res


def solve(n, m, a, b):
    ans = []
    for x, y in b:
        cur = float("-inf")
        for i in range(x, y+1):
            cur = max(cur, a[i])
        ans.append(str(cur))
    return " ".join(ans)


tests = TestSet()

n = 5
a = [2, 2, 2, 1, 5]
m = 2
b = [(1, 2), (1, 4)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

n = 3
a = [-4, 2, 6]
m = 3
b = [(0, 1), (0, 2), (1, 2)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

n = 12
a = [-23, 4, 2, 90, 0, 4, 34, 2, 6, 1, 0, 8]
m = 2
b = [(5, 9), (2, 6)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

n = 1
a = [44]
m = 2
b = [(0, 0), (0, 0)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

for _ in range(5):
    n = randint(100, 1000)
    m = randint(100, 1000)
    a = [randint(-1000, 1000) for _ in range(n)]
    b = [
        tuple(sorted([randint(0, n-1), randint(0, n-1)]))
        for _ in range(m)
    ]

    q = question(n, m, a, b)
    ans = solve(n, m, a, b)

    tests.add(q, ans)

n = 100000
m = 30000
a = [randint(-1000, 1000) for _ in range(n)]
b = [
    tuple(sorted([randint(0, n-1), randint(0, n-1)]))
    for _ in range(m)
]
q = question(n, m, a, b)
ans = solve(n, m, a, b)
tests.add(q, ans)
