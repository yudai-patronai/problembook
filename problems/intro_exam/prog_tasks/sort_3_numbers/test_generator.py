from lib.testgen import TestSet
from lib.random import randint


def question(arr):
    return '\n'.join(map(str, arr)) + '\n'

def ans(arr):
    return ' '.join(map(str, arr)) + '\n'

def random_arr():
    return [randint(-100, 100) for _ range(3)]

tests = TestSet()

for _ in range(10):
    arr = gen_arr()

    arr_sorted = sorted(arr)

    tests.add(question(arr), ans(arr_sorted))
