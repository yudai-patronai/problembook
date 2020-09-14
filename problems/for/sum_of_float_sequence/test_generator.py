from lib.testgen import TestSet
from lib.random import seed, random, randint


seed(142)


def gen_array(size):
    return [ round(randint(-100, 100) + random(), 6) for _ in range(size)]

def question(array):
    return str(len(array)) + '\n' + '\n'.join(map(str, array)) + '\n'

def answer(array):
    s = float(sum(array))
    return str(round(s, 4)) + '\n'


tests = TestSet()

a = [10.99, 0, -1.01]
tests.add(question(a), answer(a))

a = [1, -2, 3, 5]  # только целые
tests.add(question(a), answer(a))

for _ in range(7):
    size = randint(10, 1000)
    array = gen_array(size)
    tests.add(question(array), answer(array))

a = []  # пустая последовательность
tests.add(question(a), answer(a))
