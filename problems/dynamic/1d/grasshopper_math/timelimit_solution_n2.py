#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
b = [0] * n
b[0] = 1

for i in range(1, n):
    b[i] = b[i-1]
    for j in range(0, i-1):
        if j + a[j] == i:
            b[i] = (b[i] + b[j]) % 937

print(b[-1])
