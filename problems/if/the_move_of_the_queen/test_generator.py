from lib.random import randint, seed
from lib.testgen import TestSet

seed(42)
tests = TestSet()

for i in range(10):
    x1 = randint(1, 8)
    y1 = randint(1, 8)
    x2 = randint(1, 8)
    y2 = randint(1, 8)

    while x1 == x2 and y1 == y2:
        x2 = randint(1, 8)
        y2 = randint(1, 8)

    ans = 'YES' if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2 else 'NO'

    tests.add(
        '{0}\n{1}\n{2}\n{3}\n'.format(x1, y1, x2, y2),
        ans
    )
