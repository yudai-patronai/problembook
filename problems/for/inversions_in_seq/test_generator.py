#!/usr/bin/env python3

import os
import shutil
import random

random.seed(100)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')


class Test:
    def __init__(self, fname):
        self.fname = fname
        self.f = open(fname, 'w')
        self.last = 0
        self.inv = 0


    def __enter__(self):
        return self


    def __exit__(self, type, value, traceback):
        self.f.write('0\n')
        self.f.close()
        with open(self.fname + '.a', 'w') as f:
            f.write(str(self.inv) + '\n')


    def add_num(self, num):
        assert num > 0

        if self.last != 0 and self.last < num:
            self.inv += 1

        self.last = num
        self.f.write(str(num) + '\n')


def gen_rand_test(fname, size):
    with Test(fname) as t:
        for i in range(size):
            t.add_num(random.randrange(1, 100))


def write_seq_test(fname, seq):
    with Test(fname) as t:
        for x in seq:
            t.add_num(x)


def test_fname(tests_dir, ind):
    return os.path.join(tests_dir, '%.2d' % ind)


def gen_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    write_seq_test(test_fname(tests_dir, 1), [3, 2, 1])
    write_seq_test(test_fname(tests_dir, 2), [1, 2, 3])
    write_seq_test(test_fname(tests_dir, 3), [1, 1, 1])
    write_seq_test(test_fname(tests_dir, 4), [1, 2, 1])
    write_seq_test(test_fname(tests_dir, 5), [2, 2, 1])
    write_seq_test(test_fname(tests_dir, 6), [1, 2, 1, 2, 1])
    write_seq_test(test_fname(tests_dir, 7), [10])
    write_seq_test(test_fname(tests_dir, 8), [])

    gen_rand_test(test_fname(tests_dir, 9), 100)
    gen_rand_test(test_fname(tests_dir, 10), 10000)
    gen_rand_test(test_fname(tests_dir, 11), 2000000)


gen_tests(tests_dir)
