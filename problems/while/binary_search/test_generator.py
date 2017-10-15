from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TEST = 20
MAX_RAND_LEN = 100

def get_case(seq, number):
    sorted(seq)
    question = '{}\n'.format(len(seq))
    question += ' '.join(str(a) for a in seq)
    question += '\n' + str(number)
    answer = -1
    left = 0
    right = len(seq) - 1
    while (left <= right):
        middle = (left + right) // 2
        if (seq[middle] == number):
            answer = middle + 1
        elif (seq[middle] > number):
            right = middle - 1
        else:
            left = middle + 1
    
    return question, str(answer)

tests = TestSet()

for _ in range(MAX_RAND_TEST):
    tests.add(*get_case([randint(1, 200) for _ in range(10, MAX_RAND_LEN)], randint(1, 200)))