#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

ans = {
    "input": [
        [1,3],
        [4,1,2,6,8,7,5],
        [6,5,9,7],
        [7,6,5,3,2,1],
        [1002, 1000],
        [1000, 998, 1001],
        [54673,54672,54674,54676,54671],
    ],
    "output": [
        2,
        3,
        8,
        4,
        1001,
        999,
        54675
    ]
}

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
    
    
    rnd_min = random.randint(1, 100000000)
    rnd_out = random.randint(1,99999)
    test_name = os.path.join(test_folder, "%02d" % 8)
    seq = [rnd_min+i for i in range(100001) if i != rnd_out]
    random.shuffle(seq)
    generate_test(test_name, seq, rnd_min+rnd_out)
    
    
    rnd_min = random.randint(1, 100000000)
    rnd_out = random.randint(1,9999)
    test_name = os.path.join(test_folder, "%02d" % 9)
    seq = [rnd_min+i for i in range(10001) if i != rnd_out]
    random.shuffle(seq)
    generate_test(test_name, seq, rnd_min+rnd_out)