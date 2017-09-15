#!/usr/bin/python3

import os
import shutil
import random
#from lib import random
#random.seed(10000)

def write_cases(case_list):
    for test_num, case in enumerate(case_list):
        with open(os.path.join(tests_dir, '{0:0>2}'.format(test_num)), 'w') as f:
            f.write(case['question'])

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(test_num)), 'w') as f:
            f.write(case['answer'])

def get_question_str(num):
    return '{0:0>4}'.format(str(num))

def get_answer_str(num):
    digits = sorted(str(num))
    target_pos = next(i for i, d in enumerate(digits) if d != '0')
    digits[0], digits[target_pos] = digits[target_pos], digits[0]
    return '{0:0>4}\n'.format(''.join(digits))

def get_test_dict(num):
    return {'question': get_question_str(num), 'answer': get_answer_str(num)}


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

test_cases = []
N = 50

# Random tests
for _ in range(N):
    test_num = random.randint(1000, 9999)
    test_cases.append(get_test_dict(test_num))

# Custom tests
test_cases.append(get_test_dict(1024))
test_cases.append(get_test_dict(1000))
test_cases.append(get_test_dict(1010))
test_cases.append(get_test_dict(1001))
test_cases.append(get_test_dict(1101))
test_cases.append(get_test_dict(4201))
test_cases.append(get_test_dict(1111))

write_cases(test_cases)
