raw_sorted = sorted(input().split(' '))
raw_sorted = sorted(raw_sorted, key=lambda x: len(x))
print(*[sum([ord(i) for i in word]) for word in raw_sorted])
