#!/usr/bin/env python3

N = int(input())

count = 0
while N > 0:
    count += N % 2
    N //= 2

if count > 1:
    print('NO', end='')
else:
    print('YES', end='')

# print(("YES","NO")[(N & (N-1))==0])
