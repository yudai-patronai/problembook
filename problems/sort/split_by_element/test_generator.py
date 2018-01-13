#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_test(name, testn):
    n = random.randint(1, 100000)
    a = [random.randint(-1000000, 1000000) for _ in range(n)]  
    x = a[random.randint(0, n-1)] 
    with open(name, "w") as f:
        f.write(" ".join(map(str, a)) + "\n")
        f.write(str(x)+"\n")
    i = 0
    for e in a:
        if e < x:
            i += 1
    with open(name+".a", "w") as f:
        f.write(str(i)+"\n")
            

def write_manual_test(name, a): 
    x = a[random.randint(0, len(a)-1)] 
    with open(name, "w") as f:
        f.write(" ".join(map(str, a)) + "\n")
        f.write(str(x)+"\n")
    i = 0
    for e in a:
        if e < x:
            i += 1
    with open(name+".a", "w") as f:
        f.write(str(i)+"\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), [5])
    write_manual_test(os.path.join(test_folder, "07"), [random.randint(-1000000, 1000000) for _ in range(100000)])
    write_manual_test(os.path.join(test_folder, "08"), [random.randint(-1000000, 1000000)] * random.randint(1, 1000000))

