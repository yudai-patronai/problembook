from lib.testgen import TestSet
from lib.random import randint, seed


def question(n):
    return '{}\n'.format(n)


def solve(n):
    arr = [0] * 10
    while n > 0:
        arr[n % 10] += 1
        n //= 10

    for i in range(1, 10):
        if arr[i] > 0:
            digit = str(i)
            arr[i] -= 1
            break

    return digit + \
        ''.join(map(lambda i: str(i) * arr[i], range(10)))


def answer(n):
    return solve(n) + '\n'


tests = TestSet()
def add(i):
    tests.add(question(i), answer(i))


seed(42)
add(1)
add(randint(2, 9))
add(randint(1, 9) * 10)
add(randint(11, 99) * 10 ** 90)
add(randint(101, 999) * 10 ** 80)

for _ in range(7):
    add(randint(10 ** 3, 10 ** 10) * 10 ** randint(20, 80) + \
        randint(100, 10 ** 40))

add(10 ** 100 - randint(1, 9))
add(10 ** 100)
