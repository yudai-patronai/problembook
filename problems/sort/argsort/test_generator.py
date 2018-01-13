#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

max_int = 1000000

def generate_test(name, testn):
    n = random.randint(1, 1000)
    a = [random.randint(-max_int, max_int) for _ in range(n)]
    b = [i for i, _ in sorted(enumerate(a), key = lambda x: x[1])]
    with open(name, "w") as f:
        f.write(" ".join(map(str, a)))
    with open(name+".a", "w") as f:   
        f.write(" ".join(map(str, b))) 


def write_manual_test(name, a):
    b = [i for i, _ in sorted(enumerate(a), key = lambda x: x[1])]
    with open(name, "w") as f:
        f.write(" ".join(map(str, a)))
    with open(name+".a", "w") as f:   
        f.write(" ".join(map(str, b))) 


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), [random.randint(-max_int, max_int) for _ in range(1000)])
    write_manual_test(os.path.join(test_folder, "07"), [5])
