from lib.testgen import TestSet


def num(N):
    return str(N) + '\n'


tests = TestSet()
tests.add(*map(num, [5, 3]))
tests.add(*map(num, [32718, 17]))
tests.add(*map(num, [6, 2]))
tests.add(*map(num, [8, 3]))
tests.add(*map(num, [1024, 10]))
tests.add(*map(num, [32719, 18]))
tests.add(*map(num, [3**8+2, 10]))
tests.add(*map(num, [95791, 19]))
