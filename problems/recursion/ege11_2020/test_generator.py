import random
from lib.testgen import TestSet


def sol(k):
    NumbersInRecursion = []
    def F(n):
        if n > 2:
            F(int(n / 2))
            F(n - 1)
        NumbersInRecursion.append(n)
    F(k)
    res = int(sum(NumbersInRecursion))
    return res


tests = TestSet()

# 1. Simple tests of negative numbers
tests.add('-1', '-1')
tests.add('-310', '-310')

# 2. Simple tests of positive numbers
tests.add('0', '0')
tests.add('1', '1')
tests.add('2', '2')
tests.add('3', '6')
tests.add('9', '85')
tests.add('20', '850')

# 3. Near INT16_MAX

tests.add('54', '30567')
tests.add('55', '32878')
tests.add('99', '447560')

# 4. Near INT32_MAX

tests.add('400', '1058914824')
tests.add('426', '1586220698')

for k in range(100, 301, 20):
    ans = sol(int(k))
    tests.add('{:d}'.format(k), '{:d}'.format(ans))



