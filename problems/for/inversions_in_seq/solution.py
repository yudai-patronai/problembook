#!/usr/bin/env python3

a = int(input())
n = 0

while a != 0:
    b = int(input())
    if b > a:
        n += 1
    a = b

print(n)
