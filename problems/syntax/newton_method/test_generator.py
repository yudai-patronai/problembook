#!/usr/bin/python3

import os
import shutil
import math

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


tests = [
    ["x*x", "2*x", "0", "0"],
    ["x*x", "2*x", 5, 0],
    ["math.sin(x*x)", "2*x*math.cos(x*x)", 5, 0.001],
    ["math.exp(x) - 1", "math.exp(x)", 10, 0],
    ["math.exp(x+4) - math.exp(-x-20)", "math.exp(x+4) + math.exp(-x-20)", 0, 1e-7]
]

def gradient_descent(f, d, x, lr=0.1, eps=1e-4):
    yield (x, f(x))
    while True:
        xn = x - f(x)*d(x)
        yield (xn, f(xn))
        if abs(f(xn)) <= eps:
            return
        x = xn

for j, (a, b, c, d, e) in enumerate(tests):
    fx = eval("lambda x: {}".format(a))
    dx = eval("lambda x: {}".format(b))
    x = float(c)
    eps = float(e)

    with open(os.path.join(tests_dir, "{:02}".format(j+1)), "w") as f:
        f.write("\n".join(map(str, (a,b,c,d,e))))
    with open(os.path.join(tests_dir, "{:02}.a".format(j+1)), "w") as f:    
        if eps != 0.:
            for i, (xi, fxi) in enumerate(gradient_descent(fx, dx, x, eps)):
                f.write("{}{:10.5}{:10.5}".format(i, xi, fxi))
                f.write("\n")
        else:
            for i, (xi, fxi) in enumerate(gradient_descent(fx, dx, x)):
                f.write("{}{:10.5}{:10.5}".format(i, xi, fxi))
                f.write("\n")