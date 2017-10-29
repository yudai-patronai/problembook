#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

def bin_search(arr, x):
    l = 0
    r = len(arr)
    while r-l > 1:
        m = (r+l)//2
        if int(arr[m]) > x:
            r = m
        else:
            l = m
    return l

def generate_test(name, n, tr_list):
    #task
    with open(name, "w") as f:
        f.write(str(n) + '\n')
    #answer
    with open(name + ".a", "w") as f:
        i = bin_search(tr_list, n) + 1
        f.write(str(len(tr_list[:i])))

manual = [0, 1, 2, 10, 13, 66012]

if __name__ == "__main__":
    with open("tribonacci_list", "r") as f:
        tr_list = f.readline().split()
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, len(manual) + 1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, manual[test-1], tr_list)

    for test in range(len(manual) + 1, len(manual) + 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, random.randint(20, 400000), tr_list)
