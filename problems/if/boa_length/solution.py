#!/usr/bin/env python3

boa = int(input())
x = input()[0]

if x == 'm':
    boa //= 90
elif x == 'p':
    boa //= 10
elif x == 'e':
    boa //= 300

if boa == 0:
    boa = 1

print(boa)
