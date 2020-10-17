from lib.testgen import TestSet

def solution(a, d, N):
    elems = [ a + d*i for i in range(N) ]
    A = [ sum(elems[:i+1]) for i in range(N) ]
    return A


tests = TestSet()

manual_tests = [
    (1, 1, 10),
    (10, -1, 10),
    (-10, 1, 10),
    (1, 0, 10),
    (-1, 0, 10)
    (1, 2, 50),
    (-15, 1, 31),
    (100, -5, 5),
]

for a, d, N in manual_tests:
    A = solution(a, d, N)
    tests.add(
        '{} {} {}\n'.format(a, d, N),
        ' '.join(map(str, A)) + '\n'
    )
