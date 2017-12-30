#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

max_int = 1000000

def generate_test(name, testn):
    n = random.randint(1, 1000)
    a = [random.randint(-max_int, max_int) for _ in range(n)]
    b = [i for i in a if i % 2 == 0]
    b.sort()
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for i in a:
            f.write(str(i)+"\n")
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = b.pop(0)
    with open(name+".a", "w") as f:   
        for i in a:
            f.write(str(i)+" ")          


def write_manual_test(name, a):
    n = len(a)
    b = [i for i in a if i % 2 == 0]
    b.sort()
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for i in a:
            f.write(str(i)+"\n")
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = b.pop(0)
    with open(name+".a", "w") as f:   
        for i in a:
            f.write(str(i)+" ")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), [random.randint(-max_int, max_int) for _ in range(1000)])
    write_manual_test(os.path.join(test_folder, "07"), [random.randint(-10000, 10000)*2+1 for _ in range(random.randint(1, 1000))])
