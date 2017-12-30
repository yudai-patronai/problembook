from lib.testgen import TestSet
from lib import random

MAX_RAND_TESTS = 10

def case_to_str(arr_in, arr_res):
    return ' '.join(str(x) for x in arr_in) + '\n', ' '.join(str(x) for x in arr_res) + '\n'

def get_case(n):
    test_in = []
    test_out = []
    res = []
    src = random.sample(range(1, 100), n)
    for i, val in enumerate(src):
        neg = random.choice([0, 1])
        if neg == 0:
            test_in.append(val)
            res.append(val)
        else:
            test_in.append(-val)
            if (len(res) > 0):
                if (res[-1] <= val):
                    res.pop()
                else:
                    res[-1] -= val

    test_in.append(0)
    test_out.append(len(res))
    if (len(res) > 0):
        test_out.append(res[-1])
    else:
        test_out.append(-1)

    return case_to_str(test_in, test_out)

tests = TestSet()

tests.add(*case_to_str([1, 2, 5, 0], [3, 5]))
tests.add(*case_to_str([1, 5, -3, 1, -1, 0], [2, 2]))
tests.add(*case_to_str([1, 2, -2, -1, 0], [0, -1]))
tests.add(*case_to_str([-1, -2, -3, 0], [0, -1]))

for i in range(MAX_RAND_TESTS):
    tests.add(*get_case((i + 5)*2))
