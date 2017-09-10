#!/usr/bin/python3

import os
import shutil
from lib import random

def solution(dots):
    data = []
    for i in range(4):
        data.append([])
        for j in range(4):
            data[i].append(0)

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

        data[quarterNum][0] += 1

        if data[quarterNum][0] == 1 or abs(x) < data[quarterNum][1] or abs(y) < data[quarterNum][1]:
            new_min = 0
            if abs(x) < abs(y):
                new_min = abs(x)
            else:
                new_min = abs(y)
            data[quarterNum][1] = new_min
            data[quarterNum][2] = x
            data[quarterNum][3] = y

    quarterNum = 0

    max = data[0][0]
    for i in range(1, 4):
        if data[i][0] > max or (data[i][0] == max and data[i][1] < data[quarterNum][1]):
            max = data[i][0]
            quarterNum = i

    return "{} {} {} {} {}".format(quarterNum + 1, data[quarterNum][0], data[quarterNum][2], data[quarterNum][3],
                                   data[quarterNum][1])


N = 50
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
        for dot in test_input:
            f.write(str(dot[0]) + ' ' + str(dot[1]) + '\n')

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(str(solution(test_input)))
