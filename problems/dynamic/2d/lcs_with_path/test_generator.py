#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def count(s1, s2, d=None):
    if d is None:
        d = [[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
    if d[len(s1)][len(s2)] != -1:
        return d[len(s1)][len(s2)]
    if not s1 or not s2:
        d[len(s1)][len(s2)] = 0
        return 0
    if s1[-1] == s2[-1]:
        d[len(s1)][len(s2)] = count(s1[:-1], s2[:-1], d) + 1
    else:
        d[len(s1)][len(s2)] = max(count(s1[:-1], s2, d), count(s1, s2[:-1], d))
    return d[len(s1)][len(s2)]


def generate_test(name, possible=True):
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    s1 = [random.randint(0, 1000) for _ in range(n)]
    s2 = [random.randint(0, 1000) for _ in range(m)]
    with open(name, "w") as f:
        f.write(' '.join(map(str, s1))+"\n")
        f.write(' '.join(map(str, s2))+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(s1, s2))+"\n")
            

def write_manual_test(name, s1, s2):
    with open(name, "w") as f:
        f.write(' '.join(map(str, s1))+"\n")
        f.write(' '.join(map(str, s2))+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(s1, s2))+"\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    """for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)"""        
    write_manual_test(os.path.join(test_folder, "01"), [12], [12])
    write_manual_test(os.path.join(test_folder, "02"), [14, 5, 8, 11, 0, 9, 3], [1, 35, 87, 13])
    write_manual_test(os.path.join(test_folder, "03"), [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
    write_manual_test(os.path.join(test_folder, "04"), [8, 0, 3, 1, 4, 5, 6], [6, 5, 4, 1, 3, 0, 8])
    write_manual_test(os.path.join(test_folder, "05"), [random.randint(0, 1000) for _ in range(100)],
                      [random.randint(0, 1000) for _ in range(100)])
    generate_test(os.path.join(test_folder, "06"))
    generate_test(os.path.join(test_folder, "07"))