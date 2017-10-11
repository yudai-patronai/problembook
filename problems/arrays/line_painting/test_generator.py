#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_test(name, testn):
    n = random.randint(0, 100)
    m = random.randint(1, 100)
    events = []
    panels = []
    for i in range(n):
        l = random.randint(1, 1000000000)
        r = random.randint(1, 1000000000)
        c = random.randint(0, 1000000)
        if l > r:
         l, r = r, l
        events.append((l, r, c))
    for i in range(m):
        panels.append(random.randint(1, 1000000000))
    ans = ['0']*m
    for i in range(m):
        for j in reversed(range(n)):    
            if events[j][0] <= panels[i] <= events[j][1]:
                ans[i] = str(events[j][2])
                break 
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for l, r, c in events:
            f.write(str(l)+"\n")
            f.write(str(r)+"\n")
            f.write(str(c)+"\n")
        f.write(str(m)+"\n")
        for i in panels:
            f.write(str(i)+"\n")
    with open(name+".a", "w") as f:
        f.write(' '.join(ans))
            

def write_manual_test(name, n, m, events):
    panels = []
    for i in range(m):
        panels.append(random.randint(1, 1000000000))    
    ans = ['0']*m
    for i in range(m):
        for j in reversed(range(n)):    
            if events[j][0] <= panels[i] <= events[j][1]:
                ans[i] = str(events[j][2])
                break 
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for l, r, c in events:
            f.write(str(l)+"\n")
            f.write(str(r)+"\n")
            f.write(str(c)+"\n")
        f.write(str(m)+"\n")
        for i in panels:
            f.write(str(i)+"\n")
    with open(name+".a", "w") as f:
        f.write(' '.join(ans))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), 0, random.randint(1, 100), [])
    write_manual_test(os.path.join(test_folder, "07"), 2, random.randint(1, 100), [(1, 1000000000, 5), (1, 1000000000, 1000000)])
    write_manual_test(os.path.join(test_folder, "07"), 100, 100, [tuple([random.randint(1, 1000000000), random.randint(1, 1000000000), random.randint(1, 1000000)]) for _ in range(100)])
