#!/usr/bin/python3

n = int(input())
m = int(input())

print('graph x {')
for _ in range(m):
    a, b = input().split()
    print('%s -- %s' % (a, b))
print('}')
