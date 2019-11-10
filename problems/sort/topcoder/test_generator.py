#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)

RANDOM_TEST_LEN = 100

def get_name():
    return ''.join(random.sample([chr(i) for i in range(ord('a'), ord('z')+1)]+['_'], random.randint(1, 25)))


def generate_test(test_file):
    n = random.randint(1, RANDOM_TEST_LEN)
    m = []
    a = []
    for _ in range(n):
        m.append(random.randint(1, 20))
        a.append([(random.randint(-500000, 1000000)/100, get_name()) for _ in range(m[-1])])
        a[-1].sort(key=lambda x: (-x[0], x[1]))
    with open(test_file, 'w') as fs:
        fs.write(str(n) + '\n')
        for i in range(n):
            fs.write(str(m[i]) + '\n')
            for j in a[i]:
                fs.write("{:.2f} {}\n".format(*j))
    b = []
    for i in a:
        b.extend(i)
    b.sort(key=lambda x: (-x[0], x[1]))
    with open(test_file + '.a', 'w') as fs:
        fs.write(str(len(b)) + '\n')
        for i in b:
            fs.write("{:.2f} {}\n".format(*i))


def write_test(test_file, a):
    n = len(a)
    m = []
    for i in range(n):
        m.append(len(a[i]))
        a[i].sort(key=lambda x: (-x[0], x[1]))
    with open(test_file, 'w') as fs:
        fs.write(str(n) + '\n')
        for i in range(n):
            fs.write(str(m[i]) + '\n')
            for j in a[i]:
                fs.write("{:.2f} {}\n".format(*j))
    b = []
    for i in a:
        b.extend(i)
    b.sort(key=lambda x: (-x[0], x[1]))
    with open(test_file + '.a', 'w') as fs:
        fs.write(str(len(b)) + '\n')
        for i in b:
            fs.write("{:.2f} {}\n".format(*i))


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test(os.path.join(test_folder, "01"), [[(125.00, "vasya")]])
    write_test(os.path.join(test_folder, "02"), [[(7.70, "abc")], [(-7.70, "abd")]])
    write_test(os.path.join(test_folder, "03"), [[(-335.08, "vasya"), (-754.45, "petya"), (-41.05, "borya")]])
    write_test(os.path.join(test_folder, "04"), [[(random.randint(-500000, 1000000)/100, get_name()) for _ in range(20)] for _ in range(RANDOM_TEST_LEN)])

    for test in range(5, 8):
        generate_test(os.path.join(test_folder, "0{}".format(test)))
