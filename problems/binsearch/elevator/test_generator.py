from lib.testgen import TestSet
import lib.random as rand


base = 10
digits = range(base)
def gen_num(digit_count):
    num = 0
    for _ in range(digit_count):
        num = base * num + rand.choice(digits)
    return num


def bin_search(n, x, greater_or_equal):
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if greater_or_equal(m, x):
            l, r = l, m
        else:
            l, r = m+1, r
    return l


tests = TestSet()

# tests.add('...\n', '...\n')
