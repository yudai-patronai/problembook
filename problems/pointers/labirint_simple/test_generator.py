from lib.testgen import TestSet

test_list = ["""
4 1
115# 003_ 003_ 003$
""",
"""
4 1
002$ 002_ 002_ 115#
""",
"""
4 2
115# 003_ 003_ 003$
115_ 115_ 115_ 115_
""",
"""
4 2
002$ 002_ 002_ 113#
115_ 115_ 115_ 115_
""",
"""
4 2
002$ 002_ 002_ 115#
111_ 112_ 113_ 110_
""",
"""
1 4
115#
000_
000_
000$
""",
"""
1 4
001$
001_
001_
115#
""",
"""
2 2
115# 003_
555_ 000$
""",
"""
2 2
115# 555_
003_ 000$
""",
"""
5 3
111# 003_ 555_ 555_ 555_
555_ 000_ 555_ 555_ 051_
555_ 000_ 003_ 003_ 003$
""",
"""
10 5
555_ 113# 555_ 555_ 555_ 555_ 555_ 001_ 003$ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 555_ 555_ 555_
555_ 555_ 555_ 010_ 003_ 103_ 103_ 555_ 555_ 555_
""",
"""
10 5
555_ 113_ 555_ 555_ 555_ 555_ 555_ 001_ 003$ 555_
555_ 000_ 555_ 111_ 555_ 555_ 555_ 001_ 555_ 555_
111_ 001_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 001_ 555_ 000_ 555_ 555_ 051_ 555_ 555_ 555_
555_ 111# 110_ 010_ 003_ 103_ 103_ 555_ 555_ 555_
""",
"""
10 5
555_ 113# 555_ 555_ 555_ 555_ 555_ 001_ 003_ 555_
555_ 000_ 555_ 111_ 555_ 555_ 555_ 001_ 555_ 555_
111_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 003_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 555_ 000_ 555_
555_ 555_ 110_ 010_ 003_ 103_ 103_ 002$ 000_ 555_
""",
"""
10 5
555_ 001$ 555_ 555_ 555_ 555_ 555_ 001_ 003_ 555_
555_ 002_ 001_ 111_ 555_ 555_ 555_ 001_ 555_ 555_
111_ 000_ 102_ 002_ 001_ 555_ 001_ 003_ 003_ 555_
555_ 555_ 555_ 000_ 001_ 555_ 051_ 111# 555_ 555_
555_ 555_ 110_ 010_ 002_ 002_ 002_ 000_ 555_ 555_
""",
"""
10 10
555_ 113_ 555_ 555_ 555_ 555_ 555_ 001_ 003_ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 001_ 003_ 103_ 103_ 000_ 555_ 555_
555_ 113_ 555_ 001_ 555_ 555_ 555_ 000_ 003$ 555_
555_ 000_ 555_ 001_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 001_ 103_ 003_ 555_ 555_ 001_ 003_ 111# 555_
555_ 001_ 012_ 002_ 002_ 002_ 002_ 002_ 100_ 555_
555_ 002_ 000_ 010_ 003_ 103_ 103_ 555_ 555_ 555_
""",
"""
10 20
555_ 113_ 555_ 555_ 555_ 555_ 555_ 001_ 003_ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 010_ 003_ 103_ 103_ 000_ 555_ 555_
555_ 113_ 555_ 555_ 555_ 555_ 555_ 000_ 003_ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 011_ 003_ 103_ 103_ 000_ 555_ 555_
555_ 001_ 103_ 103_ 555_ 555_ 555_ 000_ 003_ 555_
555_ 001_ 555_ 555_ 555_ 555_ 555_ 000_ 555_ 555_
555_ 111# 103_ 003_ 555_ 555_ 001_ 000_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 010_ 003_ 103_ 103_ 000_ 555_ 555_
555_ 113_ 555_ 555_ 555_ 555_ 555_ 000_ 003$ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 555_ 555_ 555_
555_ 555_ 555_ 010_ 003_ 103_ 103_ 555_ 555_ 555_
""",
"""
10 20
555_ 113_ 555_ 555_ 555_ 555_ 555_ 001_ 003_ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 010_ 003_ 103_ 103_ 000_ 555_ 555_
555_ 113_ 555_ 555_ 555_ 555_ 555_ 000_ 003_ 555_
555_ 000_ 555_ 555_ 555_ 555_ 555_ 001_ 555_ 555_
555_ 000_ 103_ 003_ 555_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 011_ 003_ 103_ 103_ 000_ 555_ 555_
555_ 001_ 103_ 103_ 555_ 555_ 555_ 000_ 003_ 555_
555_ 001_ 555_ 555_ 555_ 555_ 555_ 000_ 555_ 555_
555_ 002_ 102_ 001_ 555_ 555_ 001_ 000_ 555_ 555_
555_ 555_ 555_ 001_ 555_ 555_ 051_ 000_ 555_ 555_
555_ 555_ 555_ 012_ 001_ 103_ 103_ 000_ 555_ 555_
555_ 113_ 555_ 555_ 001_ 555_ 555_ 000_ 003$ 555_
555_ 000_ 555_ 555_ 001_ 555_ 555_ 001_ 555_ 555_
555_ 111# 103_ 003_ 003_ 555_ 001_ 003_ 555_ 555_
555_ 555_ 555_ 000_ 555_ 555_ 051_ 555_ 555_ 555_
555_ 555_ 555_ 010_ 003_ 103_ 103_ 555_ 555_ 555
"""]

tests = TestSet()

for t in test_list:
    tests.add(t, 'YES\n')
