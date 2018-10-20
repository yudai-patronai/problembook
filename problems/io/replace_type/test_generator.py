#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

types = ["lint", "ulint", "sint", "usint", "schar", "dchar", "uchar", "float"] * 2

def generate_test(name, testn, dtype): 
    if testn % 2:
        num = random.randint(9223372036854775808, 9223372036854775807 + 9223372036854775807)
    else:
        num = random.randint(0, 9223372036854775807)
    with open(name, "w") as f:
        f.write(str(num) +"\n")
        f.write(dtype)
    out = name + ".a"
    os.system("./a.out <%s >%s" % (name, out))

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    if "a.out" not in os.listdir("."): os.system("gcc -o a.out solution.c")
    for i, dtype in enumerate(types):
        test = i+1
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test, dtype)
