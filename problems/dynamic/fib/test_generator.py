from lib.testgen import TestSet
from lib.random import randint


def question(n):
    return '{}\n'.format(n)


def fib(n, external_start=True):
    if n <= 1:
        return 1
    global cache
    if external_start:
        cache = [0] * (n + 1)
        cache[:2] = 0, 0
    cache[n] = fib(n - 2, False) + fib(n - 1, False)
    return cache[n]


def answer(n):
    return '{}\n'.format(fib(n))


tests = TestSet()
def add(i):
    tests.add(question(i), answer(i))


add(0)
add(1)
add(21)
add(61)
