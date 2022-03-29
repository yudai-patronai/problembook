from lib.testgen import TestSet

tests = TestSet()

tests.add("""3
0 5
5 5
10 5
5""", """15""")

tests.add("""1
10 5
5""", """0""")

tests.add("""7
0 5
6 3
9 5
14 4
18 5
23 1
24 5
5""", """-1""")

tests.add("""0
1""", """0""")

tests.add("""5
0 1
2 1
5 1
10 1
15 1
5""", """16""")

tests.add("""2
10 5
5 5
5""", """0""")

tests.add("""2
5 5
0 5
5""", """10""")

