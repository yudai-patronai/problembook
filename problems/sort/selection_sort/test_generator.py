from lib.testgen import TestSet
from lib import random

NUM_TEST = 10
random.seed(10000)


def selection_sort(a):
    a_states = []
    a_states.append(' '.join(map(str, a)))
    for i in range(0, len(a) - 1):
        min_j = i
        for j in range(i, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
        a_states.append(' '.join(map(str, a)))
    return a_states


def add_test(tests:TestSet, array):
    a = array.copy()
    question = ' '.join(map(str, a)) + '\n'
    sort_states = selection_sort(a)
    answer = '\n'.join(sort_states) + '\n'
    tests.add(question, answer)


tests = TestSet()

manual = [
    [3, 1, -1, 2],
    [3, 1, 2, 2, -1],
    [8, -12, 94, 23, 12, -18]
]

for array in manual:
    add_test(tests, array)

for i in range(NUM_TEST-len(manual)):
    n = random.randint(10, 20)
    array = [random.randint(-1000, 1000) for _ in range(n)]
    add_test(tests, array)
