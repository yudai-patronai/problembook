#!/usr/bin/python3

import os
import shutil
import math

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


tests = [
    ["-x*x", -10, 13],
    ["-2*x", 0, 2],
    ["math.log2(x)", 2, 8],
    ["math.sin(x*x)", 0, 2],
    ["x**3-6*x**2+4*x+12", -10, 1],
    ["x**4+5", 3, 8]
]

def ternary_search(f, left, right):
    while abs(right - left) > 1e-5:
        m1 = (2*left + right) / 3
        m2 = (left + 2*right) / 3
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    return (left+right)/2, f((left+right)/2)

for j, (a, b, c) in enumerate(tests):
    func = eval("lambda x: {}".format(a))
    left = float(b)
    right = float(c)

    with open(os.path.join(tests_dir, "{:02}".format(j+1)), "w") as f:
        f.write("\n".join(map(str, (a, b, c))))
    with open(os.path.join(tests_dir, "{:02}.a".format(j+1)), "w") as f:
        x, fx = ternary_search(func, left, right)
        f.write("{:.5} {:.5}".format(x, fx))

