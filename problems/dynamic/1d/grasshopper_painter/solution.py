#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
c[0] = 1
if a[0] == a[1] or b[0] == a[1]:
    c[1] = 1

for i in range(2, n):
    if a[i - 1] == a[i] or b[i - 1] == a[i]:
        c[i] = c[i - 1]
    if a[i - 2] == a[i] or b[i - 2] == a[i]:
        c[i] = (c[i] + c[i - 2]) % 947

print(c[-1])
