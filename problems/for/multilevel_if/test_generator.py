from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 20
MAX_RAND_LEN = 100

def get_case(seq):
    question = '{}\n'.format(len(seq))
    question += ' '.join(str(a) for a in seq)
    temp = []
    for i in range(len(seq)):
        digit = int(str(seq[i])[:1])
        if ((seq[i] % 4 == 0) and (digit != 4 and digit != 5)):
            temp.append(seq[i])
            continue
        if ((seq[i] % 7 == 0) and (digit != 7 and digit != 1)):
            temp.append(seq[i])
            continue
        if ((seq[i] % 9 == 0) and (digit != 8 and digit != 9)):
            temp.append(seq[i])
            continue

    if len(temp) == 0:
        temp.append(0)
    
    answer = '\n'.join([str(x) for x in temp])

    return question, answer

tests = TestSet()

for _ in range(MAX_RAND_TESTS):
    tests.add(*get_case([randint(1000,9999) for _ in range(10, MAX_RAND_LEN)]))
