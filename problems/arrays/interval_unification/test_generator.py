from lib.testgen import TestSet

tests = TestSet()

# from statement: intersection by point & no intersection
tests.add('3\n1 2\n2 3\n3 4', '1 4\n')  # 1,2 2,3 3,4 -> 1 4
tests.add('2\n1 3\n4 5', '1 3\n4 5\n')  # 1,3 4,5 -> 1,3 4,5

# trivial
tests.add('1\n1 1', '1 1\n')

# inclusion
tests.add('5\n1 10\n1 1\n1 5\n2 3\n4 6', '1 10\n') # 1,10 1,1 1,5 2,3 4,5 -> 1,10

# intersection by interval x2
tests.add('4\n1 4\n2 5\n6 8\n7 9', '1 5\n6 9\n')

# asymptotic test
test.add(
    '100000\n' + '\n'.join([' '.join((str(n), str(n+1))) for n in range(100000)]),
    '0 100000'
)
