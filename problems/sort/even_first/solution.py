#!/usr/bin/python3

l = list(map(int, input().split()))

even = [x for x in l if x % 2 == 0]
odd = [x for x in l if x % 2 != 0]

print(' '.join(map(str, sorted(even))), ' '.join(map(str, sorted(odd))))
