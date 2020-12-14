from lib.testgen import TestSet
import lib.random as rand


def f(x):
    return x * x + x ** 0.5


def solve(c):
    left = 0
    right = c
    while True:
        m = (right + left) / 2
        y = f(m)
        if abs(y - c) < 1e-6:
            return m
        elif y > c:
            right = m
        else:
            left = m


tests = TestSet()

tests.add('2\n', '1\n')
tests.add('18\n', '4\n')

USUAL_TESTS_COUNT =5
for _ in range(USUAL_TESTS_COUNT):
    c = rand.random() * 1000000
    x = solve(c)
    tests.add('{:f}\n'.format(c), '{:.06f}\n'.format(x)

c = 10 ** 10
x = solve(c)
tests.add('{:f}\n'.format(c), '{:.06f}\n'.format(x)
