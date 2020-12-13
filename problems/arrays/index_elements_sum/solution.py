#!/usr/bin/python3

N = int(input())
res = 0
for i, x in enumerate(map(int, input().split())):
    if i % 3 == 0 and i % 7 == 0:
        res += x

print(str(res))
