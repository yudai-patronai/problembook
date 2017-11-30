#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = int(input())

if a + x == b and c * x == d:
    print(5)
elif a + x == b or c * x == d:
    print(4)
elif x == 1024:
    print(3)
else:
    print(2)
