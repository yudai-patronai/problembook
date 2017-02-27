#!/usr/bin/python3

n, m = map(int, input().split(' ', 2))

print('graph x {')
for _ in range(m):
    e = tuple(input().split())
    if len(e) == 3:
        print('%s -- %s [ label="%s" ]' % e)
    else:
        print('%s -- %s' % e)
print('}')
