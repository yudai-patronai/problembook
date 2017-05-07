#!/usr/bin/env python3

N = int(input())

k = 0
tmp = 1
while tmp < N:
    k += 1
    tmp *= 2

print(k, end='')
