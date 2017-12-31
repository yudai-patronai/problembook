#!/usr/bin/env python3

a = int(input())
b = int(input())

if a == 1024 or b == 1024:
    print('BINGO')
elif a < b:
    if b % 2 == 0:
        print('NO')
    else:
        print('ZZ')
elif a > b:
    if b ** 2 == a:
        print(a * b)
    elif b < 10:
        print('NORM_SMALL')
    else:
        print('NORMAL')
else:
    print('UNKNOWN')
