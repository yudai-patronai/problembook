#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def get_name():
    return ''.join(random.sample([chr(i) for i in range(ord('a'), ord('z')+1)]+['-'], random.randint(1, 20)))


def generate_test(test_file):
    n = random.randint(1, 10000)
    f = [get_name() for _ in range(n)]
    m = random.randint(1, 10000)
    af = [get_name() for _ in range(m)]
    mf = []
    with open(test_file, 'w') as fs:
        fs.write(str(n) + '\n')
        for i in f:
            fs.write(i + '\n')
        fs.write(str(m) + '\n')
        for i in af:
            fs.write(i + '\n')
    for i in list(f):
        if i in af:
            mf.append(i)
            af.remove(i)
    with open(test_file + '.a', 'w') as fs:
        fs.write("Friends: " + ', '.join(sorted(f)) + '\n')
        fs.write("Mutual Friends: " + ', '.join(sorted(mf)) + '\n')
        fs.write("Also Friend of: " + ', '.join(sorted(af)) + '\n')


def write_test(test_file, f, af):
    n = len(f)
    m = len(af)
    mf = []
    with open(test_file, 'w') as fs:
        fs.write(str(n) + '\n')
        for i in f:
            fs.write(i + '\n')
        fs.write(str(m) + '\n')
        for i in af:
            fs.write(i + '\n')
    for i in list(f):
        if i in af:
            mf.append(i)
            af.remove(i)
    with open(test_file + '.a', 'w') as fs:
        fs.write("Friends: " + ', '.join(sorted(f)) + '\n')
        fs.write("Mutual Friends: " + ', '.join(sorted(mf)) + '\n')
        fs.write("Also Friend of: " + ', '.join(sorted(af)) + '\n')


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test(os.path.join(test_folder, "01"), ["vasya"], ["petya"])
    write_test(os.path.join(test_folder, "02"), [], [])
    write_test(os.path.join(test_folder, "03"), ["name1", "name2", "name3"], [])
    write_test(os.path.join(test_folder, "04"), [], ["name4", "name5"])
    write_test(os.path.join(test_folder, "05"), ["a", "b", "c", "d"], ["d", "c", "b", "a"])
    write_test(os.path.join(test_folder, "06"), [get_name() for _ in range(10000)], [get_name() for _ in range(10000)])

    for test in range(7, 8):
        generate_test(os.path.join(test_folder, "0{}".format(test)))
