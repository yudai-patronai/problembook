from lib.testgen import TestSet
from lib.random import randint
from lib.random import choice
from lib.random import sample

MAX_RAND_TEST = 20
MAX_RAND_LEN = 1000000

def get_case(seq, flag):
    seq.sort()
    if flag == 1:
        number = choice(seq)
    else:
        number = randint(1, 1500000)
    question = '{}\n'.format(len(seq))
    question += str(number)
    question += '\n'
    question += ' '.join(str(a) for a in seq)
    answer = -1
    left = 0
    right = len(seq) - 1
    while (left <= right):
        middle = (left + right) // 2
        if (seq[middle] == number):
            answer = middle + 1
            break
        elif (seq[middle] > number):
            right = middle - 1
        else:
            left = middle + 1
    
    return question, str(answer)

tests = TestSet()

for i in range(MAX_RAND_TEST // 2):
    tests.add(*get_case(sample(range(1, 1500000), randint(10, MAX_RAND_LEN)), 1))

for i in range(MAX_RAND_TEST // 2):
    tests.add(*get_case(sample(range(1, 1500000), randint(10, MAX_RAND_LEN)), 0))
