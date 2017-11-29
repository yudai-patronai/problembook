#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

ans = {
    "input": [
        [1],
        [1,2,3,4,5],
        [6,6,6,6,6,6,6],
        [5,-4,3,-2,-1],
        [1000,1],
        [-999,111,-888,222,-777,333,666,444,555],
        [-572],
    ],
}


def generate_answer(seq):
    n = len(seq)
    m = sum(seq)/n
    sq = sum(x*x for x in seq)/n
    return "{} {}".format(round(m,3), round(sq-m*m, 3))


def generate_test(name, data, answer = None):
    with open(name, "w") as f:
        f.write("\n".join(map(str, data + [0])))
    
    with open("%s.a" % name, 'w') as f:
        if answer is None:
            answer = generate_answer(data)
        f.write(str(answer))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    for test in range(1,8):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, ans["input"][test-1])
    
    test_name = os.path.join(test_folder, "%02d" % 8)
    seq = [random.randint(1, 1000) for _ in range(100000)]
    generate_test(test_name, seq)
    
    test_name = os.path.join(test_folder, "%02d" % 9)
    seq = [random.randint(1, 500) for _ in range(1000)]
    generate_test(test_name, seq)
