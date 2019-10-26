from lib.testgen import TestSet
from lib.random import randint


def question(n):
    return '{}\n'.format(n)


def answer(n):
    return 'NO\n' if n in [0, 2, 3, 5, 8] else 'YES\n'


tests = TestSet()
def add(i):
    tests.add(question(i), answer(i))


list(map(add, [12, 8, 1]))  # visible tests
list(map(add, range(2, 8)))
list(map(add, [0, 9, 10, 11, 13, 14, 15]))
list(map(add, [
    randint(16, 99), randint(100, 999), randint(1000, 9999), \
    randint(10000, 29989), randint(29990, 29994), \
    randint(29995, 29999), 30000]))
