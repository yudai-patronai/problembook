#!/usr/bin/python3

import sys

THRESHOLD = 0.00001


class CheckerResult:
    OK = 0
    WA = 1
    PE = 2


_in = sys.argv[1]
_out = sys.argv[2]
_ans = sys.argv[3]

with open(_in) as f:
    startup_capital = int(f.readline())
    percents = list(map(int, f.readline().split()))

try:
    with open(_out) as f:
        path1 = list(map(int, f.readline().split()))
except:
    sys.exit(CheckerResult.PE)

with open(_ans) as f:
    path2 = list(map(int, f.readline().split()))

for p, n in zip(path1, path1[1:]):
    if n-p < 2:
        sys.exit(CheckerResult.WA)

m1 = m2 = startup_capital

for i in path1[1:]:
    m1 *= (1+percents[i-1]/100)

for i in path2[1:]:
    m2 *= (1+percents[i-1]/100)

sys.exit(CheckerResult.OK if abs(m1-m2) < THRESHOLD else CheckerResult.WA)