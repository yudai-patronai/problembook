#!/usr/bin/env python3
import os
import shutil
from lib import random

random.seed(42)


def write_test(fname):
    n = random.randint(1, 1000)
    write_test_with_n(fname, n)


def write_test_with_n(fname, n):
    goblins = set([i for i in range(1, n+1)])
    q = []
    with open(fname, "w") as fin, open(fname+".a", "w") as fout:
        fin.write("{}\n".format(n))
        for _ in range(n):
            act = random.randint(1, 3) if len(q) else random.randint(1, 2)
            if (act == 1):
                x = random.choice(list(goblins))
                goblins.remove(x)
                fin.write("+ {}\n".format(x))
                q.append(x)
            elif (act == 2):
                x = random.choice(list(goblins))
                goblins.remove(x)
                fin.write("* {}\n".format(x))
                q.insert(len(q) // 2 + len(q) % 2, x)
            else:
                fin.write("-\n")
                fout.write("{}\n".format(q.pop(0)))


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i in range(10):
        write_test(os.path.join(tests_dir, '%.2d' % (i + 1)))
    write_test_with_n(os.path.join(tests_dir, '%.2d' % (11)), 1000)


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
write_tests(tests_dir)
