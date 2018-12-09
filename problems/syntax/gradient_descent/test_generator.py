#!/usr/bin/python3

import os
import shutil
import math

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


tests = [
    ["x*x", "2*x", "0", "0", "0"],
    ["x*x", "2*x", 1, 0, 0],
    ["math.sin(x*x)", "2*x*math.cos(x*x)", 5, 0.01, 0.001],
    ["1 - (1/math.sqrt(2*math.pi*2*2)*math.exp(-(x-5)*(x-5)/2/2/2)", "(math.exp(-1/8*(-5 + x)*(x-5))*(-5 + x))/(8*math.sqrt(2*math.pi))", 0, 0, 0],
    ["math.exp(x+4)+math.exp(-x-20)", "math.exp(x+4)-math.exp(-x-20)", 0, 0, 0]
]

def gradient_descent(f, d, x, lr=0.1, eps=1e-4):
    yield (x, f(x))
    while True:
        xn = x - lr*d(x)
        yield (xn, f(xn))
        if abs(f(xn) - f(x)) <= eps:
            return
        x = xn

for j, (a, b, c, d, e) in enumerate(tests):
    fx = eval("lambda x: {}".format(a))
    dx = eval("lambda x: {}".format(b))
    x = float(c)
    lr = float(d)
    eps = float(e)

    with open(os.path.join(tests_dir, "{:02}".format(j)), "w") as f:
        f.write("\n".join(map(str, (a,b,c,d,e))))
    with open(os.path.join(tests_dir, "{:02}.a".format(j)), "w") as f:    
        if lr != 0.:
            for i, (xi, fxi) in enumerate(gradient_descent(f, dx, x, lr, eps)):
                f.write("{}{:10.5}{:10.5}".format(i, xi, fxi))
                f.write("\n")
        else:
            for i, (xi, fxi) in enumerate(gradient_descent(f, dx, x)):
                f.write("{}{:10.5}{:10.5}".format(i, xi, fxi))
                f.write("\n")