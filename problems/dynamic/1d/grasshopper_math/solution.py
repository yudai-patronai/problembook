#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
b = [0] * n
b[0] = 1

for i in range(0, n - 1):
    b[i + 1] = (b[i + 1] + b[i]) % 937
    if a[i] > 1 and i + a[i] < n:
        b[i + a[i]] = (b[i + a[i]] + b[i]) % 937

print(b[-1])
