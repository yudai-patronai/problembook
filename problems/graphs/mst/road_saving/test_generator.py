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

tests.add(
'''11
8 11
0 1 2
0 2 3
1 2 1
1 3 1
1 5 4
2 3 1
3 4 2
3 7 2
4 5 2
4 6 5
4 7 3
''', 'YES\n'
)

tests.add(
'''12
8 11
0 1 2
0 2 3
1 2 1
1 3 1
1 5 4
2 3 1
3 4 2
3 7 2
4 5 2
4 6 5
4 7 3
''', 'NO\n'
)

tests.add(
'''1
3 2
0 1 1
1 2 1
''', 'NO\n'
)

tests.add(
'''1
3 3
0 1 1
1 2 1
2 0 1
''', 'YES\n'
)