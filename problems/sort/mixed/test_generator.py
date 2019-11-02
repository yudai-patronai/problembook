from lib.testgen import TestSet
from lib.random import randint


def random_digits(size):
    return [ randint(-100, 100) for _ in range(size) ]


def question(array):
    return ' '.join(map(str, array)) + '\n'


def answer(arr):
    s = ''
    for j in range(len(arr)):
        chg = 0
        pp = -1
        pn = -1
        for i in range(len(arr)):
            if (arr[i] >= 0:
                if pp >= 0 and arr[i] < arr[pp]:
                    arr[i], arr[pp] = arr[pp], arr[i]
                    s += ' '.join(map(str, arr)) + '\n'
                    chg += 1
                pp = i
            else:
                if pn >= 0 and arr[i] > arr[pn]:
                    arr[i], arr[pn] = arr[pn], arr[i]
                    s += ' '.join(map(str, arr)) + '\n'
                    chg += 1
                pn = i
        if chg == 0:
            break
    return s

tests = TestSet()

for size in [5, 10, 15, 20, 25, 30]:
    arr = random_digits(size)
    tests.add(
        question(arr),
        answer(arr)
    )

