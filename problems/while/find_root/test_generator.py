from lib.testgen import TestSet
import math

def find_root(f, a, b, tol):
    eps = 1e-6
    while (b - a) > tol:
        x = (b + a) / 2.
        val = f(x)
        if abs(val) < eps:
            return x
        elif f(a) * val > 0.:
            a = x
        else:
            b = x
    return x

functions = ["def f(x): return x + 0.1", "def f(x): return x * x + 5.0 * x", "def f(x): return x * x * x - 0.9", "def f(x): return math.sin(x * x * x) - 0.2"]
a, b, tol = -1, 1, 0.01

tests = TestSet()

for el in functions:
    question = el + "\n" + str(a) + " " + str(b) + " " + str(tol)
    print(el)
    exec(el)
    answer = find_root(f, a, b, tol)

    tests.add(
        question,
        str(answer) + '\n'
    )
