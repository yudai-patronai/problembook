from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 20
MAX_RAND_LEN = 100

def get_case(seq):
    q_str = '{}\n'.format(len(seq))
    q_str += ' '.join(str(e) for e in seq)

    d = [0] * len(seq)
    for i in range(len(seq)):
        d[i] = 1
        for j in range(i):
            if seq[j] < seq[i]:
                d[i] = max(d[i], 1 + d[j])

    ans = d[0]
    for i in range(len(seq)):
        ans = max(ans, d[i])

    return q_str, str(ans)


tests = TestSet()

tests.add(*get_case([1]))
tests.add(*get_case([-1, 0, 1]))
tests.add(*get_case([1, -2, 2, -1, 3]))
tests.add(*get_case([3, 2, 1]))
tests.add(*get_case([-1, 0, -1]))

for _ in range(MAX_RAND_TESTS):
    tests.add(*get_case([randint(-20, 20) for _ in range(10, MAX_RAND_LEN)]))
