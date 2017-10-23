#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)
            

def write_manual_test(name, a, b, c, t):
    with open(name, "w") as f:
        f.write(str(a)+"\n")
        f.write(str(b)+"\n")
        f.write(str(c)+"\n")
    with open(name+".a", "w") as f:
        f.write(t)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)    
    write_manual_test(os.path.join(test_folder, "01"), 8, 10, 6, "right")
    write_manual_test(os.path.join(test_folder, "02"), 5, 0, 5, "impossible")
    write_manual_test(os.path.join(test_folder, "03"), 0, 0, 0, "impossible")
    write_manual_test(os.path.join(test_folder, "04"), 40, 40, 40, "acute")
    write_manual_test(os.path.join(test_folder, "05"), 15, 4, 9, "impossible")
    write_manual_test(os.path.join(test_folder, "06"), 12, 6, 6, "impossible")
    write_manual_test(os.path.join(test_folder, "07"), 3, 4, 6, "obtuse")
    write_manual_test(os.path.join(test_folder, "08"), 8, 8, 3, "acute")
    write_manual_test(os.path.join(test_folder, "09"), 13, 2, 12, "obtuse")
