from lib.testgen import TestSet

tests = TestSet()

# datetime.timedelta(seconds=X) for self-check

tests.add('65\n', '0\n1\n5\n')
tests.add('3752\n', '1\n2\n32\n')
tests.add('71394\n', '19\n49\n54\n')
tests.add('81475\n', '22\n37\n55\n')
tests.add('24183\n', '6\n43\n3\n')
tests.add('0\n', '0\n0\n0\n')
tests.add('15\n', '0\n0\n15\n')
tests.add('300\n', '0\n5\n0\n')
tests.add('3601\n', '1\n0\n1\n')
