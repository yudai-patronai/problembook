from lib.testgen import TestSet
from lib.random import randint

tests = TestSet()

def solve(a, b):
    a = set(a)
    b = set(b)
    return "{} {} {}\n".format(len(a), len(b), len(a&b))


def to_str(n, m, a, b):
    return "{} {}\n{}\n{}\n".format(n, m, ' '.join(map(str, a)), ' '.join(map(str, b)))

tests.add(to_str(3, 3, [1, 4, 9], [2, 2, 3]), solve([1, 4, 9], [2, 2, 3]))
tests.add(to_str(4, 2, [7, 3, 3, 8], [3, 8]), solve([7, 3, 3, 8], [3, 8]))
tests.add(to_str(2, 3, [4, 5], [0, 7, 6]), solve([4, 5], [0, 7, 6]))
for i in range(3):
    n = randint(20, 100)
    m = randint(20, 100)
    a = [randint(-100, 100) for _ in range(a)]
    b = [randint(-100, 100) for _ in range(b)]

    tests.add(to_str(n, m, a, b), solve(a, b))
for i in range(2):
    n = randint(100, 500)
    m = randint(100, 500)
    a = [randint(-100, 100) for _ in range(a)]
    b = [randint(-100, 100) for _ in range(b)]
    tests.add(to_str(n, m, a, b), solve(a, b))

a = [randint(-100000, 100000) for _ in range(1000)]
b = [randint(-100000, 100000) for _ in range(1000)]
tests.add(to_str(1000, 1000, a, b), solve(a, b))
