#!/usr/bin/env python3

elem = int(input())
m = elem
s = 0
n = 0
while elem != 0:
    if elem < m:
        m = elem
    s += elem
    n += 1
    elem = int(input())
res = int((2*m + n) / 2 * (n+1)) - s

print(res)
