#!/usr/bin/env python3

a = int(input())
op = input()
b = int(input())

if op == '<' and a < b or op == '>' and a > b:
    print('YES')
else:
    print('NO')
