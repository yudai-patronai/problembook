from lib.testgen import TestSet


tests = TestSet()
tests.add(
    '3 2 4\n1 3 4 2\n',
    '1 3 1 3 4 2 1 3 4\n'
)
tests.add(
    '8 2 3 9\n4 2 9 3 8\n',
    '4 2 9 3 8 4 2 4 2 9 3 4 2 9\n',
)
tests.add(
    '15\n73 82 41 2 15 8 21\n',
    '73 82 41 2 15\n'
)
tests.add(
    '2 2 2\n1 2\n',
    '1 2 1 2 1 2\n'
)
tests.add(
    '1 2 3\n3 2 1\n',
    '3 2 1 3 2 3\n'
)
