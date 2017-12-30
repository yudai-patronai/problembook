#!/usr/bin/env python3

s = 0
mx = -1001
nmx = 0
a = int(input())
while a != 0:
    if a < mx:
        s += 1
    elif a == mx:
        nmx += 1
    else:
        s += nmx
        mx = a
        nmx = 1
    a = int(input())

print(s)
