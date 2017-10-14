#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_test(name, testn):      
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for s in code:
            f.write(s+"\n")
        for i in cipher:
            f.write(str(i)+"\n")
    with open(name+".a", "w") as f:
        f.write(" ".join(ans))
            

def write_manual_test(name, n, code, cipher):



if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    