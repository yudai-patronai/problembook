from lib.testgen import TestSet
from lib.random import seed, randomint
from solution import solution

seed(42)


def to_string(n, A):
    return "{}\n{}\n".format(n, ' '.join(map(str, A)))

def random_array(lenA):
    A = [None] * lenA
    for i in range(lenA):
        A[i] = randomint(1, 100)  # for boundaries see statement.md
    return A


tests = TestSet()
tests.add(to_string(3, [1, 3, 1]), to_string(2, [0, 2]))
tests.add(to_string(4, [2, 1, 5, 1]), to_string(2, [1, 3]))
tests.add(to_string(4, [1, 1, 1, 1]), to_string(2, [1, 3]))
tests.add(to_string(6, [100, 1, 1, 100, 1, 1]), to_string(4, [1, 2, 4, 5]))

# random tests
for i in [10, 20, 30]:
    A = random_array(i)
    tests.add(to_string(i, A), to_string(*solution(i, A)))
