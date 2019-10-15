from lib.testgen import TestSet
from lib.random import randint, seed

NUMBER_OF_TESTS = 15
RANDOM_FLOOR = 10000

seed(10)


def question(a, b):
    return '{} {}\n'.format(a, b)

def answer(a, b):
    summ = a + b
    diff = a - b

    return '{},{}\n'.format(summ, diff)

def random_test():
    a = randint(-RANDOM_FLOOR, RANDOM_FLOOR)
    b = randint(-RANDOM_FLOOR, RANDOM_FLOOR)

    return question(a, b), answer(a, b)


tests = TestSet()

for _ in range(NUMBER_OF_TESTS):
    tests.add( *random_test() )
