from lib.testgen import TestSet

def join_all(arr):
    return ' '.join(map(str, arr)) + '\n'

def question(arr, k):
    return join_all(arr) + str(k) + '\n'

def answer(arr):
    return join_all(arr)

tests = TestSet()

tests.add(
    question([0, 1, 2, 3], 1),
    answer(  [1, 0, 3, 2])
)
tests.add(
    question(['ru', 'mipt', 'cs'], 2),
    answer(  ['cs', 'mipt', 'ru'])
)
tests.add(
    question([0, 1, 2, 3], 4),
    answer(  [0, 1, 2, 3])
)
tests.add(
    question([0, 1, 2, 3], 100),
    answer(  [0, 1, 2, 3])
)
tests.add(
    question([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    answer(  [5, 6, 7, 8, 9, 0, 1, 2, 3, 4])
)
tests.add(
    question([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
    answer(  [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 10])
)