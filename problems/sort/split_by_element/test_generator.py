from lib.testgen import TestSet

def question(arr, barrier):
    return ' '.join(map(str, arr)) + '\n' + str(barrier) + '\n'

def answer(arr):
    return ' '.join(map(str, arr)) + '\n'

tests = TestSet()

arrays = [
    (
        [3, 4, 2, 0, 6, 6], #  input array
        3,                  #  barrier
        [2, 0, 3, 4, 6, 6]  #  output array
    ),
    (
        [3, 4, 2, 0, 6, 6],
        1,
        [0, 3, 4, 2, 6, 6]
    ),
    (
        [3, 4, 2, 0, 6, 6],
        5,
        [3, 4, 2, 0, 6, 6]
    ),
    (   [10, 7, 4, 1, 8, 1, 12, 5, 7, 9, 4, 3, 2, 12, 2],
        8,
        [7, 4, 1, 1, 5, 7, 4, 3, 2, 2, 8, 10, 12, 9, 12]
    )
]

for inp, barrier, out in arrays:
    tests.add(
        question(inp, barrier),
        answer(out)
    )