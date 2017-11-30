#!/usr/bin/env python3

s = 0
fibs = [1, 1]
elem = int(input())
while elem != 0:
    for i in range(len(fibs), elem):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    s += fibs[elem - 1]
    elem = int(input())

print(s)
