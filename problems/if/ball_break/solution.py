#!/usr/bin/env python3

n = int(input())
m = int(input())
k = int(input())
x = int(input())

if m >= n and (k > m or m - k > x):
    print('YES')
else:
    print('NO')
