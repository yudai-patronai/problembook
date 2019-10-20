from lib.testgen import TestSet
from lib.random import randint


def random_digits(size):
    return [ randint(0, 9) for _ in range(size) ]


def question(array):
    return ' '.join(map(str, array)) + '\n'


def answer(question_array):
    quantities = [0] * 10
    sorted_arr = list(sorted(question_array))

    s = ''
    for x in question_array:
        quantities[x] += 1
        s += ' '.join(map(str, quantities)) + '\n'
    
    s += ' '.join(map(str, sorted_arr)) + '\n'

    return s

tests = TestSet()

arr = [9, 2, 3, 4, 2, 8, 5, 2, 9, 0, 2, 7, 6, 5, 2]
tests.add(
    question([9, 2, 3, 4, 2, 8, 5, 2, 9, 0, 2, 7, 6, 5, 2]),
    answer(arr)
)

for size in [20, 20, 100]:
    arr = random_digits(size)
    tests.add(
        question(arr),
        answer(arr)
    )
