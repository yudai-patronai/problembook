from lib.testgen import TestSet
from lib.random import seed, randint


def solution(arr):
    b = sorted(arr)
    return sum(b[i] // 2 + 1 for i in range(len(b) // 2 + 1))


def question(arr):
    return '{}\n{}\n'.format(len(arr), ' '.join(map(str, arr)))


def answer(arr):
    return '{}\n'.format(solution(arr))


tests = TestSet()
def add(arr):
    tests.add(question(arr), answer(arr))


if __name__ == '__main__':
    seed(42)
    for arr in ([1],
                [158],
                [1, 1, 1, 1, 1, 1, 1],
                [2, 45, 7, 6, 33],
                [randint(1, 2000) for _ in range(200)]):
        add(arr)
    # for _ in range(4):
    #     add([randint(1, 100000) for _ in range(randint(1, 10000))])
