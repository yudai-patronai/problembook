#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_string(l=random.randint(1, 100)):
    s = ""
    for _ in range(l):
        if random.randint(0, 1) == 0:
            c = chr(random.randint(ord("A"), ord("Z")))
        else:
            c = chr(random.randint(ord("a"), ord("z")))
        s += c
    return s


def generate_test(name, testn):
    n = random.randint(1, 100)
    code = [generate_string() for _ in range(n)]
    cipher = [random.randint(0, n-1) for _ in range(n)]
    ans = [code[i] for i in cipher]      
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for s in code:
            f.write(s+"\n")
        for i in cipher:
            f.write(str(i)+"\n")
    with open(name+".a", "w") as f:
        f.write(" ".join(ans))
            

def write_manual_test(name, n, code, cipher):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for s in code:
            f.write(s+"\n")
        for i in cipher:
            f.write(str(i)+"\n")
    ans = [code[i] for i in cipher]
    with open(name+".a", "w") as f:
         f.write(" ".join(ans))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), 1, ["Hello"], [0])
    write_manual_test(os.path.join(test_folder, "07"), 100, [generate_string(100) for _ in range(100)], [random.randint(0, 99) for _ in range(100)])
