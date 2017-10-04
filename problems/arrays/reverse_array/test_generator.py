#!/usr/bin/env python3

import os
import shutil
from lib import random

manual = {
    "test" : [
        [[1,2,3,4,5], 5],
        [[1,2,3,4,5], 4],
        [[1,2,3,4,5], 3],
        [[1,2,3,4,5], 0],
        [[0], 0],
        [[0], 1]
    ],
    "answer" : [
        [5,4,3,2,1],
        [4,3,2,1,5],
        [3,2,1,4,5],
        [1,2,3,4,5],
        [0],
        [0]
    ]
}

NUM_RANDOM_TESTS = 5
random.seed(42)

def gen_answer(arr, N):
    arr = arr[:]
    for i in range(N//2):
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
    return arr

if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    # manual tests
    for idx, (test, answer) in enumerate(zip(manual["test"], manual["answer"])):
        test_name = os.path.join(test_folder, "%02d" % (idx+1,))
        with open(test_name, "w") as f:
            f.write('{}\n{}'.format(" ".join(map(str, test[0])), test[1]))
        with open(test_name+'.a', "w") as f:
            f.write(' '.join(map(str, answer)))
    # random tests
    shift = len(manual["answer"])
    for test in range(NUM_RANDOM_TESTS):
        test_name = os.path.join(test_folder, "%02d" % (test+shift,))
        seq_len = random.randint(30,100)
        N = random.randint(0,seq_len)
        seq = [random.randint(-100,100) for _ in range(seq_len)]
        
        with open(test_name, "w") as f:
            f.write('{}\n{}'.format(" ".join(map(str, seq)), N))
        
        with open(test_name+'.a', "w") as f:
            f.write(' '.join(map(str, gen_answer(seq, N))))