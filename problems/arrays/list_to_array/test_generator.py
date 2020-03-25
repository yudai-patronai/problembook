from lib.testgen import TestSet

tests = TestSet()
tests.add('40 3\t21 0\t17 1\t77 -1\t17 1\n', '17 21 40 77\n')
tests.add('1 3\t17 2\t25 -1\t8 1\t1 3\n', '1 8 17 25\n')
tests.add('30 1\t33 2\t55 -1\t20 0\t20 0\n', '20 30 33 55\n')
tests.add('1 1\t2 2\t3 3\t4 -1\t1 1\n', '1 2 3 4\n')
tests.add('1 -1\t2 0\t3 1\t4 2\t4 2\n', '4 3 2 1\n')
