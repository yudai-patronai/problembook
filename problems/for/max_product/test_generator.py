#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_test(name, testn):
    n = random.randint(2, 10000)
    nums = [random.randint(-10000, 10000) for _ in range(n)]
    nums.sort() 
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for i in nums:
            f.write(str(i)+"\n")
    if nums[0]*nums[1] >= nums[-1]*nums[-2]:
        ans = str(nums[0]*nums[1])
    else:
        ans = str(nums[-1]*nums[-2])
    with open(name+".a", "w") as f:
        f.write(ans)
            

def write_manual_test(name, n, nums):
    nums.sort() 
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for i in nums:
            f.write(str(i)+"\n")
    if nums[0]*nums[1] >= nums[-1]*nums[-2]:
        ans = str(nums[0]*nums[1])
    else:
        ans = str(nums[-1]*nums[-2])
    with open(name+".a", "w") as f:
        f.write(ans)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), 2, [0, 0])
    write_manual_test(os.path.join(test_folder, "07"), 10000, [random.randint(-10000, 10000) for _ in range(10000)])
    write_manual_test(os.path.join(test_folder, "08"), 7, [-9, -7, 2, 5, 1, 0, 6])
