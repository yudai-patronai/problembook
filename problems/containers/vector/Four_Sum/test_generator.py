from lib.testgen import TestSet
from lib.random import sample

tests = TestSet()
tests.add('0\n[]\n', '[]\n') # [] ->[]
tests.add('3\n4 4 4\n \n12', '[]\n')# [4,4,4], 12 ->  []
tests.add('4\n4 4 4 2\n16', '[]\n') # [4,4,4,2], 16
tests.add('4\n4 4 4 4\n16', '[4 4 4 4]\n') #[4,4,4,4], 16
tests.add('8\n2 7 4 0 9 5 1 3\n20', '[0 4 7 9]\n') #[2,7,4,0,9,5,1,3], 20
tests.add('8\n2 7 4 0 9 5 1 3\n120', '[]\n') #[2,7,4,0,9,5,1,3], 120
tests.add('10\n1 2 3 4 5 9 19 12 12 19\n40', '[4 5 12 19]\n') #[1,2,3,4,5,9,19,12,12,19], 40