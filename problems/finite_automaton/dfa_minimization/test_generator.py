from lib.testgen import TestSet
from string import ascii_lowercase

tests = TestSet()

# statement tests
tests.add(
"""4 1 2
2
0 a 1
0 b 0
1 a 1
1 b 2
2 a 3
2 b 3
3 a 3
3 b 3
""", '4')

tests.add(
"""4 1 2
3
0 a 1
0 b 2
1 a 1
1 b 3
2 a 2
2 b 3
3 a 3
3 b 3
""", '3')

# trivial
tests.add(
"""1 1 1
0
0 a 0
""", '1')

# messing with input order, test from statement
tests.add(
"""4 1 2
3
2 a 2
0 a 1
3 a 3
1 a 1
2 b 3
0 b 2
3 b 3
1 b 3
""", '3')

# no terminals
tests.add(
"""1 0 1
0 a 0
""", '1')

tests.add(
"""3 0 2
0 a 1
0 b 2
1 a 1
1 b 0
2 a 1
2 b 2
""", '1')

# not trivial, already minimal
tests.add(
"""4 2 3
2 1
0 a 2
0 b 2
0 c 2
1 a 2
1 b 2
1 c 2
2 a 3
2 b 3
2 c 2
3 a 3
3 b 2
3 c 1
""", '4')

# merge into loop
tests.add(
"""3 3 1
0 1 2
0 a 1
1 a 2
2 a 2
""", '1')

# merge cycle
tests.add(
"""3 3 1
0 1 2
0 a 1
1 a 2
2 a 0
""", '1')

# do not merge cycles when not appropriate
tests.add(
"""3 1 1
2
0 a 1
1 a 2
2 a 2
""", '3')

tests.add(
"""3 1 1
2
0 a 1
1 a 2
2 a 0
""", '3')

# merge trash states and cycles
tests.add(
"""4 1 2
3
0 a 3
0 b 1
1 a 1
1 b 2
2 a 2
2 b 2
3 a 3
3 b 3
""", '3')

tests.add(
"""5 1 2
4
0 a 4
0 b 1
1 a 1
1 b 2
2 a 2
2 b 3
3 a 1
3 b 1
4 a 4
4 b 4
""", '3')

# merge branches; do not merge different branches
tests.add(
"""8 1 2
7
0 a 1
0 b 2
1 a 3
1 b 3
2 a 3
2 b 3
3 a 4
3 b 5
4 a 7
4 b 7
5 a 6
5 b 6
6 a 7
6 b 7
7 a 0
7 b 0
""", '6')

# asymptotic test, takes O(letter_num * state_num^2)
ntk = "1000 1 26\n999"
dfa_start = '\n'.join([' '.join((str(i), c, str(i+1))) for i in range(999) for c in ascii_lowercase])
dfa_end = '\n'.join(['999 ' + c + ' 999' for c in ascii_lowercase])
tests.add('\n'.join((ntk, dfa_start, dfa_end, '')), '1000')
