from lib.testgen import TestSet

tests = TestSet()
tests.add('1 0 -1 0 0 5\n0 0\n', '-1 0 1 0 0 -5\n')
tests.add('4 0 5 2 8 3\n0 0\n', '-4 0 -5 -2 -8 -3\n')
tests.add('9 8 -9 -8 3 1\n2 2\n', '-5 -4 13 12 1 3\n')
tests.add('10 -20 -30 40 88 98\n-24 -32\n', '-58 -44 -18 -104 -136 -162\n')
tests.add('10 -20 -30 40 88 98\n24 32\n', '38 84 78 24 -40 -34\n')
tests.add('22 22 11 11 -11 11\n4 4\n', '-14 -14 -3 -3 19 -3\n')
tests.add('22 22 11 11 -11 11\n-8 0\n', '-38 -22 -27 -11 -5 -11\n')
tests.add('22 22 11 11 -11 11\n-200 200\n', '-422 378 -411 389 -389 389\n')
tests.add('3 1 3 2 2 2\n10 12\n', '17 23 17 22 18 22\n')
tests.add('3 1 3 2 2 2\n-20 4\n', '-43 7 -43 6 -42 6\n')
