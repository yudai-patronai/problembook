from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 20
MAX_RAND_LEN = 100

def get_case(seq):
    question = '{}\n'.format(len(seq))
    question += ' '.join(str(a) for a in seq)
    temp = []
    for i in range(len(seq)):
        if ((seq[i] % 4 == 0) or (seq[i] % 7 == 0) or (seq[i] % 9 == 0)):
            temp.append(seq[i])
            continue
        digit = int(str(seq[i])[:1])
        if (digit == 7 or digit == 1 or digit == 4 or digit == 5 or digit == 9):
            temp.append(seq[i])

    if len(temp) == 0:
        temp.append(0)
    
    answer = ' '.join([str(x) for x in temp])

    return question, answer

tests = TestSet()

for _ in range(MAX_RAND_TESTS):
    tests.add(*get_case([randint(1000,9999) for _ in range(10, MAX_RAND_LEN)]))
