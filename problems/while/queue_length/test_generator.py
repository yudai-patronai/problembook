#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

ans = {
    "input": [
        [1565],
        [1492,1536,1620,1743,1852],
        [1521,1632,1703,1703,1703,1703,1703,1703],
        [1564,1642,1758,1758,1695,1642,1713,1642,1564],
        [1532,1521,1784,1524,1632,1872,1932,1721,1643,2041],
        [7,7,7,7,7,7],
        [5,4,3,2,1],
    ],
    "output": [
        1,
        5,
        3,
        3,
        5,
        1,
        1,
    ]
}


def generate_answer(seq):
    s, m = 0, 0
    for i in seq:
        if i > m:
            s += 1
            m = i
    return s


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
        generate_test(test_name, ans["input"][test-1], ans["output"][test-1])
    
    test_name = os.path.join(test_folder, "%02d" % 8)
    seq = [random.randint(1000, 2500) for _ in range(100000)]
    generate_test(test_name, seq)
