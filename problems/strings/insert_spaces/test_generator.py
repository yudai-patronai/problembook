#!/usr/bin/python3

import os
import shutil
from lib import random
from string import ascii_letters

NUM_TEST = 50
MAX_STR_LEN = 256

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

def write_cases(case_list):
    for test_num, case in enumerate(case_list):
        with open(os.path.join(tests_dir, '{0:0>2}'.format(test_num)), 'w') as f:
            f.write(case['question'])
        
        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(test_num)), 'w') as f:
            f.write(case['answer'])

def get_question(data):
    return data

def get_answer(data):
    data = " ".join(data[i:i+5] for i in range(0, len(data), 5))
    return data

def get_case(data):
    return {'question': get_question(data), 'answer': get_answer(data)}

case_list = []

def get_rand_char():
    return chr(random.randint(ord('A'), ord('z')))

for _ in range(NUM_TEST):
    in_str = ''.join(get_rand_char() for  _ in range(random.randint(42, MAX_STR_LEN)))
    case_list.append(get_case(in_str))

write_cases(case_list)