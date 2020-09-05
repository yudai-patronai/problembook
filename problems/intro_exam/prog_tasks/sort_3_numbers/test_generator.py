from lib.testgen import TestSet
from lib.random import randint, seed

seed(18)


def question(arr):
    return '\n'.join(map(str, arr)) + '\n'

def answer(arr):
    return ' '.join(map(str, arr)) + '\n'

def random_arr():
    return [randint(-100, 100) for _ in range(3)]

tests = TestSet()

for _ in range(9):
    arr = random_arr()

    arr_sorted = sorted(arr)

    tests.add(question(arr), answer(arr_sorted))

tests.add(question([10, -8, -8]), answer([-8, -8, 10]))
