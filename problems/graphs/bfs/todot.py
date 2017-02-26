#!/usr/bin/python3

n, m = map(int, input().split())

print('graph x {')
for _ in range(m):
    a, b = input().split()
    print('%s -- %s' % (a, b))
print('}')
