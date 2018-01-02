#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

max_int = 1000000

def generate_test(name, testn):
    n = random.randint(1, 1000)
    a = [(random.randint(-max_int, max_int), random.randint(-max_int, max_int)) for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for e in a:
            f.write(str(e[0])+"\n")
        for e in a:
            f.write(str(e[1])+"\n")
    a.sort()
    with open(name+".a", "w") as f:   
        for e in a:
            f.write(str(e[0])+" ")
        f.write("\n")
        for e in a:
            f.write(str(e[1])+" ")             


def write_manual_test(name, a):
    with open(name, "w") as f:
        f.write(str(len(a))+"\n")
        for e in a:
            f.write(str(e[0])+"\n")
        for e in a:
            f.write(str(e[1])+"\n")
    a.sort()
    with open(name+".a", "w") as f:   
        for e in a:
            f.write(str(e[0])+" ")
        f.write("\n")
        for e in a:
            f.write(str(e[1])+" ")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 4):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "04"), [(random.randint(-max_int, max_int), random.randint(-max_int, max_int)) for _ in range(1000)])
    write_manual_test(os.path.join(test_folder, "05"), [(5, 1), (4, 2), (3, 3), (2, 4), (1, 3)])
