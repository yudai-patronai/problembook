#!/usr/bin/env python3
import os
import shutil
from lib import random

random.seed(42)


def write_test(fname):
    n = random.randint(1, 20)
    m = n - 1
    s = []
    with open(fname, "w") as fin, open(fname+".a", "w") as fout: 
        while n and m:
            act = random.randint(0, 1)
            if len(s) < 2 or act:
                n -= 1
                x = random.randint(-20, 20)
                fin.write("{}\n".format(x))
                s.append(x)
            else:
                m -= 1
                act = random.choice(['+', '+', '-', '-', '*'])
                fin.write("{}\n".format(act))
                if act == "+":
                    s.append(s.pop() + s.pop())
                elif act == "-":
                    s.append(-s.pop() + s.pop())
                else:
                    s.append(s.pop() * s.pop())
        while m:
            m -= 1
            act = random.choice(['+', '+', '-', '-', '*'])
            fin.write("{}\n".format(act))
            if act == "+":
                s.append(s.pop() + s.pop())
            elif act == "-":
                s.append(-s.pop() + s.pop())
            else:
                s.append(s.pop() * s.pop())
        fin.write("=\n")
        fout.write("{}\n".format(s.pop()))


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i in range(10):
        write_test(os.path.join(tests_dir, '%.2d' % (i + 1)))

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
write_tests(tests_dir)
