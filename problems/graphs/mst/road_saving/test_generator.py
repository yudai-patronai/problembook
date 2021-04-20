from lib.testgen import TestSet


tests = TestSet()

tests.add(
'''15
7 9
0 1 8
0 2 6
1 2 5
2 3 7
2 4 8
2 6 4
4 5 5
4 6 3
5 6 3
''', 'YES\n'
)

tests.add(
'''30
7 9
0 1 8
0 2 6
1 2 5
2 3 7
2 4 8
2 6 4
4 5 5
4 6 3
5 6 3
''', 'NO\n'
)