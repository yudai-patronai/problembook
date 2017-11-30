#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

ans = {
    "input": [
        [1],
        [1,2,3,4,5],
        [1,2,3,4,4],
        [1,3,5,5,4,2,3,2,1],
        [13,1,13,2,13,3,13,4,2,13],
        [7,7,7,7,7,7],
        [5,4,3,2,1],
        [-1,-3,-5,-6,-2,-6,-5,-1,-3,-3,-3]
    ],
    "output": [
        0,
        4,
        3,
        7,
        5,
        0,
        4,
        9,
    ]
}


def generate_answer(seq):
    mx = max(seq)
    return len([True for i in seq if i!=mx])


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
    
    for test in range(1,9):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, ans["input"][test-1], ans["output"][test-1])
    
    test_name = os.path.join(test_folder, "%02d" % 9)
    seq = [random.randint(1,1000) for _ in range(100000)]
    generate_test(test_name, seq)
