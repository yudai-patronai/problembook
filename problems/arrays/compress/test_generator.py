from lib.testgen import TestSet

tests = TestSet()
tests.add("""4 5
0 1 2 3 0
0 0 1 1 1
3 2 1 0 0
0 0 6 6 6
""",'1 2 3 1 1 1 3 2 1 6 6 6')

tests.add("""2 5
1 1 1 1 0
1 1 1 0 0""",'')

tests.add("""7 7
0 0 0 0 1 1 1
2 2 2 0 0 0 0
0 3 0 3 0 3 0
0 0 0 0 4 4 4
0 5 5 0 0 5 0
0 0 0 0 6 6 6
7 0 7 0 0 7 0""",'1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7')

tests.add("""2 5
1 0 1 0 0
1 1 1 0 0""",'')
