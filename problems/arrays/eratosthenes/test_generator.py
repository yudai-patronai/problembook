#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def bin_search(a, x):
    l = 0
    r = len(a)
    while r-l > 1:
        m = (r+l)//2
        if int(a[m]) > x:
            r = m
        else:
            l = m
    return l


def generate_test(name, n, primes):
    with open(name, "w") as f:
        f.write(str(n))
    with open(name+".a", "w") as f:
        i = bin_search(primes, n) + 1
        f.write(' '.join(primes[:i]))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    with open("prime_list", "r") as f:
        primes = f.readline().split(' ')
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, random.randint(3, 10000), primes)
        
    generate_test(os.path.join(test_folder, "06"), 2, primes)
    generate_test(os.path.join(test_folder, "07"), 10000, primes)
    generate_test(os.path.join(test_folder, "08"), 8689, primes)
