from lib.testgen import TestSet

tests = TestSet()
tests.add('4\n2 7 11 15\n9', '0 1\n') #[2, 7, 11, 15] 9
tests.add('3\n3 2 4\n6', '1 2\n') #[3, 2, 4] 6
tests.add('5\n-1 -2 -3 -4 -5\n-8', '2 4\n') # [-1,-2,-3,-4,-5] -8
tests.add('4\n-3 4 3 90\n0', '0 2\n') # [-3,4,3,90] 0
tests.add('2\n3 3\n6', '01\n') #[3, 3] 6