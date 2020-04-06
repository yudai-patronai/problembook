from lib.testgen import TestSet


# function and true root
fun_root = [
    ("def f(x): return x + 0.1", -0.1),
    ("def f(x): return x * x + 5.0 * x", 0.0),
    ("def f(x): return x * x * x - 0.9", 0.9654893846056297),
    ("def f(x): return x * x * x - 0.5", 0.7937005259840998),
    ("def f(x): return x * x * x - 0.2", 0.5848035476425733),
]

a, b, tol = -1.0, 1.0, 0.01

tests = TestSet()

for f_str, r in fun_root:
    question = f_str + "\n" + "{} {} {} {}\n".format(a, b, tol, r)

    tests.add(
        question,
        'YES\n'
    )
