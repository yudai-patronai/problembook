from lib.testgen import TestSet


# function and true root
fun_root = [
    ("lin", -0.1),
    ("quad", 0.0),
    ("cub_1", 0.9654893846056297),
    ("cub_2", 0.7937005259840998),
    ("cub_3", 0.5848035476425733),
]

a, b, tol = -1.0, 1.0, 0.01

tests = TestSet()

for f_str, r in fun_root:
    question = f_str + "\n" + "{} {} {} {}\n".format(a, b, tol, r)

    tests.add(
        question,
        'YES\n'
    )
