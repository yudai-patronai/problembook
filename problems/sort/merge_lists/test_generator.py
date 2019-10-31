from lib.testgen import TestSet
from lib.random import randint


NUMBER_OF_RANDOM_TESTS = 7
RANDOM_ARRAY_SIZE = 25
RANDOM_ARRAY_ELEMENT_MINMAX = (-100, 100)


def question(L, R):
    return ' '.join(map(str, L)) + '\n' + ' '.join(map(str, R)) + '\n'


def answer(A):
    return ' '.join(map(str, A)) + '\n'


def solution(L, R):
    A = L + R
    A.sort()
    return A


def random_sorted_array(size):
    random_arr = [ randint(*RANDOM_ARRAY_ELEMENT_MINMAX) for _ in range(size)]
    random_arr.sort()
    return random_arr


tests = TestSet()

tests.add(
    question([2, 4, 8], [1, 2, 3, 10]),
    answer([1, 2, 2, 3, 4, 8, 10])
)
tests.add(
    question([4], [3, 10]),
    answer([3, 4, 10])
)
tests.add(
    question([2, 4, 8], []),
    answer([2, 4, 8])
)


for _ in range(NUMBER_OF_RANDOM_TESTS):
    random_L = random_sorted_array(RANDOM_ARRAY_SIZE)
    random_R = random_sorted_array(RANDOM_ARRAY_SIZE)
    solution_A = solution(random_L, random_R)

    tests.add(
        question(random_L, random_R),
        answer(solution_A)
    )
