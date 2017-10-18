#!/usr/bin/python3

import os
import shutil

from lib import random
random.seed(10000)

def write_cases(case_list):
    for test_num, case in enumerate(case_list):
        with open(os.path.join(tests_dir, '{0:0>2}'.format(test_num)), 'w') as f:
            f.write(case['question'])

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(test_num)), 'w') as f:
            f.write(case['answer'])

def get_question_str(in_array):
    return '{0}\n{1}\n'.format(len(in_array), ' '.join(str(n) for n in in_array))

def get_answer_str(in_array):
    in_array.sort()
    sum_min = sum(in_array[:2])
    sum_max = sum(in_array[-2:])
    return '{} {}'.format(sum_min, sum_max)

def get_test_dict(in_array):
    return {'question': get_question_str(in_array), 'answer': get_answer_str(in_array)}


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

test_cases = []
N = 20

# Random tests
for test_num in range(N):
    test_len = random.randint(4, 100) + test_num * 10
    in_array = [random.randint(1, 100000) for _ in range(test_len)]
    test_cases.append(get_test_dict(in_array))

# Constant test
const_array = [42] * 1000
test_cases.append(get_test_dict(const_array))

# Blink tests
blink_array = [1, 2] * 1000
test_cases.append(get_test_dict(blink_array))

blink_array = [2, 1] * 1000
test_cases.append(get_test_dict(blink_array))

# Sorted tests
for test_num in range(N):
    test_len = random.randint(4, 100) + test_num * 10
    in_array = [random.randint(1, 1000000) for _ in range(test_len)]

    sort_array = sorted(in_array)
    test_cases.append(get_test_dict(sort_array))

    sort_array = sorted(in_array, reverse=True)
    test_cases.append(get_test_dict(sort_array))

write_cases(test_cases)
