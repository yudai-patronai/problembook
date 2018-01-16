#!/usr/bin/python3

numbers = list(map(int, input().split()))

negative = [x for x in numbers if x < 0]
positive = [x for x in numbers if x >= 0]

print(
    ' '.join(map(str, sorted(negative, reverse=True))),
    ' '.join(map(str, sorted(positive)))
)
