from lib.testgen import TestSet

tests = TestSet()

def join_all(arr):
    return '\n'.join(arr) + '\n'

tests.add(
    join_all(["0 0", "left 1", "right 1", "stop"]),
    "0 0\n"
)
tests.add(
    join_all(["1 -1", "top 2", "left 10", "right 2", "left 2", "down 3", "stop"]),
    "-9 -2\n"
)
tests.add(
    join_all(["1 1", "top 1", "left 1", "right 1", "down 1", "stop"]),
    "1 1\n"
)
tests.add(
    join_all(["0 0"] + 5*["left 1"] + 5*["top 1"] + ["stop"]),
    "-5 5\n"
)
tests.add(
    join_all(["0 0"] + 5*["left 1"] + 5*["top 1"] + 5*["down 1"] + 5*["right 1"] + ["stop"]),
    "0 0\n"
)
tests.add(
    join_all(["0 0"] + ["stop"]),
    "0 0\n"
)