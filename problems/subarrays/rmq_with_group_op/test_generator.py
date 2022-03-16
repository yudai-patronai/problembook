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
    a = a[:]
    for cmd, *args in b:
        if cmd == "add":
            f, t, v = args
            for i in range(f, t+1):
                a[i] += v
        else:
            s = 0
            f, t = args
            for i in range(f, t+1):
                s += a[i]
            ans.append("{:.3g}".format(s / (t-f+1)))
    return " ".join(ans)


tests = TestSet()

n = 5
a = [2, 2, 2, 1, 5]
m = 3
b = [("mean", 1, 2), ("add", 1, 3, -1), ("mean", 1, 4)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

n = 3
a = [-4, 2, 6]
m = 3
b = [("mean", 0, 1), ("mean", 0, 2), ("mean", 1, 2)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

n = 12
a = [-23, 4, 2, 90, 0, 4, 34, 2, 6, 1, 0, 8]
m = 2
b = [("add", 5, 9, 6), ("mean", 2, 6)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

n = 1
a = [44]
m = 2
b = [("add", 0, 0, 0), ("mean", 0, 0)]
ans = solve(n, m, a, b)
tests.add(question(n, m, a, b), ans)

for _ in range(5):
    n = randint(100, 1000)
    m = randint(100, 1000)
    a = [randint(-1000, 1000) for _ in range(n)]
    flag = False
    b = []
    for _ in range(m):
        cmd = randint(0, 19)
        cmd = "add" if cmd > 14 else "mean"
        if cmd == "add":
            f = randint(0, n-1)
            t = randint(f, n-1)
            v = randint(-1000, 1000)
            b.append((cmd, f, t, v))
        else:
            flag = True
            f = randint(0, n-1)
            t = randint(f, n-1)
            b.append((cmd, f, t))
    if not flag:
        f = randint(0, n-1)
        t = randint(f, n-1)
        b[-1] = ("mean", f, t)

    q = question(n, m, a, b)
    ans = solve(n, m, a, b)

    tests.add(q, ans)

# some max tests
for _ in range(11):
    n = 30000
    m = 5000
    a = [randint(-1000, 1000) for _ in range(n)]
    flag = False
    b = []
    for _ in range(m):
        cmd = randint(0, 19)
        cmd = "add" if cmd > 14 else "mean"
        if cmd == "add":
            f = randint(0, n-1)
            t = randint(f, n-1)
            v = randint(-1000, 1000)
            b.append((cmd, f, t, v))
        else:
            f = randint(0, n-1)
            t = randint(f, n-1)
            b.append((cmd, f, t))
    if not flag:
        f = randint(0, n-1)
        t = randint(f, n-1)
        b[-1] = ("mean", f, t)
    q = question(n, m, a, b)
    ans = solve(n, m, a, b)
    tests.add(q, ans)
