raw_sorted = sorted(input().split(' '), key=lambda x: len(x))
print(*[sum([ord(i) for i in word]) for word in raw_sorted])
