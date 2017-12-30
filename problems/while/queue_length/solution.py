#!/usr/bin/env python3

s, m = 0, 0
elem = int(input())
while elem != 0:
    if elem > m:
        s += 1
        m = elem
    elem = int(input())
print(s)
