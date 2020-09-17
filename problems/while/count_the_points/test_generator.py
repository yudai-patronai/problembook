#!/usr/bin/python3

import os
import shutil
from lib import random

def solution(dots):
    counters = [0]*4

    for dot in dots:
        x, y = dot
        quarterNum = -1
        if x * y != 0:
            if x > 0 and y > 0:
                quarterNum = 0
            elif x < 0 and y > 0:
                quarterNum = 1
            elif x < 0 and y < 0:
                quarterNum = 2
            else:
                quarterNum = 3
        else:
            continue

        counters[quarterNum] += 1

    max_count = counters[0]
    max_count_quarter = 1
    for i in range(1, 4):
        if counters[i] > max_count:
            max_count = counters[i]
            max_count_quarter = i + 1  # сдвиг, т.к. "нулевая" четверть называется первой
    return "{} {}".format(max_count_quarter, max_count)


N = 10
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


def gen_dots(n=None):
    if n == None:
        num = random.randint(10, 100)
    else:
        num = n
    test_dots = []
    for i in range(num):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        dot = (x, y)
        test_dots.append(dot)
    return test_dots


for i in range(1, N + 1):
    test_input = gen_dots()

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write(str(len(test_input)) + '\n')
        for dot in test_input:
            f.write(str(dot[0]) + ' ' + str(dot[1]) + '\n')

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(str(solution(test_input)))
