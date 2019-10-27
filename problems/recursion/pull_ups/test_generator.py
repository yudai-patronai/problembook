from lib.testgen import TestSet


def cycle_solution(k:int, m:int):
    today = k
    for day in range(2, m+1):
        today += (k + day - 1) + (k + day - 2)
    return today


def question(k:int, m:int):
    return str(k) + '\n' + str(m) + '\n'


def answer(ans:int):
    return str(ans) + '\n'


manual_tests = [
#    K      M
    (4,     20),
    (1,     10),
    (5,     100),
    (999,   13),
    (1,     1),
    (32,    3),
    (1000,  500)
]

tests = TestSet()
for k, m in manual_tests:
    ans = cycle_solution(k, m)
    tests.add(question(k, m), answer(ans))
