#!/usr/bin/env python3

N = int(input())

print(1, end='')
k = 2
while k * k <= N:
    print(' ', k * k, end='')
    k += 1
