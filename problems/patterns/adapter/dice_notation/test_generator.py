#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)

tests = [ "3 d8", "5d6 + 3d4 +4", "2 d 20 + 17", "7d2+5d12+7d20+3d4"
]

def dice_res(dice):
    _lst = [int(x) for x in dice.split("d")].append(1)
    return _lst[:2]

def gen_res(dst):
    dice_lst = (self.dice_res(i) for i in dst.replace(" ", "").split("+"))
    sm = sum((x[0]*x[1] for x in dice_lst))
    return str(sm ** 257 % 337)

if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    for i in range(1,16):
        if i<len(tests):
            tst = tests[i]
        else:
            tst = "+".join(["{}d{}".format(random.randint(1,50), random.randint(1, 100)) for _ in range(2**i)])
            if i%2:
                tst += "+{}".format(random.randint(1, 10000))
        with open(os.path.join(os.path.join(test_folder, "{:02}".format(i)), "w") as f:
            f.write(tst)
        with open(os.path.join(os.path.join(test_folder, "{:02}.a".format(i)), "w") as f:
            f.write(gen_res(tst))
        