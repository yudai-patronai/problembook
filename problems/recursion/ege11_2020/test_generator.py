import random
from lib.testgen import TestSet


global NumbersInRecursion

def sol(k):
    NumbersInRecursion = []
    def F(n):
        if n > 2:
            F(int(n))
            F(n - 1)
        NumbersInRecursion.append()
    F(k)
    res = sum(NumberInRecusion)
    return res


tests = TestSet()

# 1. Simple tests of negative numbers
tests.add('-1', '-1')
tests.add('-310', '-310')
tests.add('-32766', '-32766')

# 2. Simple tests of positive numbers
tests.add('0', '0')
tests.add('1', '1')
tests.add('2', '2')
tests.add('3', '6')
tests.add('9', '85')
tests.add('20', '850')

# 3. Near INT16_MAX

tests.add('54', '30567')
tests.add('55', '32767')
tests.add('99', '447560')

# 4. Near INT32_MAX

tests.add('400', '1058914824')
tests.add('426', '1586220698')
tests.add('444', '2074041907')
tests.add('453', '2363558241')

for num in range(20):
    k = random.randrange(-100, 100)
    ans = sol(k)
    tests.add("{}".format(k), "{}".format(ans))
